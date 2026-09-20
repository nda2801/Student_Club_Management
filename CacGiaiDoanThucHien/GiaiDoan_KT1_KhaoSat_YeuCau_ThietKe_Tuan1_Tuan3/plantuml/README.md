# BỘ SƯU TẬP MÃ NGUỒN PLANTUML (UML DIAGRAMS)
## HỆ THỐNG QUẢN LÝ CÂU LẠC BỘ SINH VIÊN CÓ TÍCH HỢP AI (ĐỀ TÀI 28)

Thư mục này chứa đầy đủ **15 tệp mã nguồn PlantUML (`.puml`)** chuẩn hóa của toàn bộ hệ thống, hỗ trợ render trực tiếp thành hình ảnh PNG/SVG thông qua VS Code extension `PlantUML`, IntelliJ IDEA, Docker PlantUML CLI, hoặc công cụ trực tuyến [PlantText](https://www.planttext.com/).

---

### 📂 Danh mục 15 Tệp Mã Nguồn PlantUML:

| STT | Tên tệp PlantUML | Loại Biểu đồ | Vị trí tương ứng trong Docs 08 | Nội dung & Mục đích |
| :---: | :--- | :--- | :--- | :--- |
| **01** | [`painpoint_to_solution.puml`](./painpoint_to_solution.puml) | **Concept / Flow** | Mục 1.4 | Ánh xạ 6 Điểm đau (Pain Points) $\rightarrow$ 6 Giải pháp Chức năng & AI |
| **02** | [`ai_functional_flow.puml`](./ai_functional_flow.puml) | **Concept / Flow** | Mục 2.2 | Luồng xử lý dữ liệu đầu vào / đầu ra của 3 tính năng AI |
| **03** | [`usecase_overall.puml`](./usecase_overall.puml) | **Use Case** | Mục 4.2 | Use Case Tổng thể toàn hệ thống (5 Phân hệ, 12 UC, 4 Tác nhân) |
| **04** | [`usecase_sub1_auth.puml`](./usecase_sub1_auth.puml) | **Use Case** | Mục 4.3.1 | Phân hệ 1: Xác thực JWT & Phân quyền RBAC (UC01, UC12) |
| **05** | [`usecase_sub2_member.puml`](./usecase_sub2_member.puml) | **Use Case** | Mục 4.3.2 | Phân hệ 2: Hồ sơ Thành viên, Skill Matrix & Ban Chuyên môn (UC02, UC11) |
| **06** | [`usecase_sub3_event.puml`](./usecase_sub3_event.puml) | **Use Case** | Mục 4.3.3 | Phân hệ 3: Sự kiện & Điểm danh QR Độc bản (UC04, UC09) |
| **07** | [`usecase_sub4_task.puml`](./usecase_sub4_task.puml) | **Use Case** | Mục 4.3.4 | Phân hệ 4: Quản lý Nhiệm vụ & Kanban Board (UC05, UC10) |
| **08** | [`usecase_sub5_ai.puml`](./usecase_sub5_ai.puml) | **Use Case** | Mục 4.3.5 | Phân hệ 5: Trợ lý AI & Báo cáo Thống kê (UC06, UC07, UC08, UC03) |
| **09** | [`class_diagram.puml`](./class_diagram.puml) | **Class Diagram** | Mục 5.1 | Lớp Phân tích & Thực thể CSDL (User, Dept, Activity, Task, AIService...) |
| **10** | [`activity_auth_login.puml`](./activity_auth_login.puml) | **Activity** | Mục 5.2.1 | Hoạt động Đăng nhập, Xác thực Bcrypt & Cấp Token JWT |
| **11** | [`activity_qr_attendance.puml`](./activity_qr_attendance.puml) | **Activity** | Mục 5.2.2 | Hoạt động Tổ chức Sự kiện & Quét QR Điểm danh qua Mobile |
| **12** | [`activity_ai_matching.puml`](./activity_ai_matching.puml) | **Activity** | Mục 5.2.3 | Hoạt động AI Smart Matchmaking với cơ chế Dual-Engine Fallback |
| **13** | [`sequence_auth_login.puml`](./sequence_auth_login.puml) | **Sequence** | Mục 5.3.1 | Tuần tự Xác thực Đăng nhập & Điều hướng vai trò |
| **14** | [`sequence_qr_checkin.puml`](./sequence_qr_checkin.puml) | **Sequence** | Mục 5.3.2 | Tuần tự Quét QR Điểm danh Realtime & Chống gian lận |
| **15** | [`sequence_ai_matchmaking.puml`](./sequence_ai_matchmaking.puml) | **Sequence** | Mục 5.3.3 | Tuần tự AI Gợi ý Phân công với Dual Fallback (< 100ms switch) |
| **16** | [`sequence_kanban_rbac.puml`](./sequence_kanban_rbac.puml) | **Sequence** | Mục 5.3.4 | Tuần tự Cập nhật Task Kanban với Kiểm soát RBAC (HTTP 401/403) |
| **17** | [`state_task_lifecycle.puml`](./state_task_lifecycle.puml) | **State Machine** | Mục 5.4.1 | Vòng đời Trạng thái Nhiệm vụ (TO_DO -> IN_PROGRESS -> DONE...) |
| **18** | [`state_activity_lifecycle.puml`](./state_activity_lifecycle.puml) | **State Machine** | Mục 5.4.2 | Vòng đời Trạng thái Sự kiện (DRAFT -> PUBLISHED -> COMPLETED...) |
| **19** | [`deployment_docker.puml`](./deployment_docker.puml) | **Deployment** | Mục 5.5 | Triển khai Kiến trúc Container 3-tier Docker Compose + Cloud AI |

---

### 🚀 Hướng dẫn Sử dụng:
- Dán nội dung của bất kỳ tệp nào vào trang web: [https://www.planttext.com](https://www.planttext.com) để xuất ảnh PNG/SVG chất lượng cao.
- Sử dụng trực tiếp trong Markdown preview trên VS Code bằng tổ hợp phím `Alt + D`.
