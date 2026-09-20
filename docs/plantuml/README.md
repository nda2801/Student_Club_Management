# BỘ SƯU TẬP MÃ NGUỒN PLANTUML (UML DIAGRAMS & ERD)
## HỆ THỐNG QUẢN LÝ CÂU LẠC BỘ SINH VIÊN CÓ TÍCH HỢP AI (ĐỀ TÀI 28)

Thư mục này chứa đầy đủ **22 tệp mã nguồn PlantUML (`.puml`)** chuẩn hóa của toàn bộ hệ thống, hỗ trợ render trực tiếp thành hình ảnh PNG/SVG lưu trong thư mục `images/` phục vụ báo cáo và tài liệu kỹ thuật.

---

### 📂 Danh mục 22 Tệp Mã Nguồn PlantUML & Hình ảnh Tương ứng:

| STT | Tên tệp PlantUML | Tên ảnh đã render (`images/`) | Loại Biểu đồ | Vị trí trong Docs | Nội dung & Mục đích |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **01** | [`painpoint_to_solution.puml`](./painpoint_to_solution.puml) | `painpoint_to_solution.png` | **Concept / Flow** | Mục 1.4 Docs 08 | Ánh xạ 6 Điểm đau (Pain Points) $\rightarrow$ 6 Giải pháp Chức năng & AI |
| **02** | [`ai_functional_flow.puml`](./ai_functional_flow.puml) | `ai_functional_flow.png` | **Concept / Flow** | Mục 2.2 Docs 08 | Luồng xử lý dữ liệu đầu vào / đầu ra của 3 tính năng AI |
| **03** | [`functional_decomposition.puml`](./functional_decomposition.puml) | `functional_decomposition.png` | **WBS Decomposition** | Phụ lục Docs 08 | Cây cấu trúc phân rã chức năng toàn diện 5 phân hệ |
| **04** | [`usecase_overall.puml`](./usecase_overall.puml) | `usecase_overall.png` | **Use Case** | Mục 4.2 Docs 08 | Use Case Tổng thể toàn hệ thống (5 Phân hệ, 12 UC, 4 Tác nhân) |
| **05** | [`usecase_sub1_auth.puml`](./usecase_sub1_auth.puml) | `usecase_sub1_auth.png` | **Use Case** | Mục 4.3.1 Docs 08 | Phân hệ 1: Xác thực JWT & Phân quyền RBAC (UC01, UC12) |
| **06** | [`usecase_sub2_member.puml`](./usecase_sub2_member.puml) | `usecase_sub2_member.png` | **Use Case** | Mục 4.3.2 Docs 08 | Phân hệ 2: Hồ sơ Thành viên, Skill Matrix & Ban Chuyên môn (UC02, UC11) |
| **07** | [`usecase_sub3_event.puml`](./usecase_sub3_event.puml) | `usecase_sub3_event.png` | **Use Case** | Mục 4.3.3 Docs 08 | Phân hệ 3: Sự kiện & Điểm danh QR Độc bản (UC04, UC09) |
| **08** | [`usecase_sub4_task.puml`](./usecase_sub4_task.puml) | `usecase_sub4_task.png` | **Use Case** | Mục 4.3.4 Docs 08 | Phân hệ 4: Quản lý Nhiệm vụ & Kanban Board (UC05, UC10) |
| **09** | [`usecase_sub5_ai.puml`](./usecase_sub5_ai.puml) | `usecase_sub5_ai.png` | **Use Case** | Mục 4.3.5 Docs 08 | Phân hệ 5: Trợ lý AI & Báo cáo Thống kê (UC06, UC07, UC08, UC03) |
| **10** | [`class_diagram.puml`](./class_diagram.puml) | `class_diagram.png` | **Class Diagram** | Mục 5.1 Docs 08, Docs 04 | Lớp Phân tích & Thực thể CSDL (User, Dept, Activity, Task, AIService...) |
| **11** | [`erd_database.puml`](./erd_database.puml) | `erd_database.png` | **Database ERD** | Docs 06, Schema DB | Sơ đồ Thực thể Quan hệ CSDL (Crow's Foot notation, 7 bảng, PK, FK, Constraints) |
| **12** | [`screenflow_diagram.puml`](./screenflow_diagram.puml) | `screenflow_diagram.png` | **Screen Flow** | Docs 06, UI/UX | Sơ đồ Phân luồng 8 màn hình ứng dụng React-Vite SPA |
| **13** | [`activity_auth_login.puml`](./activity_auth_login.puml) | `activity_auth_login.png` | **Activity** | Mục 5.2.1 Docs 08 | Hoạt động Đăng nhập, Xác thực Bcrypt & Cấp Token JWT |
| **14** | [`activity_qr_attendance.puml`](./activity_qr_attendance.puml) | `activity_qr_attendance.png` | **Activity** | Mục 5.2.2 Docs 08 | Hoạt động Tổ chức Sự kiện & Quét QR Điểm danh qua Mobile |
| **15** | [`activity_ai_matching.puml`](./activity_ai_matching.puml) | `activity_ai_matching.png` | **Activity** | Mục 5.2.3 Docs 08 | Hoạt động AI Smart Matchmaking với cơ chế Dual-Engine Fallback |
| **16** | [`sequence_auth_login.puml`](./sequence_auth_login.puml) | `sequence_auth_login.png` | **Sequence** | Mục 5.3.1 Docs 08 | Tuần tự Xác thực Đăng nhập & Điều hướng vai trò |
| **17** | [`sequence_qr_checkin.puml`](./sequence_qr_checkin.puml) | `sequence_qr_checkin.png` | **Sequence** | Mục 5.3.2 Docs 08 | Tuần tự Quét QR Điểm danh Realtime & Chống gian lận |
| **18** | [`sequence_ai_matchmaking.puml`](./sequence_ai_matchmaking.puml) | `sequence_ai_matchmaking.png` | **Sequence** | Mục 5.3.3 Docs 08, Docs 04 | Tuần tự AI Gợi ý Phân công với Dual Fallback (< 100ms switch) |
| **19** | [`sequence_kanban_rbac.puml`](./sequence_kanban_rbac.puml) | `sequence_kanban_rbac.png` | **Sequence** | Mục 5.3.4 Docs 08 | Tuần tự Cập nhật Task Kanban với Kiểm soát RBAC (HTTP 401/403) |
| **20** | [`state_task_lifecycle.puml`](./state_task_lifecycle.puml) | `state_task_lifecycle.png` | **State Machine** | Mục 5.4.1 Docs 08 | Vòng đời Trạng thái Nhiệm vụ (TO_DO -> IN_PROGRESS -> DONE...) |
| **21** | [`state_activity_lifecycle.puml`](./state_activity_lifecycle.puml) | `state_activity_lifecycle.png` | **State Machine** | Mục 5.4.2 Docs 08 | Vòng đời Trạng thái Sự kiện (DRAFT -> PUBLISHED -> COMPLETED...) |
| **22** | [`deployment_docker.puml`](./deployment_docker.puml) | `deployment_docker.png` | **Deployment** | Mục 5.5 Docs 08 | Triển khai Kiến trúc Container 3-tier Docker Compose + Cloud AI |

---

### 🚀 Hướng dẫn Sử dụng & Tái tạo Hình ảnh:
- Chạy lệnh: `python render_diagrams_to_images.py` để tự động render toàn bộ 22 tệp sang thư mục `images/`.
- Dán nội dung của bất kỳ tệp nào vào trang web: [https://www.planttext.com](https://www.planttext.com) để xuất ảnh PNG/SVG thủ công nếu cần.
- Sử dụng trực tiếp trong Markdown preview trên VS Code bằng tổ hợp phím `Alt + D`.
