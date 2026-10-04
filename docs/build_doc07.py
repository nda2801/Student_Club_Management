# -*- coding: utf-8 -*-
"""
Generate Doc 07: User Guide & Operational Manual
Strictly aligned with Doc 08 (Final), user roles, and system workflows.
"""

import os
import sys
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from _builder_core import create_document, DOCS_DIR, CG_DIR, KT4_DIR

sys.stdout.reconfigure(encoding='utf-8')

# Table Roles Matrix
role_headers = ["Vai trò (Role)", "Đối tượng Áp dụng", "Phạm vi Quyền hạn (RBAC)", "Màn hình Truy cập Chính", "Nhiệm vụ Cốt lõi"]
role_rows = [
    [
        "Ban Chủ nhiệm (ADMIN)", "Chủ nhiệm, Phó Chủ nhiệm CLB", "Toàn quyền quản trị hệ thống (Full Access)",
        "Dashboard, Quản lý Ban, Quản lý Thành viên, Cấu hình RBAC, Bảng xếp hạng",
        "Quản lý cơ cấu 4 ban, bổ nhiệm Trưởng ban, điều chuyển nhân sự, theo dõi KPI toàn CLB và đánh giá thi đua khen thưởng cuối kỳ."
    ],
    [
        "Trưởng ban (LEADER)", "Trưởng ban, Phó ban chuyên môn", "Quản lý ban chuyên môn, sự kiện & nhiệm vụ",
        "Dashboard, Sự kiện & QR, Bảng Kanban Board, Trợ lý AI Hub",
        "Tạo sự kiện, kích hoạt trình chiếu mã QR điểm danh, tạo và phân chia nhiệm vụ trên Kanban, sử dụng AI sinh bài truyền thông, tóm tắt báo cáo và gợi ý phân công."
    ],
    [
        "Thành viên (MEMBER)", "Tất cả sinh viên tham gia CLB", "Quyền thành viên cá nhân (Self-Service)",
        "Dashboard, Hồ sơ cá nhân (Skill Matrix & Lịch rảnh), Quét QR Điểm danh, Nhiệm vụ của tôi",
        "Cập nhật ma trận kỹ năng sở trường, đăng ký lịch rảnh trong tuần, quét mã QR điểm danh khi tham gia sự kiện, cập nhật tiến độ công việc được giao."
    ]
]

# Table Ports and Config
env_headers = ["Biến Môi trường (Variable)", "Giá trị Mặc định", "Mô tả & Mục đích Kỹ thuật"]
env_rows = [
    ["PORT_FRONTEND", "5173", "Cổng dịch vụ Web Client (React 18 + Vite SPA)"],
    ["PORT_BACKEND", "5000", "Cổng dịch vụ REST API (Flask Python 3.11 + Gunicorn WSGI)"],
    ["DATABASE_URL", "postgresql://club_admin:club_secret_2026@db:5432/club_management", "Chuỗi kết nối Cơ sở dữ liệu quan hệ PostgreSQL 16 Container"],
    ["SECRET_KEY", "student_club_jwt_secret_key_super_secure_2026", "Khóa bí mật ký mã hóa JWT Token (HMAC-SHA256, thời hạn 24 giờ)"],
    ["GEMINI_API_KEY", "AIzaSy... (khóa cấu hình trong .env)", "Khóa xác thực dịch vụ đám mây Google Gemini AI API"],
    ["FALLBACK_TIMEOUT_SEC", "5.0", "Ngưỡng thời gian chờ gọi Cloud AI trước khi tự động kích hoạt Local Rule Matcher"]
]

p7_sections = [
    ("MỤC LỤC TỔNG QUAN TÀI LIỆU", [
        "CHƯƠNG 1: GIỚI THIỆU HỆ THỐNG VÀ HƯỚNG DẪN TRIỂN KHAI MÔI TRƯỜNG (SETUP & DEPLOYMENT)",
        "CHƯƠNG 2: HƯỚNG DẪN DÀNH CHO BAN CHỦ NHIỆM (ADMIN OPERATIONAL MANUAL)",
        "CHƯƠNG 3: HƯỚNG DẪN DÀNH CHO TRƯỞNG BAN CHUYÊN MÔN (LEADER MANUAL)",
        "CHƯƠNG 4: HƯỚNG DẪN DÀNH CHO THÀNH VIÊN CÂU LẠC BỘ (MEMBER MANUAL)",
        "CHƯƠNG 5: HƯỚNG DẪN SỬ DỤNG TRỢ LÝ TRÍ TUỆ NHÂN TẠO (AI HUB SPECIAL GUIDE)",
        "CHƯƠNG 6: CÂU HỎI THƯỜNG GẶP VÀ XỬ LÝ SỰ CỐ KỸ THUẬT (FAQ & TROUBLESHOOTING)",
        "CHƯƠNG 7: QUY TRÌNH SAO LƯU, PHỤC HỒI DỮ LIỆU & BẢO TRÌ ĐỊNH KỲ"
    ]),
    ("CHƯƠNG 1: GIỚI THIỆU HỆ THỐNG VÀ HƯỚNG DẪN TRIỂN KHAI MÔI TRƯỜNG (SETUP & DEPLOYMENT)", [
        "1.1 Tổng quan về Hệ thống Quản lý Câu lạc bộ Sinh viên có Tích hợp AI (Đề tài 28):",
        "Hệ thống Quản lý Câu lạc bộ Sinh viên Tích hợp AI là nền tảng quản trị hoạt động ngoại khóa toàn diện, giải quyết triệt để 06 Điểm đau (Pain Points) truyền thống của các CLB sinh viên: phân công công việc sai năng lực, điểm danh giấy chậm chạp, nhiệm vụ bị trôi tin nhắn trên mạng xã hội, viết bài truyền thông đơn điệu, tổng hợp báo cáo phân tán và đánh giá đóng góp cảm tính.",
        "Hệ thống phân cấp rõ ràng 3 nhóm đối tượng người dùng với quyền hạn chặt chẽ:",
        ('table', role_headers, role_rows),
        "1.2 Yêu cầu Cấu hình Hệ thống & Môi trường Vận hành:",
        " - Đối với Máy chủ Vận hành (Server / Laptop cá nhân):",
        "   + Hệ điều hành: Windows 10/11 (chạy WSL2), Ubuntu Linux 20.04/22.04 LTS, hoặc macOS.",
        "   + Phần cứng: CPU 4 cores trở lên, RAM tối thiểu 8GB (khuyến nghị 16GB), dung lượng ổ đĩa trống 10GB.",
        "   + Phần mềm cài đặt sẵn: Docker Desktop (phiên bản 4.x) hoặc Docker Engine + Docker Compose V2, Git.",
        " - Đối với Người dùng cuối (Clients):",
        "   + Máy tính hoặc Điện thoại thông minh (iOS/Android) có kết nối mạng Internet/Wifi nội bộ.",
        "   + Trình duyệt Web hiện đại hỗ trợ Camera Web API: Google Chrome, Microsoft Edge, Safari, Firefox.",
        "1.3 Hướng dẫn Triển khai và Khởi chạy Hệ thống Chỉ với 1 Câu lệnh (1-Command Docker Startup):",
        "Hệ thống đã được đóng gói toàn diện thành các Container Docker độc lập. Để đưa toàn bộ hệ thống vào hoạt động:",
        " - Bước 1: Mở Terminal (Command Prompt / PowerShell trên Windows hoặc Terminal trên Linux/macOS) tại thư mục gốc của dự án.",
        " - Bước 2: Kiểm tra cấu hình file .env tại thư mục gốc. Danh mục các thông số cấu hình cốt lõi:",
        ('table', env_headers, env_rows),
        " - Bước 3: Thực thi câu lệnh khởi chạy Docker Compose duy nhất:",
        "   docker-compose up --build -d",
        " - Bước 4: Kiểm tra trạng thái hoạt động của 3 Containers qua lệnh: docker ps. Đảm bảo các containers db, backend và frontend đều ở trạng thái 'Up' (Healthy).",
        " - Bước 5: Truy cập hệ thống trên trình duyệt Web:",
        "   + Địa chỉ Giao diện Người dùng: http://localhost:5173",
        "   + Địa chỉ Cổng API Backend: http://localhost:5000",
        "   + Kiểm tra API Health: http://localhost:5000/api/stats/dashboard",
        " - Bước 6: Khởi tạo Dữ liệu Mẫu (Initial Seed Data): Mở terminal và chạy lệnh nạp dữ liệu mẫu ban đầu: docker exec -it student_club_backend python seed_data.py. Lệnh này sẽ tạo sẵn 4 ban chuyên môn, các tài khoản Admin, Leader, Member mẫu, cùng các sự kiện và nhiệm vụ mẫu để trải nghiệm ngay lập tức."
    ]),
    ("CHƯƠNG 2: HƯỚNG DẪN DÀNH CHO BAN CHỦ NHIỆM (ADMIN OPERATIONAL MANUAL)", [
        "2.1 Đăng nhập & Quản lý Phân quyền Hệ thống (UC01, UC12):",
        " - Bước 1: Truy cập trang đăng nhập tại địa chỉ http://localhost:5173/login.",
        " - Bước 2: Nhập thông tin tài khoản Quản trị viên (Mặc định: email admin@club.edu.vn, mật khẩu Admin@123) -> Nhấn 'Đăng nhập'.",
        " - Bước 3: Sau khi xác thực thành công, hệ thống cấp JWT Access Token và tự động chuyển hướng tới Dashboard Quản trị. Admin có thể xem toàn bộ danh sách thành viên, trạng thái tài khoản và phân cấp vai trò (Admin, Leader, Member).",
        "2.2 Quản trị Cơ cấu 4 Ban Chuyên môn (UC11 / FR-SYS-03):",
        " - Bước 1: Trên thanh điều hướng chính, chọn mục 'Quản lý Ban'.",
        " - Bước 2: Màn hình hiển thị danh sách 4 ban chuyên môn: Ban Truyền thông, Ban Sự kiện, Ban Chuyên môn, Ban Đối ngoại.",
        " - Bước 3: Bổ nhiệm Trưởng ban: Nhấp vào nút 'Chỉnh sửa' tại ban tương ứng, chọn thành viên từ danh sách thả xuống để bổ nhiệm làm Trưởng ban (Leader). Hệ thống tự động nâng cấp vai trò của thành viên đó lên Leader.",
        " - Bước 4: Thêm Ban mới: Bấm 'Thêm Ban mới', nhập Tên ban và Mô tả chức năng -> Bấm 'Lưu'. Hệ thống kiểm tra ràng buộc không cho phép tạo trùng tên ban.",
        " - Bước 5: Điều chuyển nhân sự: Chọn thành viên cần chuyển và chọn ban tiếp nhận từ danh sách để hoàn tất điều chuyển.",
        "2.3 Theo dõi Dashboard Điều hành & Bảng Xếp hạng Leaderboard (UC03 / FR-SYS-06):",
        " - Theo dõi 4 thẻ KPI tổng quan: Tổng số thành viên đang sinh hoạt, Số sự kiện sắp diễn ra trong tuần, Số nhiệm vụ đang thực hiện và Tỷ lệ hoàn thành công việc.",
        " - Giám sát Bảng xếp hạng Leaderboard: Xem danh sách thành viên có Điểm Đóng góp (Contribution Score) cao nhất. Hệ thống phân loại huy hiệu vinh danh (Kim cương, Vàng, Bạc, Đồng) minh bạch, làm căn cứ chính xác để khen thưởng và trao giấy chứng nhận cuối kỳ."
    ]),
    ("CHƯƠNG 3: HƯỚNG DẪN DÀNH CHO TRƯỞNG BAN CHUYÊN MÔN (LEADER MANUAL)", [
        "3.1 Tạo Sự kiện Mới & Kích hoạt Trình chiếu Mã QR Điểm danh Độc bản (UC04 / FR-SYS-04):",
        " - Bước 1: Vào mục 'Sự kiện' trên thanh điều hướng -> Nhấn nút 'Tạo Sự kiện mới'.",
        " - Bước 2: Điền đầy đủ thông tin: Tiêu đề sự kiện (ví dụ: 'Workshop Kỹ năng Thiết kế GenAI'), Thời gian bắt đầu và kết thúc, Địa điểm tổ chức (Hội trường A1), Bán kính kiểm soát Geofencing (mặc định 100m) và Mô tả nội dung -> Nhấn 'Tạo sự kiện'.",
        " - Bước 3: Hệ thống tự động sinh một chuỗi mã Dynamic QR Token độc bản UUID v4 duy nhất cho sự kiện này.",
        " - Bước 4: Khi sự kiện bắt đầu, Trưởng ban chuyển trạng thái sự kiện sang 'Đang diễn ra' (ONGOING) và nhấp nút 'Trình chiếu Mã QR'.",
        " - Bước 5: Màn hình hiển thị mã QR Code phóng to toàn màn hình máy chiếu hoặc màn hình hội trường để các thành viên quét bằng điện thoại. Trưởng ban có thể theo dõi danh sách sinh viên check-in thành công tăng lên theo thời gian thực.",
        "3.2 Quản trị Nhiệm vụ trên Bảng Kanban Board (UC05 / FR-SYS-05):",
        " - Bước 1: Vào mục 'Nhiệm vụ' để mở giao diện Bảng Kanban 3 cột trực quan: Cần làm (To-Do), Đang làm (In-Progress), Hoàn thành (Done).",
        " - Bước 2: Tạo thẻ nhiệm vụ mới: Nhấn nút 'Thêm Nhiệm vụ', nhập Tiêu đề task, Mô tả yêu cầu, chọn Kỹ năng chuyên môn yêu cầu (Required Skill: Thiết kế, MC, Setup, Content...), thiết lập Hạn chót (Deadline) và chọn thành viên trong ban để gán việc.",
        " - Bước 3: Theo dõi và điều phối: Kéo thả các thẻ nhiệm vụ giữa các cột để cập nhật tiến độ công việc của ban. Hệ thống hiển thị cảnh báo viền đỏ đối với các task bị quá hạn.",
        " - Bước 4: Sử dụng Trợ lý AI Phân công: Nếu chưa biết phân công ai, nhấp nút 'AI Gợi ý Phân công' ngay trên thanh công cụ để hệ thống tự động tìm người phù hợp nhất."
    ]),
    ("CHƯƠNG 4: HƯỚNG DẪN DÀNH CHO THÀNH VIÊN CÂU LẠC BỘ (MEMBER MANUAL)", [
        "4.1 Đăng ký, Đăng nhập & Thiết lập Ma trận Kỹ năng - Lịch rảnh (UC01, UC02 / FR-SYS-02):",
        " - Bước 1: Đăng nhập vào hệ thống bằng tài khoản thành viên cá nhân (email và mật khẩu do BCN cấp hoặc tự đăng ký).",
        " - Bước 2: Truy cập vào mục 'Hồ sơ cá nhân'.",
        " - Bước 3: Thiết lập Ma trận Kỹ năng (Skill Matrix): Tích chọn các ô kỹ năng là sở trường của bản thân (ví dụ: Thiết kế đồ họa Photoshop/Canva, Dẫn chương trình MC, Setup âm thanh ánh sáng, Viết bài Content, Quay dựng video TikTok/CapCut...).",
        " - Bước 4: Thiết lập Lịch rảnh cố định (Free Slots): Tích chọn các buổi rảnh trong tuần không bị vướng lịch học (Sáng, Chiều, Tối từ Thứ 2 đến Chủ nhật) -> Nhấn 'Lưu hồ sơ'.",
        " - Lợi ích: Khi có dữ liệu kỹ năng và lịch rảnh chính xác, bộ máy AI sẽ tự động đề xuất phân công bạn vào đúng các công việc bạn yêu thích và vào khung giờ bạn rảnh rỗi.",
        "4.2 Quét Mã Dynamic QR Điểm danh qua Điện thoại Di động (UC09 / FR-SYS-04):",
        " - Bước 1: Khi có mặt tại địa điểm diễn ra sự kiện, dùng trình duyệt điện thoại (Chrome/Safari) truy cập hệ thống -> Chọn mục 'Điểm danh QR'.",
        " - Bước 2: Cho phép trình duyệt truy cập Camera -> Hướng camera về phía mã QR đang được trình chiếu trên màn hình lớn của hội trường.",
        " - Bước 3: Trong vòng 1-2 giây, hệ thống phát tiếng thông báo và hiển thị hộp thoại màu xanh: 'Điểm danh thành công! Bạn được cộng +5 điểm đóng góp'.",
        " - Lưu ý: Mỗi sự kiện chỉ được quét điểm danh 1 lần duy nhất. Nếu quét lại lần 2, hệ thống sẽ báo lỗi 'Bạn đã điểm danh sự kiện này rồi'.",
        "4.3 Theo dõi & Cập nhật Trạng thái Nhiệm vụ Cá nhân (UC10 / FR-SYS-05):",
        " - Bước 1: Vào mục 'Nhiệm vụ', chọn bộ lọc 'Nhiệm vụ của tôi' để xem danh sách công việc Trưởng ban giao cho bạn.",
        " - Bước 2: Khi bắt đầu thực hiện, kéo thẻ task từ cột 'Cần làm' (To-Do) sang cột 'Đang làm' (In-Progress).",
        " - Bước 3: Khi hoàn thành công việc, kéo task sang cột 'Hoàn thành' (Done): Hệ thống tự động ghi nhận bạn hoàn tất nhiệm vụ và tự động cộng +10 Điểm Đóng góp (Contribution Score) vào hồ sơ của bạn.",
        " - Lưu ý bảo mật: Theo cơ chế phân quyền RBAC, thành viên chỉ có quyền thay đổi trạng thái của chính nhiệm vụ được phân công cho mình, không thể sửa task của người khác.",
        "4.4 Tra cứu Bảng Xếp hạng (Leaderboard) & Điểm Đóng góp Cá nhân (UC03 / FR-SYS-06):",
        " - Truy cập mục 'Bảng xếp hạng' để xem thứ hạng thi đua của bản thân trong ban và trong toàn CLB.",
        " - Công thức tích lũy điểm: +5 điểm cho mỗi lần tham gia sự kiện và điểm danh QR đúng giờ; +10 điểm cho mỗi nhiệm vụ hoàn thành đúng hạn; -2 điểm nếu để nhiệm vụ bị trễ deadline."
    ]),
    ("CHƯƠNG 5: HƯỚNG DẪN SỬ DỤNG TRỢ LÝ TRÍ TUỆ NHÂN TẠO (AI HUB SPECIAL GUIDE)", [
        "Trợ lý Trí tuệ Nhân tạo (AI Hub) tích hợp kiến trúc Dual-Engine hiện đại, hỗ trợ 3 tính năng tự động hóa vượt trội:",
        "5.1 Tính năng 1: AI Sinh Bài viết Thông báo Sự kiện Đa Phong cách (UC07 / FR-AI-01):",
        " - Bước 1: Vào mục 'Trợ lý AI' trên menu -> Chọn Tab 'Sinh Thông báo Sự kiện'.",
        " - Bước 2: Nhập thông tin thô sự kiện: Tên chương trình, Thời gian tổ chức, Địa điểm, Đối tượng tham gia và Nội dung hoạt động nổi bật.",
        " - Bước 3: Lựa chọn Phong cách (Tone giọng):",
        "   + Tone 'Hào hứng / Trẻ trung' (Fun): Dành cho các hoạt động dã ngoại, teambuilding, giao lưu văn nghệ (văn phong sôi nổi, nhiều emoji sinh động, lời kêu gọi hấp dẫn).",
        "   + Tone 'Trang trọng / Lịch thiệp' (Formal): Dành cho Đại hội CLB, Tọa đàm chuyên môn, Lễ ký kết hợp tác (văn phong chuẩn mực, nghiêm túc, đúng văn phong hành chính).",
        "   + Tone 'Thân thiện / Cổ vũ' (Friendly): Dành cho các buổi sinh hoạt thường kỳ, họp mặt chào đón tân sinh viên.",
        " - Bước 4: Nhấn nút 'AI Sinh Thông báo'. Trong vòng 2-3 giây, hệ thống trả về bài viết hoàn chỉnh định dạng Markdown.",
        " - Bước 5: Nhấn nút 'Sao chép bài viết' để dán trực tiếp lên Fanpage Facebook hoặc gửi vào nhóm chat Zalo của CLB.",
        "5.2 Tính năng 2: AI Tóm tắt Kết quả Hoạt động & Báo cáo 3 Phần (UC08 / FR-AI-02):",
        " - Bước 1: Chọn Tab 'Tóm tắt Báo cáo' trong AI Hub.",
        " - Bước 2: Dán nội dung biên bản cuộc họp dài dòng, các ý kiến phản hồi thô của thành viên sau sự kiện vào ô văn bản.",
        " - Bước 3: Nhấn nút 'AI Tóm tắt'.",
        " - Bước 4: Hệ thống tự động phân tích và trích xuất cấu trúc báo cáo chuẩn mực gồm 3 phần rõ ràng:",
        "   + Phần 1: Kết quả nổi bật đạt được (Số lượng tham gia, mục tiêu đã hoàn thành).",
        "   + Phần 2: Các tồn tại và hạn chế (Các sự cố phát sinh, khâu chuẩn bị chưa chu đáo).",
        "   + Phần 3: Đề xuất hành động cải tiến cho sự kiện lần sau.",
        "5.3 Tính năng 3: AI Gợi ý Phân công Nhiệm vụ Thông minh (UC06 / FR-AI-03):",
        " - Bước 1: Chọn Tab 'Gợi ý Phân công'.",
        " - Bước 2: Chọn nhiệm vụ cần giao việc từ danh sách thẻ task đang chờ phân công.",
        " - Bước 3: Nhấn nút 'AI Gợi ý'.",
        " - Bước 4: Thuật toán AI Smart Matchmaking sẽ tự động đối soát kỹ năng yêu cầu của task với Ma trận Kỹ năng (Skill Matrix) và Lịch rảnh (Free Slots) của toàn bộ thành viên trong ban.",
        " - Bước 5: Màn hình hiển thị danh sách thành viên đề xuất kèm theo chỉ số Match Score % (ví dụ: 'Nguyễn Văn A - Match Score 95% - Có kỹ năng Thiết kế Photoshop, rảnh Thứ 7').",
        " - Bước 6: Trưởng ban nhấp nút 'Phê duyệt' để áp dụng phân công ngay lập tức mà không tốn công sức nhắn tin hỏi từng người.",
        "5.4 Vận hành Ngoại tuyến với Cơ chế Dual-Engine Fallback (NFR-REL-02 / NFR-PERF-03):",
        " - Hệ thống được trang bị bộ chuyển đổi thông minh: Bình thường, hệ thống ưu tiên gọi dịch vụ đám mây Google Gemini AI API để cho ra kết quả ngôn ngữ tự nhiên chất lượng cao nhất.",
        " - Khi máy chủ mất kết nối Internet hoặc dịch vụ đám mây gặp sự cố timeout (> 5 giây), hệ thống tự động kích hoạt bộ máy Local Rule-based Matcher chạy cục bộ trên máy chủ trong thời gian < 100ms.",
        " - Trưởng ban vẫn nhận được kết quả gợi ý phân công chính xác dựa trên thuật toán luật cục bộ mà không hề gặp thông báo lỗi hay gián đoạn công việc."
    ]),
    ("CHƯƠNG 6: CÂU HỎI THƯỜNG GẶP VÀ XỬ LÝ SỰ CỐ KỸ THUẬT (FAQ & TROUBLESHOOTING)", [
        "6.1 Sự cố Tài khoản & Đăng nhập:",
        " - Hỏi: Tôi đăng nhập nhưng hệ thống báo lỗi 'Invalid credentials'?",
        "   Trả lời: Hãy kiểm tra lại chính xác email và mật khẩu của bạn. Chú ý phím Caps Lock khi nhập mật khẩu.",
        " - Hỏi: Tôi nhận được thông báo lỗi HTTP 403 Forbidden 'Insufficient permissions'?",
        "   Trả lời: Bạn đang cố gắng truy cập vào chức năng hoặc API vượt quá thẩm quyền vai trò của bạn (ví dụ: Thành viên cố tình gọi API tạo ban hoặc sửa task của người khác). Hãy liên hệ Ban Chủ nhiệm nếu bạn cần nâng quyền.",
        "6.2 Sự cố Quét QR Điểm danh:",
        " - Hỏi: Mở chức năng quét QR nhưng trình duyệt không hiển thị camera?",
        "   Trả lời: Hãy kiểm tra và cấp quyền truy cập Camera cho trình duyệt (trên Chrome/Safari vào Cài đặt trang web -> Quyền Camera -> Chọn Cho phép).",
        " - Hỏi: Tôi quét mã nhưng hệ thống báo 'Sự kiện hiện không trong thời gian cho phép điểm danh'?",
        "   Trả lời: Hãy liên hệ Trưởng ban kiểm tra xem sự kiện đã được chuyển sang trạng thái 'Đang diễn ra' (ONGOING) hay chưa.",
        " - Hỏi: Tôi quét mã nhưng hệ thống báo lỗi 'Vị trí của bạn nằm ngoài bán kính tổ chức sự kiện'?",
        "   Trả lời: Sự kiện này có bật tính năng kiểm soát khoảng cách Geofencing. Bạn cần bật định vị GPS trên điện thoại và có mặt trong bán kính 100m tại địa điểm tổ chức để điểm danh hợp lệ.",
        "6.3 Sự cố Trợ lý AI:",
        " - Hỏi: Khi mạng Internet bị ngắt, tính năng gợi ý phân công có hoạt động không?",
        "   Trả lời: Có! Hệ thống tích hợp cơ chế Dual-Engine Fallback, tự động chuyển đổi sang bộ máy Local Rule Matcher chạy cục bộ trong < 100ms mà không làm gián đoạn công việc của bạn.",
        " - Hỏi: Tôi nhập yêu cầu nhưng AI báo 'Nội dung bị từ chối do vi phạm an toàn'?",
        "   Trả lời: Hệ thống có bộ lọc bảo mật phòng chống Prompt Injection. Vui lòng không nhập các câu lệnh can thiệp vào chỉ thị hệ thống hoặc mã độc hại.",
        "6.4 Sự cố Khởi động Docker Containers:",
        " - Hỏi: Chạy lệnh 'docker-compose up' bị báo lỗi cổng 5000 hoặc 5173 đã được sử dụng (Port is already allocated)?",
        "   Trả lời: Kiểm tra xem có ứng dụng nào khác đang chiếm cổng 5000/5173 trên máy không. Tắt các ứng dụng đó hoặc đổi cổng ánh xạ trong file docker-compose.yml."
    ]),
    ("CHƯƠNG 7: QUY TRÌNH SAO LƯU, PHỤC HỒI DỮ LIỆU & BẢO TRÌ ĐỊNH KỲ", [
        "7.1 Quy trình Sao lưu Dữ liệu Định kỳ (Database Backup):",
        "Để đảm bảo an toàn tuyệt đối cho dữ liệu của câu lạc bộ, quản trị viên thực hiện sao lưu định kỳ hàng tuần:",
        " - Bước 1: Mở Terminal máy chủ.",
        " - Bước 2: Thực thi lệnh pg_dump xuất toàn bộ CSDL ra file sao lưu:",
        "   docker exec -t student_club_db pg_dump -U club_admin club_management > backup_club_$(date +%Y%m%d).sql",
        " - Bước 3: Lưu trữ file backup vào thư mục lưu trữ an toàn hoặc tải lên đám mây bảo mật.",
        "7.2 Quy trình Phục hồi Dữ liệu khi Gặp Sự cố (Disaster Recovery):",
        "Khi máy chủ gặp sự cố hoặc cần khôi phục lại dữ liệu từ bản sao lưu cũ:",
        " - Bước 1: Khởi động container CSDL bằng lệnh: docker-compose up -d db",
        " - Bước 2: Thực thi lệnh phục hồi dữ liệu từ file backup:",
        "   docker exec -i student_club_db psql -U club_admin -d club_management < backup_club_YYYYMMDD.sql",
        " - Bước 3: Khởi động lại toàn bộ hệ thống bằng lệnh: docker-compose up -d",
        "7.3 Bảo trì Hệ thống & Quản lý Docker Named Volume:",
        " - Toàn bộ dữ liệu PostgreSQL được ánh xạ vào Docker Named Volume có tên postgres_data. Khi cần cập nhật mã nguồn (git pull), quản trị viên chỉ cần chạy docker-compose down rồi docker-compose up --build -d. Dữ liệu tài khoản, sự kiện và điểm danh hoàn toàn nguyên vẹn và bền vững."
    ])
]

doc7 = create_document(
    "HƯỚNG DẪN SỬ DỤNG VÀ VẬN HÀNH HỆ THỐNG\n(USER GUIDE & OPERATIONAL MANUAL)",
    "Giai đoạn KT1 & KT4 (Từ 27/07/2026 đến 27/09/2026 - Hết Tuần 9)",
    p7_sections
)

out_path7 = os.path.join(DOCS_DIR, "07_GenAI_SoftwareDevelopment_user-guide.docx")
doc7.save(out_path7)
print(f"✓ Đã tạo thành công File 07: {out_path7}")

# Sync to CacGiaiDoanThucHien
shutil.copyfile(out_path7, os.path.join(CG_DIR, "07_GenAI_SoftwareDevelopment_user-guide.docx"))
shutil.copyfile(out_path7, os.path.join(KT4_DIR, "07_GenAI_SoftwareDevelopment_user-guide.docx"))
print("  ✓ Đã đồng bộ File 07 sang CacGiaiDoanThucHien/ và KT4!")
