# NHẬT KÝ PROMPT MINH CHỨNG SDLC - GIAI ĐOẠN KT1
**Dự án**: Hệ thống Quản lý Câu lạc bộ Sinh viên Tích hợp AI (Đề tài 28)  
**Nhóm 15**: La Văn Quyền & Nguyễn Đức Anh  
**Giai đoạn**: KT1 (Tuần 1 - Tuần 3: Khảo sát hiện trạng, Đặc tả yêu cầu SRS & Thiết kế hệ thống)  
**Tài liệu minh chứng chuyên sâu**: Xem file [`MINH_CHUNG_AI_PHAN_TICH_YEU_CAU.md`](MINH_CHUNG_AI_PHAN_TICH_YEU_CAU.md) | File Word: [`docs/MINH_CHUNG_AI_PHAN_TICH_YEU_CAU.docx`](../docs/MINH_CHUNG_AI_PHAN_TICH_YEU_CAU.docx)

---

## 1. PROMPT BÓC TÁCH 06 ĐIỂM ĐAU TỪ DỮ LIỆU KHẢO SÁT THỰC TẾ

### 💬 Prompt gửi AI (Mary - Business Analyst Agent):
```text
System: Bạn là Chuyên gia Phân tích Nghiệp vụ Phần mềm (Senior Business Analyst).
Dự án: Xây dựng "Hệ thống Quản lý Câu lạc bộ Sinh viên Tích hợp AI" cho các trường Đại học.
Ngữ cảnh khảo sát thực tế:
Nhóm đã phỏng vấn 06 Ban Chủ nhiệm, 08 Trưởng ban chuyên môn và thu thập 120 phiếu khảo sát từ sinh viên thuộc 4 ban (Truyền thông, Sự kiện, Chuyên môn, Đối ngoại). Thực trạng hiện tại:
- Quản lý qua Zalo, Messenger, Google Sheet rời rạc.
- Trưởng ban mất hàng giờ hỏi lịch rảnh và kỹ năng của từng bạn để giao việc, thường giao sai người hoặc giao cho người đang quá tải.
- Điểm danh sự kiện bằng giấy mất 15-20 phút, dễ ký hộ, gian lận, mất file tổng kết.
- Viết bài truyền thông Facebook/Fanpage mất 2-3 tiếng duyệt qua lại, thiếu hấp dẫn.
- Sau sự kiện, phản hồi của thành viên để rải rác, không ai tổng kết ưu nhược điểm.
- Cuối kỳ xét khen thưởng cảm tính vì không có số liệu đo lường mức độ đóng góp.

Task:
Hãy phân tích và bóc tách thành 06 Điểm đau cốt lõi (Pain Points) có cấu trúc chuẩn hóa gồm:
Mã Pain Point, Tên vấn đề, Mô tả hiện trạng định lượng, Hậu quả nghiệp vụ, Tác nhân chịu ảnh hưởng trực tiếp, và Đề xuất Hướng giải quyết bằng Công nghệ / Trí tuệ Nhân tạo.
```

### 🤖 Phản hồi của AI:
> **06 Điểm đau cốt lõi (Pain Points)**:
> 1. `PP-01`: Phân công việc thủ công, sai kỹ năng & xung đột lịch học (78.3% Leader mất 1.5 - 3h/tuần; 42% task sai sở trường).
> 2. `PP-02`: Điểm danh sự kiện bằng giấy chậm trễ và gian lận (mất 15 - 25 phút; 64% vụ việc ký hộ).
> 3. `PP-03`: Theo dõi tiến độ task rời rạc, trễ hạn và thiếu phân quyền (28% task bị trôi; thành viên tự ý sửa task nhau).
> 4. `PP-04`: Soạn thảo bài truyền thông tốn thời gian, văn phong đơn điệu (mất 2 - 4h viết và duyệt; lỡ khung giờ vàng).
> 5. `PP-05`: Tóm tắt biên bản họp và phản hồi sau sự kiện chậm trễ (không nắm được điểm yếu để khắc phục).
> 6. `PP-06`: Đánh giá thi đua cuối kỳ cảm tính, thiếu minh bạch (không có số liệu đo lường; giảm động lực cống hiến).

---

## 2. PROMPT PHÂN RÃ CẤU TRÚC CHỨC NĂNG WBS (05 PHÂN HỆ)

### 💬 Prompt gửi AI (Mary - BA Agent):
```text
Dựa trên 06 điểm đau và mục tiêu xây dựng Hệ thống Quản lý CLB Sinh viên, hãy phân rã toàn bộ hệ thống phần mềm thành 05 Phân hệ nghiệp vụ cốt lõi (WBS Functional Decomposition). 
Với mỗi phân hệ, hãy xác định: Mã phân hệ, Tên phân hệ, Danh sách các chức năng con, và Vai trò người dùng phụ trách (Admin, Leader, Member).
```

### 🤖 Phản hồi của AI:
> 1. `SUB-01`: Xác thực & Phân quyền (Auth & RBAC) - 4 chức năng (Bcrypt, JWT 7 ngày, Header Bearer Token).
> 2. `SUB-02`: Quản lý Thành viên & Ban Chuyên môn - 5 chức năng (Hồ sơ, Skill Matrix, Free Slots, Cơ cấu 4 Ban).
> 3. `SUB-03`: Quản lý Sự kiện & Điểm danh QR Độc bản - 5 chức năng (Tạo sự kiện, Dynamic QR UUID v4, Quét Web/Mobile).
> 4. `SUB-04`: Quản lý Nhiệm vụ & Kanban Board - 5 chức năng (Kanban 3 cột To-Do/In-Progress/Done, Siết RBAC sửa task).
> 5. `SUB-05`: Báo cáo Thống kê & Trợ lý AI - 5 chức năng (Contribution Score Leaderboard, Content Gen, Summarizer, Matchmaking).

---

## 3. PROMPT ĐẶC TẢ YÊU CẦU CHỨC NĂNG (06 FR-SYS & 03 FR-AI)

### 💬 Prompt gửi AI (Mary - BA Agent):
```text
Hãy chuẩn hóa các chức năng trên thành danh mục Yêu cầu Chức năng Hệ thống (FR-SYS) và Yêu cầu Chức năng AI (FR-AI) theo chuẩn đặc tả phần mềm quốc tế:
Yêu cầu định dạng bảng gồm: Mã yêu cầu, Tên yêu cầu chức năng, Dữ liệu đầu vào (Input), Quy trình xử lý nghiệp vụ (Business Rules), Dữ liệu đầu ra (Output), và Tác nhân sử dụng.
Đặc biệt, các yêu cầu AI phải nêu rõ cơ chế phòng vệ khi API bên ngoài gặp sự cố hoặc timeout.
```

### 🤖 Phản hồi của AI:
> - `FR-SYS-01`: Xác thực Tài khoản & Phân quyền RBAC.
> - `FR-SYS-02`: Quản lý Hồ sơ, Ma trận Kỹ năng (Skill Matrix) & Lịch rảnh (Free Slots).
> - `FR-SYS-03`: Quản lý Cơ cấu Ban Chuyên môn & Bổ nhiệm Trưởng ban.
> - `FR-SYS-04`: Quản lý Sự kiện & Sinh mã Dynamic QR Điểm danh Độc bản.
> - `FR-SYS-05`: Quản lý Nhiệm vụ qua Kanban Board kéo thả & Kiểm soát RBAC.
> - `FR-SYS-06`: Dashboard Thống kê Chỉ số KPI Vận hành & Leaderboard Realtime.
> - `FR-AI-01`: AI Sinh Bài viết Truyền thông Sự kiện (Multi-tone Fun/Formal + Emoji).
> - `FR-AI-02`: AI Tóm tắt Biên bản Họp & Đánh giá Hoạt động (Báo cáo cấu trúc 3 phần).
> - `FR-AI-03`: AI Gợi ý Phân công Nhiệm vụ Thông minh (Dual-Engine Fallback < 100ms khi Gemini API lỗi/timeout).

---

## 4. PROMPT CHUẨN HÓA 14 YÊU CẦU PHI CHỨC NĂNG (ISO/IEC 25010)

### 💬 Prompt gửi AI (Mary - BA Agent):
```text
Hãy áp dụng tiêu chuẩn chất lượng phần mềm quốc tế ISO/IEC 25010 để xây dựng bộ Yêu cầu Phi chức năng (Non-Functional Requirements - NFR) cho hệ thống.
Bao quát 7 tiêu chí chất lượng: 
1. Hiệu năng (Performance Efficiency)
2. Bảo mật (Security)
3. Độ tin cậy (Reliability & Resilience)
4. Khả năng sử dụng (Usability)
5. Tính tương thích (Compatibility)
6. Khả năng bảo trì (Maintainability)
7. Tính di động & Triển khai (Portability)

Yêu cầu mỗi NFR phải có: Mã định danh, Chỉ số đo lường định lượng (Quantitative Metrics), Tiêu chí nghiệm thu rõ ràng (Acceptance Criteria), và Phương pháp kiểm thử cụ thể (Test Method).
```

### 🤖 Phản hồi của AI:
> Đã xây dựng 14 tiêu chuẩn chất lượng định lượng:
> - `NFR-PERF-01`: P95 API CRUD <= 500ms ở tải 200 VUs (Locust Test).
> - `NFR-PERF-02`: Thời gian phản hồi AI <= 3.0s (Async worker).
> - `NFR-SEC-01`: Mã hóa mật khẩu Bcrypt rounds >= 12.
> - `NFR-SEC-02`: Token JWT HMAC-SHA256 thời hạn 7 ngày.
> - `NFR-SEC-03`: Phân quyền RBAC HTTP 403 Forbidden chặn can thiệp task trái phép.
> - `NFR-SEC-04`: Bộ lọc phòng vệ Prompt Injection 5 tầng.
> - `NFR-REL-01`: Uptime hệ thống >= 99.5%, tự phục hồi qua Docker daemon.
> - `NFR-REL-02`: Độ trễ chuyển mạch sang Local Rule Fallback Engine < 100ms.
> - `NFR-USE-01`: Thành viên mới làm quen hệ thống trong <= 10 phút.
> - `NFR-USE-02`: Giao diện Responsive trên cả Mobile Browser và Desktop.
> - `NFR-COMP-01`: Hoạt động mượt mà trên Chrome, Edge, Safari, Firefox.
> - `NFR-MAINT-01`: Clean Architecture tách biệt Controller - Service - Model.
> - `NFR-MAINT-02`: Pydantic Schemas V2 xác thực 100% dữ liệu API.
> - `NFR-PORT-01`: Khởi chạy toàn bộ hệ thống bằng 1 lệnh `docker compose up -d`.

---

## 5. PROMPT MÔ HÌNH HÓA USE CASES & VIẾT USE CASE SPECS

### 💬 Prompt gửi AI (Mary - BA Agent & Winston - System Architect):
```text
Từ danh mục yêu cầu FR-SYS và FR-AI, hãy mô hình hóa thành 12 Ca sử dụng (Use Cases) phân bổ vào 5 gói phân hệ.
Yêu cầu:
1. Quan hệ thừa kế: Ban Chủ nhiệm (Admin), Trưởng ban (Leader), Thành viên (Member) đều thừa kế từ Người dùng Authenticated User.
2. Đổi tất cả quan hệ include của AI thành quan hệ <<extend>>.
3. Viết Đặc tả Ca sử dụng chi tiết (Use Case Specification) cho 03 ca quan trọng nhất:
   - UC04: Quản lý Sự kiện & Sinh mã Dynamic QR Điểm danh Độc bản
   - UC05: Quản lý Nhiệm vụ qua Kanban Board & Siết chặt RBAC
   - UC06: AI Gợi ý Phân công Nhiệm vụ (Smart Matchmaking)
```

### 🤖 Phản hồi của AI:
> - Danh mục 12 Use Cases (`UC01` đến `UC12`).
> - Quan hệ `<<extend>>`: UC04 extend 'Sinh mã QR độc bản'; UC09 extend 'Xác thực JWT'; UC10 extend 'RBAC Check Task Owner'; UC05 extend 'UC06 Gợi ý Phân công'; UC04 extend 'UC07 Sinh Bài đăng'; UC04 extend 'UC08 Tóm tắt Kết quả'.
> - 03 Use Case Specifications chi tiết với đầy đủ Luồng chính (Main Flow), Luồng phụ (Alternative Flow), Ngoại lệ (Exception Flow).

---

## 6. PROMPT THIẾT KẾ CƠ SỞ DỮ LIỆU ERD (7 BẢNG CHUẨN 3NF)

### 💬 Prompt gửi AI (Winston - System Architect Agent):
```text
System: Bạn là Kiến trúc sư Hệ thống. Dựa trên danh sách Use Cases và yêu cầu lưu vết minh chứng AI, hãy thiết kế Sơ đồ Cơ sở Dữ liệu quan hệ ERD chuẩn 3NF bao gồm các bảng: users, departments, activities, attendances, tasks, task_assignments, ai_logs.
```

### 🤖 Phản hồi của AI:
> Thiết kế 7 bảng CSDL PostgreSQL:
> - `users`: `id`, `full_name`, `email`, `password_hash`, `role`, `department_id`, `skills` (JSON), `free_slots` (JSON), `contribution_score`.
> - `departments`: `id`, `name`, `description`, `leader_id`.
> - `activities`: `id`, `title`, `description`, `start_time`, `end_time`, `location`, `status`, `qr_code_token`, `created_by`.
> - `attendances`: `id`, `activity_id`, `user_id`, `checkin_time`, `method`.
> - `tasks`: `id`, `activity_id`, `department_id`, `title`, `description`, `required_skills` (JSON), `deadline`, `status`, `created_by`, `assignee_id`.
> - `task_assignments`: `id`, `task_id`, `user_id`, `match_score`, `is_ai_suggested`, `suggestion_reason`, `assigned_at`.
> - `ai_logs`: `id`, `user_id`, `feature_type`, `prompt_text`, `response_payload` (JSON), `engine_used`, `execution_time_ms`, `created_at`.

---

## 7. PROMPT MA TRẬN TRUY VẾT YÊU CẦU (RTM) & PHÂN LOẠI MOSCOW

### 💬 Prompt gửi AI:
```text
Hãy lập:
1. Ma trận Phân loại Ưu tiên MoSCoW (Must, Should, Could, Won't) cho 12 Use Cases và 9 Yêu cầu chức năng.
2. Ma trận Truy vết Yêu cầu 2 chiều (Requirements Traceability Matrix - RTM) liên kết:
   Mã Yêu cầu -> Nguồn gốc Khảo sát Điểm đau -> Tác nhân Áp dụng -> Use Case Ánh xạ -> Lớp UML / Bảng CSDL PostgreSQL -> Kế hoạch Triển khai Code Flask & React (KT2).
```

### 🤖 Phản hồi của AI:
> Ma trận MoSCoW: 6 Must Have (FR-SYS-01..05, FR-AI-03), 3 Should Have (FR-SYS-06, FR-AI-01..02).
> Bảng RTM kết nối 100% yêu cầu chức năng với CSDL PostgreSQL và kế hoạch lập trình Tuần 4 - Tuần 7.
