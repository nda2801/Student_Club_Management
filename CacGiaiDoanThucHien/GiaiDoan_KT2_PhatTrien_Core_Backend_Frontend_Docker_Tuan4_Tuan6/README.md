# GIAI ĐOẠN KT2: PHÁT TRIỂN HỆ THỐNG CỐT LÕI & CONTAINERIZATION
## PHẠM VI: TỪ TUẦN 4 ĐẾN HẾT TUẦN 6 (17/08/2026 – 06/09/2026)

---

### 1. Mục tiêu Giai đoạn KT2
1. Khởi tạo môi trường Docker Compose 3 container (`frontend:3000`, `backend:5000`, `db:5432`).
2. Hiện thực hóa Backend Flask 3.1 RESTful API kết hợp Pydantic V2 Schemas và JWT Authentication Middleware.
3. Tạo lập CSDL PostgreSQL 16 và ánh xạ SQLAlchemy ORM Models (`User`, `Department`, `Activity`, `Attendance`, `Task`, `TaskAssignment`, `AILog`).
4. Xây dựng giao diện React 18 + Vite SPA với Design System chuẩn Responsive Component System.
5. Triển khai các tính năng cốt lõi (Must Have):
   - **Tuần 4:** Đăng nhập, phân quyền RBAC 3 vai trò, bảo mật mật khẩu bằng Bcrypt.
   - **Tuần 5:** Hồ sơ Skill Matrix, Lịch rảnh cá nhân (Free Slots), Quản lý Ban chuyên môn, Tạo sự kiện & Sinh mã Dynamic QR Code UUID độc bản, Quét QR Check-in.
   - **Tuần 6:** Bảng Kanban Board kéo thả, kiểm soát RBAC sửa Task (chặn 403), Tính điểm Contribution Score & Leaderboard.

---

### 2. Danh mục Hồ sơ Tài liệu Bàn giao Giai đoạn KT2

| Tên File | Dung lượng | Mô tả Nội dung |
| :--- | :---: | :--- |
| **`05_GenAI_SoftwareDevelopment_functional-testing.docx`** | 39.3 KB | Kế hoạch kiểm thử chức năng & Danh mục Test Cases (25+ test cases cho API Auth, Event, QR, Task). |
| **`06_GenAI_SoftwareDevelopment_screenflow_db.docx`** | 38.5 KB | Thiết kế luồng màn hình UI/UX (Screen Flow) & Sơ đồ quan hệ CSDL PostgreSQL (ERD). |

---

### 3. Kế hoạch Phân công Công việc KT2 (Nhóm 15)
- **La Văn Quyền (Lead Dev / Architect):**
  - Cấu hình `docker-compose.yml`, Dockerfile Backend/Frontend.
  - Viết Flask Blueprints (`auth_bp`, `members_bp`, `activities_bp`, `attendance_bp`, `tasks_bp`).
  - Cấu hình SQLAlchemy Models, Migration và JWT Security Middleware.
- **Nguyễn Đức Anh (BA / UX / QA):**
  - Xây dựng React UI Components (Navbar, Kanban Board, QR Scanner, Skill Matrix Editor, Stats Leaderboard).
  - Viết bộ kịch bản kiểm thử Postman Test Collection và tích hợp Mock API.
