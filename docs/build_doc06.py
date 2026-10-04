# -*- coding: utf-8 -*-
"""
Generate Doc 06: Screen Flow & Database ERD Design
Strictly aligned with Doc 08 (Final), plantuml files, and actual codebase.
"""

import os
import sys
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from _builder_core import create_document, DOCS_DIR, CG_DIR, KT2_DIR

sys.stdout.reconfigure(encoding='utf-8')

# Table Screen Matrix (8 Screens)
scr_headers = ["Mã SCR", "Tên Màn hình", "Đường dẫn / Component", "Phân quyền RBAC", "Thao tác & Nghiệp vụ Trọng tâm", "API Endpoints Liên kết"]
scr_rows = [
    [
        "SCR-01", "Đăng nhập / Đăng ký", "/login, /register\n(Login.jsx)", "Public (Tất cả)",
        "Xác thực email/mật khẩu qua Bcrypt, cấp JWT Access Token, lưu trữ LocalStorage, chuyển đổi giữa Form Đăng nhập và Đăng ký.",
        "POST /api/auth/login\nPOST /api/auth/register"
    ],
    [
        "SCR-02", "Dashboard Tổng quan", "/dashboard\n(Dashboard.jsx)", "Admin, Leader, Member",
        "Hiển thị 4 thẻ KPI thống kê (Tổng thành viên, Sự kiện sắp tới, Nhiệm vụ đang làm, Điểm đóng góp), Lịch hoạt động tuần, Bảng xếp hạng Leaderboard Top 5 và nút điều hướng nhanh.",
        "GET /api/stats/dashboard\nGET /api/stats/leaderboard"
    ],
    [
        "SCR-03", "Quản lý Thành viên & Hồ sơ", "/members\n(Members.jsx)", "Admin, Leader, Member",
        "Hiển thị danh bạ thành viên, bộ lọc theo Ban chuyên môn; Modal cập nhật thông tin cá nhân, tích chọn Ma trận Kỹ năng (Skill Matrix) và các khung Lịch rảnh trong tuần (Free Slots).",
        "GET /api/members\nPUT /api/users/profile\nGET /api/users/profile"
    ],
    [
        "SCR-04", "Quản lý Ban Chuyên môn", "/departments\n(Members.jsx - Tab Ban)", "Admin (Quản trị viên)",
        "Xem cơ cấu 4 Ban (Truyền thông, Sự kiện, Chuyên môn, Đối ngoại), thêm Ban mới, bổ nhiệm/miễn nhiệm Trưởng ban, điều chuyển nhân sự giữa các ban.",
        "GET /api/departments\nPOST /api/departments\nPUT /api/departments/{id}"
    ],
    [
        "SCR-05", "Quản lý Sự kiện & QR", "/activities\n(Activities.jsx, QRCodeModal.jsx)", "Leader, Admin, Member",
        "Leader/Admin: Tạo sự kiện mới, cài đặt thời gian/tọa độ, kích hoạt sự kiện, mở Modal Trình chiếu Dynamic QR Code độc bản phóng to trên máy chiếu.\nMember: Bật camera điện thoại quét QR điểm danh realtime.",
        "GET /api/activities\nPOST /api/activities\nPOST /api/activities/{id}/checkin"
    ],
    [
        "SCR-06", "Quản lý Nhiệm vụ Kanban", "/tasks\n(Tasks.jsx, KanbanBoard.jsx)", "Admin, Leader, Member",
        "Bảng Kanban 3 cột trực quan (To-Do, In-Progress, Done), kéo-thả thẻ task cập nhật tiến độ, kiểm soát RBAC chỉ người làm mới được đổi task, tự động cộng điểm khi hoàn thành, tích hợp nút gọi AI Hub.",
        "GET /api/tasks\nPOST /api/tasks\nPUT /api/tasks/{id}/status"
    ],
    [
        "SCR-07", "AI Hub - Smart Matchmaking", "/aihub (Tab Phân công)\n(AIHub.jsx)", "Leader, Admin",
        "Gợi ý phân công nhiệm vụ thông minh: Leader chọn task cần giao việc, bấm 'AI Gợi ý', hệ thống tính toán Match Score % (Skills + Free Slots), hiển thị danh sách đề xuất tối ưu và nút phê duyệt 1-click. Tự động Fallback khi mất mạng.",
        "POST /api/ai/matchmaking"
    ],
    [
        "SCR-08", "AI Hub - Sinh bài & Tóm tắt", "/aihub (Tab Generator/Summary)\n(AIHub.jsx)", "Leader, Admin",
        "Tab 1: Sinh bài đăng thông báo sự kiện đa phong cách (Tone Hào hứng/Fun, Trang trọng/Formal...) chèn emoji tự động.\nTab 2: Tóm tắt biên bản cuộc họp và phản hồi thành báo cáo súc tích chuẩn 3 phần.",
        "POST /api/ai/announcement\nPOST /api/ai/summary"
    ]
]

# Table ERD 07 Tables
db_headers = ["Tên Cột (Column)", "Kiểu Dữ liệu", "Khóa / Ràng buộc", "Giá trị Mặc định", "Diễn giải Nghiệp vụ"]

t_dept_rows = [
    ["id", "SERIAL / INTEGER", "PK, AutoIncrement", "Tự tăng", "Mã định danh duy nhất của Ban chuyên môn"],
    ["name", "VARCHAR(100)", "UNIQUE, NOT NULL", "None", "Tên ban (Truyền thông, Sự kiện, Chuyên môn, Đối ngoại)"],
    ["description", "TEXT", "NULLABLE", "None", "Mô tả vai trò, nhiệm vụ và phạm vi hoạt động của Ban"]
]

t_user_rows = [
    ["id", "SERIAL / INTEGER", "PK, AutoIncrement", "Tự tăng", "Mã định danh duy nhất của người dùng"],
    ["full_name", "VARCHAR(150)", "NOT NULL", "None", "Họ và tên đầy đủ của thành viên / người dùng"],
    ["email", "VARCHAR(150)", "UNIQUE, NOT NULL, INDEX", "None", "Địa chỉ email định danh, dùng để đăng nhập hệ thống"],
    ["password_hash", "VARCHAR(255)", "NOT NULL", "None", "Mật khẩu đã được băm an toàn qua thư viện Bcrypt (salt >= 10)"],
    ["role", "VARCHAR(20)", "CHECK: ADMIN/LEADER/MEMBER", "'MEMBER'", "Vai trò phân quyền trong hệ thống (RBAC)"],
    ["department_id", "INTEGER", "FK -> departments(id)", "NULL", "Ban chuyên môn mà thành viên đang sinh hoạt (ON DELETE SET NULL)"],
    ["skills", "TEXT / JSONB", "NULLABLE", "'[]'", "Mảng JSON lưu trữ danh sách kỹ năng sở trường (Skill Matrix)"],
    ["free_slots", "TEXT / JSONB", "NULLABLE", "'[]'", "Mảng JSON lưu trữ các khung giờ rảnh cố định trong tuần (Free Slots)"],
    ["avatar_url", "VARCHAR(255)", "NULLABLE", "None", "Đường dẫn ảnh đại diện người dùng"],
    ["contribution_score", "INTEGER", "NOT NULL", "0", "Điểm đóng góp tích lũy của thành viên phục vụ xếp hạng Leaderboard"],
    ["created_at", "TIMESTAMP", "NOT NULL", "CURRENT_TIMESTAMP", "Thời điểm tạo tài khoản"]
]

t_act_rows = [
    ["id", "SERIAL / INTEGER", "PK, AutoIncrement", "Tự tăng", "Mã định danh duy nhất của sự kiện / hoạt động"],
    ["title", "VARCHAR(200)", "NOT NULL", "None", "Tiêu đề, tên hoạt động hoặc sự kiện câu lạc bộ"],
    ["description", "TEXT", "NULLABLE", "None", "Mô tả chi tiết nội dung, mục đích và yêu cầu sự kiện"],
    ["start_time", "TIMESTAMP", "NOT NULL", "None", "Thời gian bắt đầu sự kiện"],
    ["end_time", "TIMESTAMP", "NULLABLE", "None", "Thời gian kết thúc sự kiện"],
    ["location", "VARCHAR(200)", "NULLABLE", "None", "Địa điểm tổ chức sự kiện (Hội trường, phòng họp...)"],
    ["latitude", "FLOAT", "NULLABLE", "21.028511", "Tọa độ vĩ độ địa lý tổ chức sự kiện phục vụ Geofencing"],
    ["longitude", "FLOAT", "NULLABLE", "105.804817", "Tọa độ kinh độ địa lý tổ chức sự kiện phục vụ Geofencing"],
    ["radius_meters", "FLOAT", "NOT NULL", "100.0", "Bán kính cho phép điểm danh hợp lệ (mét)"],
    ["status", "VARCHAR(20)", "CHECK: UPCOMING/ONGOING/COMPLETED", "'UPCOMING'", "Trạng thái sự kiện (Sắp diễn ra, Đang diễn ra, Đã hoàn thành)"],
    ["qr_code_hash", "VARCHAR(100)", "NULLABLE, INDEX", "UUID v4", "Chuỗi mã token Dynamic QR độc bản sinh ngẫu nhiên để điểm danh"],
    ["created_by", "INTEGER", "FK -> users(id)", "NULL", "Người tạo sự kiện (Trưởng ban hoặc Admin)"],
    ["created_at", "TIMESTAMP", "NOT NULL", "CURRENT_TIMESTAMP", "Thời điểm tạo sự kiện"]
]

t_att_rows = [
    ["id", "SERIAL / INTEGER", "PK, AutoIncrement", "Tự tăng", "Mã định danh bản ghi điểm danh"],
    ["activity_id", "INTEGER", "FK -> activities(id), NOT NULL", "None", "Mã sự kiện được điểm danh (ON DELETE CASCADE)"],
    ["user_id", "INTEGER", "FK -> users(id), NOT NULL", "None", "Mã thành viên tham gia điểm danh (ON DELETE CASCADE)"],
    ["checkin_time", "TIMESTAMP", "NOT NULL", "CURRENT_TIMESTAMP", "Thời điểm chính xác thành viên thực hiện quét QR điểm danh"],
    ["status", "VARCHAR(20)", "CHECK: PRESENT/LATE/ABSENT", "'PRESENT'", "Trạng thái điểm danh (Có mặt, Đi muộn, Vắng mặt)"],
    ["device_fingerprint", "VARCHAR(255)", "NULLABLE", "None", "Chuỗi vân tay thiết bị trình duyệt di động chống gian lận"],
    ["UNIQUE Ràng buộc", "UNIQUE INDEX", "(activity_id, user_id)", "None", "Đảm bảo mỗi thành viên chỉ được điểm danh đúng 1 lần cho mỗi sự kiện"]
]

t_task_rows = [
    ["id", "SERIAL / INTEGER", "PK, AutoIncrement", "Tự tăng", "Mã định danh duy nhất của nhiệm vụ"],
    ["activity_id", "INTEGER", "FK -> activities(id), NOT NULL", "None", "Sự kiện mà nhiệm vụ này thuộc về (ON DELETE CASCADE)"],
    ["title", "VARCHAR(200)", "NOT NULL", "None", "Tiêu đề nhiệm vụ cần triển khai"],
    ["description", "TEXT", "NULLABLE", "None", "Mô tả chi tiết yêu cầu công việc và sản phẩm bàn giao"],
    ["required_skill", "VARCHAR(100)", "NULLABLE", "None", "Kỹ năng chuyên môn yêu cầu (Thiết kế, MC, Setup, Quay dựng...)"],
    ["deadline", "TIMESTAMP", "NULLABLE", "None", "Hạn chót hoàn thành nhiệm vụ"],
    ["status", "VARCHAR(20)", "CHECK: TO_DO/IN_PROGRESS/DONE", "'TO_DO'", "Trạng thái trên bảng Kanban (Cần làm, Đang làm, Hoàn thành)"]
]

t_assign_rows = [
    ["id", "SERIAL / INTEGER", "PK, AutoIncrement", "Tự tăng", "Mã định danh phân công nhiệm vụ"],
    ["task_id", "INTEGER", "FK -> tasks(id), NOT NULL", "None", "Mã nhiệm vụ được phân công (ON DELETE CASCADE)"],
    ["user_id", "INTEGER", "FK -> users(id), NOT NULL", "None", "Mã thành viên được phân công làm việc (ON DELETE CASCADE)"],
    ["ai_suggested", "BOOLEAN", "NOT NULL", "FALSE", "Cờ đánh dấu nhiệm vụ này do thuật toán AI Smart Matchmaking đề xuất"],
    ["match_score", "FLOAT", "NOT NULL", "1.0", "Điểm tương đồng kỹ năng và lịch rảnh (thang điểm 0.0 đến 1.0)"],
    ["assigned_by", "INTEGER", "FK -> users(id), NULLABLE", "NULL", "Người phê duyệt phân công (Leader hoặc Admin)"],
    ["assigned_at", "TIMESTAMP", "NOT NULL", "CURRENT_TIMESTAMP", "Thời điểm thực hiện phân công"],
    ["UNIQUE Ràng buộc", "UNIQUE INDEX", "(task_id, user_id)", "None", "Đảm bảo không phân công trùng lặp 1 người 2 lần trên cùng 1 task"]
]

t_ailog_rows = [
    ["id", "SERIAL / INTEGER", "PK, AutoIncrement", "Tự tăng", "Mã định danh nhật ký tương tác AI"],
    ["user_id", "INTEGER", "FK -> users(id), NULLABLE", "NULL", "Thành viên/Leader thực hiện yêu cầu gọi AI (ON DELETE SET NULL)"],
    ["prompt_type", "VARCHAR(50)", "NOT NULL", "None", "Loại tính năng AI (ANNOUNCEMENT, SUMMARY, RECOMMEND/MATCHMAKING)"],
    ["input_data", "TEXT", "NOT NULL", "None", "Dữ liệu văn bản thô đầu vào truyền tới bộ máy AI"],
    ["output_result", "TEXT", "NOT NULL", "None", "Kết quả văn bản Markdown hoặc cấu trúc JSON do AI sinh ra"],
    ["engine_used", "VARCHAR(50)", "NOT NULL", "'GEMINI_PRO'", "Bộ máy xử lý thực tế ('GEMINI_CLOUD' hoặc 'LOCAL_RULE_FALLBACK')"],
    ["created_at", "TIMESTAMP", "NOT NULL", "CURRENT_TIMESTAMP", "Thời điểm ghi nhận nhật ký"]
]

p6_sections = [
    ("MỤC LỤC TỔNG QUAN TÀI LIỆU", [
        "CHƯƠNG 1: KIẾN TRÚC GIAO DIỆN & PHÂN LUỒNG MÀN HÌNH (SCREEN FLOW DIAGRAM)",
        "CHƯƠNG 2: MA TRẬN ĐẶC TẢ CHI TIẾT 08 MÀN HÌNH CỐT LÕI (SCREEN SPECIFICATIONS)",
        "CHƯƠNG 3: QUY CHUẨN THIẾT KẾ GIAO DIỆN UI/UX VÀ TƯƠNG THÍCH ĐA NỀN TẢNG",
        "CHƯƠNG 4: MÔ HÌNH THỰC THỂ QUAN HỆ CƠ SỞ DỮ LIỆU (DATABASE ERD - POSTGRESQL)",
        "CHƯƠNG 5: ĐẶC TẢ CHI TIẾT 07 BẢNG CSDL QUAN HỆ (DATA DICTIONARY)",
        "CHƯƠNG 6: RÀNG BUỘC TOÀN VẸN, CHỈ MỤC B-TREE VÀ TỐI ƯU HÓA HIỆU NĂNG P95"
    ]),
    ("CHƯƠNG 1: KIẾN TRÚC GIAO DIỆN & PHÂN LUỒNG MÀN HÌNH (SCREEN FLOW DIAGRAM)", [
        "1.1 Nguyên lý Thiết kế Kiến trúc Single Page Application (React-Vite SPA):",
        "Giao diện người dùng của Hệ thống Quản lý Câu lạc bộ Sinh viên được xây dựng theo kiến trúc SPA hiện đại trên nền tảng React 18, Vite và CSS Component System chuẩn mực:",
        " - Cơ chế Định tuyến Phía máy khách (Client-side Routing): Chuyển đổi trạng thái màn hình linh hoạt giữa các tab chức năng không gây giật lag hoặc tải lại toàn trang.",
        " - Quản lý Phiên & Trạng thái Toàn cục: Token JWT và thông tin tài khoản người dùng được lưu trữ an toàn trong LocalStorage. Tầng AuthContext / Client kiểm tra tính hợp lệ của token trước khi kích hoạt các màn hình tương ứng.",
        " - Phân quyền Hiển thị Giao diện theo Vai trò (RBAC Conditional Rendering):",
        "   + Admin (Ban Chủ nhiệm): Toàn quyền truy cập mọi màn hình, bao gồm quản trị cơ cấu ban, phân quyền tài khoản và cấu hình hệ thống.",
        "   + Leader (Trưởng ban): Truy cập Dashboard, Quản lý thành viên trong ban, Tạo sự kiện, Trình chiếu QR Code, Quản lý bảng Kanban và khai thác toàn bộ Trợ lý AI Hub.",
        "   + Member (Thành viên): Truy cập Dashboard cá nhân, Cập nhật Hồ sơ (Skill Matrix & Lịch rảnh), Quét QR điểm danh bằng camera điện thoại, nhận và chuyển trạng thái nhiệm vụ cá nhân trên Kanban Board.",
        "1.2 Sơ đồ Phân luồng Màn hình Ứng dụng (Screen Flow Diagram):",
        "Sơ đồ mô hình hóa toàn bộ 08 màn hình chức năng chính và các luồng điều hướng tương tác giữa người dùng và hệ thống:",
        ('image', "screenflow_diagram.png", "Hình 1: Sơ đồ Phân luồng 8 Màn hình Ứng dụng React-Vite SPA (Screen Flow Diagram)", Inches(6.2)),
        "1.3 Phân tích Luồng Điều hướng Chính trong Hệ thống:",
        " - Luồng 1 (Khởi động & Xác thực): Người dùng truy cập hệ thống bắt đầu tại SCR-01 (Màn hình Đăng nhập). Khi xác thực thành công, hệ thống cấp JWT Token và điều hướng tức thì vào SCR-02 (Dashboard Tổng quan). Khi chọn Đăng xuất, hệ thống xóa token và đưa về SCR-01.",
        " - Luồng 2 (Điều hướng từ Dashboard): Tại SCR-02, thanh Sidebar cung cấp điều hướng nhanh tới 5 phân hệ: Quản lý Thành viên (SCR-03), Ban Chuyên môn (SCR-04), Sự kiện & Điểm danh (SCR-05), Bảng Nhiệm vụ Kanban (SCR-06) và Trợ lý AI Hub.",
        " - Luồng 3 (Tương tác Sự kiện - AI Hub): Tại màn hình Sự kiện (SCR-05), Trưởng ban có thể chuyển hướng nhanh sang SCR-08 để nhờ AI sinh nội dung thông báo truyền thông hoặc tóm tắt biên bản họp sau khi kết thúc sự kiện.",
        " - Luồng 4 (Tương tác Kanban - Smart Matchmaking): Tại bảng Kanban (SCR-06), khi cần giao nhiệm vụ, Trưởng ban nhấp nút 'AI Gợi ý Phân công' để chuyển sang SCR-07. Sau khi xem xét độ tương thích Match Score %, Leader phê duyệt để áp dụng kết quả phân công trở lại Kanban Board."
    ]),
    ("CHƯƠNG 2: MA TRẬN ĐẶC TẢ CHI TIẾT 08 MÀN HÌNH CỐT LÕI (SCREEN SPECIFICATIONS)", [
        "Bảng ma trận đặc tả chi tiết 08 màn hình chức năng, phân quyền RBAC, dữ liệu và API liên kết:",
        ('table', scr_headers, scr_rows)
    ]),
    ("CHƯƠNG 3: QUY CHUẨN THIẾT KẾ GIAO DIỆN UI/UX VÀ TƯƠNG THÍCH ĐA NỀN TẢNG", [
        "3.1 Hệ thống Thiết kế Token Màu sắc và Theme System:",
        "Giao diện hệ thống tuân thủ nghiêm ngặt tiêu chuẩn WCAG 2.1 AA về độ tương phản màu sắc và hỗ trợ chuyển đổi giao diện Sáng / Tối (Light / Dark Mode):",
        " - Primary Brand Blue: #2563EB (Tạo cảm giác tin cậy, hiện đại, năng động của sinh viên).",
        " - Neutral Backgrounds: #F8FAFC (Light Mode) và #0F172A (Dark Mode).",
        " - Functional Status Colors: Xanh lá (#16A34A - Hoàn thành / Điểm danh thành công), Vàng (#D97706 - Đang xử lý / Cảnh báo), Đỏ (#DC2626 - Quá hạn / Lỗi / Từ chối quyền).",
        " - Hệ thống Phản hồi Trực quan (Toast Notification): Component ToastContainer tự động hiển thị thông báo góc trên bên phải màn hình khi người dùng thực hiện thao tác (Đăng nhập thành công, Điểm danh thành công, Kéo task, Sinh thông báo AI...).",
        "3.2 Thiết kế Tương thích Đa Kích thước (Responsive Layout Strategy):",
        "Giao diện được tối ưu hóa responsive thông qua CSS Grid và Flexbox trên các độ phân giải phổ biến:",
        " - Desktop Màn hình lớn (1920x1080 & 1440x900): Sidebar hiển thị đầy đủ bên trái (rộng 260px), vùng nội dung chính chiếm không gian còn lại (tối đa 1400px), Bảng Kanban hiển thị đồng thời 3 cột rộng rãi.",
        " - Tablet (768x1024): Sidebar thu gọn hiển thị icon, bảng Kanban hỗ trợ thanh cuộn ngang mượt mà.",
        " - Mobile Smartphone (375x667 đến 414x896):",
        "   + Sidebar tự động ẩn vào Menu Hamburger hoặc thanh điều hướng chân trang.",
        "   + Màn hình Quét QR Điểm danh (SCR-05 / SCR-06) tối ưu hóa toàn màn hình điện thoại với khung ngắm camera chữ nhật ở chính giữa, cho phép sinh viên giơ điện thoại quét mã tức thì trong vòng 1-2 giây."
    ]),
    ("CHƯƠNG 4: MÔ HÌNH THỰC THỂ QUAN HỆ CƠ SỞ DỮ LIỆU (DATABASE ERD - POSTGRESQL)", [
        "4.1 Kiến trúc Cơ sở Dữ liệu Quan hệ Chuẩn hóa 3NF:",
        "Cơ sở dữ liệu của hệ thống được xây dựng trên hệ quản trị CSDL quan hệ mã nguồn mở mạnh mẽ PostgreSQL 16:",
        " - Vận hành trong môi trường Container hóa độc lập qua Docker Compose, dữ liệu được ánh xạ vào Docker Named Volume postgres_data để đảm bảo không bị mất mát khi tắt bật máy chủ.",
        " - Chuẩn hóa dữ liệu đạt dạng chuẩn 3NF (Third Normal Form), loại bỏ hoàn toàn các dị thường thêm/xóa/sửa (anomalies) và đảm bảo tính nhất quán tham chiếu.",
        " - Tầng truy cập dữ liệu được đóng gói thông qua SQLAlchemy ORM trong Python/Flask, tự động kiểm soát kiểu dữ liệu và tham số hóa câu lệnh SQL an toàn.",
        "4.2 Sơ đồ Thực thể - Quan hệ CSDL (PostgreSQL ERD - Crow's Foot Notation):",
        "Sơ đồ ERD mô hình hóa đầy đủ 07 bảng thực thể và 09 mối quan hệ ràng buộc khóa ngoại chặt chẽ:",
        ('image', "erd_database.png", "Hình 2: Sơ đồ Thực thể - Mối quan hệ Cơ sở dữ liệu PostgreSQL (PostgreSQL Database ERD - Crow's Foot Notation)", Inches(6.2)),
        "4.3 Danh mục 09 Mối quan hệ Quan trọng giữa các Thực thể CSDL:",
        " 1. departments -> users: Quan hệ 1 - N (Một Ban chuyên môn có nhiều thành viên tham gia, khóa ngoại users.department_id).",
        " 2. users -> activities: Quan hệ 1 - N (Một Leader/Admin khởi tạo nhiều sự kiện, khóa ngoại activities.created_by).",
        " 3. activities -> attendances: Quan hệ 1 - N (Một sự kiện ghi nhận nhiều lượt điểm danh, khóa ngoại attendances.activity_id).",
        " 4. users -> attendances: Quan hệ 1 - N (Một thành viên tham gia điểm danh nhiều sự kiện khác nhau, khóa ngoại attendances.user_id).",
        " 5. activities -> tasks: Quan hệ 1 - N (Một sự kiện lớn được phân rã thành nhiều nhiệm vụ nhỏ, khóa ngoại tasks.activity_id).",
        " 6. tasks -> task_assignments: Quan hệ 1 - N (Một nhiệm vụ có bản ghi phân công người thực hiện, khóa ngoại task_assignments.task_id).",
        " 7. users -> task_assignments: Quan hệ 1 - N (Một thành viên được phân công một hoặc nhiều nhiệm vụ, khóa ngoại task_assignments.user_id).",
        " 8. users -> task_assignments: Quan hệ 0..1 - N (Một Leader có thể là người phê duyệt nhiều phân công công việc, khóa ngoại task_assignments.assigned_by).",
        " 9. users -> ai_logs: Quan hệ 0..1 - N (Mỗi lượt gọi AI được lưu vết liên kết với người dùng thực hiện, khóa ngoại ai_logs.user_id)."
    ]),
    ("CHƯƠNG 5: ĐẶC TẢ CHI TIẾT 07 BẢNG CSDL QUAN HỆ (DATA DICTIONARY)", [
        "5.1 Bảng 1: departments (Quản lý 4 Ban Chuyên môn):",
        ('table', db_headers, t_dept_rows),
        "5.2 Bảng 2: users (Tài khoản Người dùng, RBAC, Skill Matrix & Lịch rảnh):",
        ('table', db_headers, t_user_rows),
        "5.3 Bảng 3: activities (Sự kiện, Hoạt động CLB & Dynamic QR Token):",
        ('table', db_headers, t_act_rows),
        "5.4 Bảng 4: attendances (Nhật ký Điểm danh & Chống Gian lận):",
        ('table', db_headers, t_att_rows),
        "5.5 Bảng 5: tasks (Quản lý Nhiệm vụ trên Bảng Kanban Board):",
        ('table', db_headers, t_task_rows),
        "5.6 Bảng 6: task_assignments (Phân công Nhiệm vụ & AI Smart Matchmaking):",
        ('table', db_headers, t_assign_rows),
        "5.7 Bảng 7: ai_logs (Nhật ký Thực thi Trí tuệ Nhân tạo & Fallback Audit):",
        ('table', db_headers, t_ailog_rows)
    ]),
    ("CHƯƠNG 6: RÀNG BUỘC TOÀN VẸN, CHỈ MỤC B-TREE VÀ TỐI ƯU HÓA HIỆU NĂNG P95", [
        "6.1 Chiến lược Ràng buộc Toàn vẹn Dữ liệu và Xử lý Khóa Ngoại:",
        " - Ràng buộc Chống Trùng lặp Điểm danh Tuyệt đối: UNIQUE INDEX uq_attendance_act_user ON attendances (activity_id, user_id). Ràng buộc này đảm bảo ở cấp độ CSDL rằng không có bất kỳ người dùng nào có thể điểm danh lần thứ 2 trong cùng một sự kiện, ngăn chặn hoàn toàn tình trạng spam request.",
        " - Ràng buộc Phân công Độc bản: UNIQUE INDEX uq_task_assignment ON task_assignments (task_id, user_id). Đảm bảo một thành viên không bị phân công trùng lặp hai lần vào cùng một thẻ nhiệm vụ.",
        " - Quy tắc Xóa Dữ liệu An toàn (Referential Actions):",
        "   + Cấu hình ON DELETE CASCADE cho attendances, tasks và task_assignments khi sự kiện cha bị xóa, tránh để lại các bản ghi 'mồ côi' (orphaned records).",
        "   + Cấu hình ON DELETE SET NULL cho users.department_id, activities.created_by, task_assignments.assigned_by và ai_logs.user_id. Quy tắc này đảm bảo khi một cán bộ hoặc thành viên rời CLB, toàn bộ lịch sử điểm danh, các sự kiện đã tổ chức và nhật ký hệ thống vẫn được lưu trữ nguyên vẹn.",
        " - Cơ chế Geofencing Điểm danh: Khi sự kiện kích hoạt bán kính kiểm soát, backend đối soát khoảng cách giữa tọa độ thiết bị của sinh viên và tọa độ sự kiện (Haversine formula). Nếu khoảng cách > radius_meters (mặc định 100m), hệ thống từ chối điểm danh với mã lỗi HTTP 400.",
        "6.2 Thiết kế 05 Chỉ mục B-Tree (B-Tree Indexes) Phục vụ Tối ưu hóa Truy vấn P95 <= 500ms:",
        "Để đảm bảo đáp ứng tiêu chuẩn NFR-PERF-01 (thời gian phản hồi API CRUD P95 <= 500ms, thực tế đạt 185ms) ngay cả khi dữ liệu tăng trưởng lên hàng chục nghìn bản ghi:",
        " - Index 1: CREATE UNIQUE INDEX idx_users_email ON users(email); -> Giúp thời gian truy vấn đăng nhập tìm kiếm theo email diễn ra với độ phức tạp O(log N), thời gian xử lý < 20ms.",
        " - Index 2: CREATE INDEX idx_activities_qr ON activities(qr_code_hash); -> Cho phép API xác thực mã Dynamic QR Token phản hồi tức thì cho hàng trăm sinh viên quét mã cùng lúc.",
        " - Index 3: CREATE INDEX idx_attendances_composite ON attendances(activity_id, user_id); -> Tăng tốc độ kiểm tra sinh viên đã điểm danh hay chưa.",
        " - Index 4: CREATE INDEX idx_tasks_activity_status ON tasks(activity_id, status); -> Giúp tải dữ liệu các cột Kanban Board (To-Do, In-Progress, Done) trong vòng < 60ms.",
        " - Index 5: CREATE INDEX idx_task_assign_user ON task_assignments(user_id, task_id); -> Hỗ trợ lọc nhanh danh mục 'Nhiệm vụ của tôi' của từng thành viên.",
        "6.3 Tối ưu hóa Tầng ORM SQLAlchemy & Xử lý N+1 Query:",
        " - Áp dụng kỹ thuật Eager Loading thông qua các toán tử joinedload() và selectinload() khi truy vấn bảng users và activities kèm các quan hệ liên kết, triệt tiêu bài toán N+1 Query, giảm thiểu số lượng round-trip truy vấn tới CSDL PostgreSQL xuống mức tối thiểu."
    ])
]

doc6 = create_document(
    "THIẾT KẾ PHÂN LUỒNG MÀN HÌNH VÀ CƠ SỞ DỮ LIỆU\n(SCREEN FLOW & DATABASE ERD)",
    "Giai đoạn KT1 & KT2 (Từ 27/07/2026 đến 06/09/2026 - Hết Tuần 6)",
    p6_sections
)

out_path6 = os.path.join(DOCS_DIR, "06_GenAI_SoftwareDevelopment_screenflow_db.docx")
doc6.save(out_path6)
print(f"✓ Đã tạo thành công File 06: {out_path6}")

# Sync to CacGiaiDoanThucHien
shutil.copyfile(out_path6, os.path.join(CG_DIR, "06_GenAI_SoftwareDevelopment_screenflow_db.docx"))
shutil.copyfile(out_path6, os.path.join(KT2_DIR, "06_GenAI_SoftwareDevelopment_screenflow_db.docx"))
print("  ✓ Đã đồng bộ File 06 sang CacGiaiDoanThucHien/ và KT2!")
