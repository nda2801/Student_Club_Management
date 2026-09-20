# Đề tài 28: Hệ thống quản lý câu lạc bộ sinh viên có tích hợp AI

## 1. Mô tả bài toán

Câu lạc bộ sinh viên cần quản lý thành viên, ban chuyên môn, hoạt động, điểm danh, nhiệm vụ và truyền thông. Nếu chỉ dùng biểu mẫu rời rạc, ban chủ nhiệm khó theo dõi đóng góp và tổng hợp hoạt động. Hệ thống cần quản lý câu lạc bộ và tích hợp AI sinh thông báo, tóm tắt hoạt động, gợi ý phân công nhiệm vụ.

## 2. Mục tiêu

- Quản lý thành viên, ban chuyên môn, hoạt động, điểm danh QR, nhiệm vụ Kanban và báo cáo thống kê.
- Tích hợp AI để sinh thông báo truyền thông, tóm tắt kết quả hoạt động, gợi ý phân công nhiệm vụ (kèm Local Rule-based Fallback Engine).
- Áp dụng quy trình SDLC chuẩn mực, container hóa toàn bộ hệ thống bằng Docker.

## 3. Yêu cầu chức năng

### 3.1. Chức năng quản lý (FR-SYS)
1. **Đăng nhập & Phân quyền (FR-SYS-01):** Xác thực tài khoản bằng Email/Password, cấp JWT Token, phân quyền 3 vai trò (Ban Chủ nhiệm, Trưởng ban, Thành viên).
2. **Quản lý Hồ sơ, Skill & Lịch rảnh (FR-SYS-02):** Cập nhật thông tin thành viên, Ma trận Kỹ năng (Skill Matrix) và Lịch rảnh (Free Slots) xác thực qua Pydantic Schema.
3. **Quản lý Ban chuyên môn (FR-SYS-03):** Quản lý cơ cấu ban, điều chuyển và phân bổ nhân sự.
4. **Quản lý Hoạt động & Điểm danh QR (FR-SYS-04):** Tạo sự kiện, sinh mã QR Code độc bản, quét QR điểm danh tức thì, chống gian lận.
5. **Quản lý Nhiệm vụ Kanban (FR-SYS-05):** Quản lý tiến độ task qua Kanban Board (To-Do, In-Progress, Done) có siết chặt RBAC.
6. **Thống kê & Bảng xếp hạng (FR-SYS-06):** Tính điểm đóng góp tự động (Contribution Score) và hiển thị Leaderboard vinh danh.

### 3.2. Chức năng AI (FR-AI)
1. **AI Sinh thông báo (FR-AI-01):** AI sinh bài viết truyền thông sự kiện theo nhiều Tone giọng (Hào hứng, Trang trọng, Thân thiện) kèm emoji sinh động.
2. **AI Tóm tắt hoạt động (FR-AI-02):** AI tổng hợp biên bản họp và phản hồi thành viên thành báo cáo 3 phần súc tích.
3. **AI Gợi ý phân công nhiệm vụ (FR-AI-03):** AI phân tích Task, Skill Matrix và Free Slots để tính Match Score (%) và gợi ý ghép cặp tối ưu (kèm Local Rule-based Fallback khi offline).

## 4. Yêu cầu kỹ thuật & Kiến trúc công nghệ

- **Backend:** Flask (Python 3.11+) + Pydantic V2 + JWT Authentication + Gunicorn WSGI.
- **Frontend:** React + Vite + CSS Responsive Component System.
- **Cơ sở dữ liệu:** PostgreSQL 16 (chuẩn hóa quan hệ qua SQLAlchemy ORM).
- **Containerization & Deployment:** Docker & Docker Compose (Orchestrate 3 services: PostgreSQL DB, Flask Backend, React-Vite Frontend).
- **AI Engine:** Google Gemini Cloud API / OpenAI API kết hợp Local Rule-based Fallback Engine.
- **Kiểm thử:** Đầy đủ Unit Test & Integration Test (25+ test cases) cho API Auth, Hoạt động, Điểm danh, Nhiệm vụ và AI.

## 5. Dữ liệu đầu vào, đầu ra và dữ liệu hệ thống

- **Dữ liệu chính:** Thành viên, ban chuyên môn, hoạt động, điểm danh, nhiệm vụ, phân công, nhật ký AI.
- **Đầu vào AI:** Mô tả hoạt động, Ma trận Kỹ năng, Lịch rảnh, phản hồi cuộc họp.
- **Đầu ra AI:** Thông báo truyền thông, báo cáo tóm tắt, bảng đề xuất phân công nhiệm vụ (JSON Pydantic Schema).

### Prompt mẫu:

```text
System: Bạn là Trợ lý Quản lý Câu lạc bộ Sinh viên. Hãy phân tích thông tin công việc và kỹ năng thành viên để đưa ra gợi ý phân công tối ưu.
User: Hoạt động: {{activity_info}}. Danh sách nhiệm vụ: {{task_list}}. Danh sách thành viên và kỹ năng: {{member_skills_free_slots}}. Hãy gợi ý ghép cặp Task - Thành viên kèm Match Score (%) và lý do.
```

## 6. Hướng dẫn sử dụng AI trong từng giai đoạn SDLC

- **KT1 (Tuần 1 - 3):** Dùng AI khảo sát hiện trạng, phân tích nghiệp vụ, thiết kế Use Case và CSDL PostgreSQL (ERD).
- **KT2 (Tuần 4 - 6):** Lập trình Backend Flask, Frontend React-Vite, xây dựng CRUD Thành viên, Sự kiện, Điểm danh QR, Nhiệm vụ Kanban và cấu hình Docker Compose.
- **KT3 (Tuần 7 - 8):** Tích hợp Prompt AI Engine (Gemini / OpenAI), xây dựng Local Rule-based Fallback và kiểm thử toàn diện.
- **Cuối kỳ (Tuần 9):** Hoàn thiện tài liệu Hướng dẫn sử dụng, Slide thuyết trình và Video Demo vận hành Docker.
