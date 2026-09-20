# NHẬT KÝ PROMPT MINH CHỨNG SDLC - GIAI ĐOẠN KT1
**Dự án**: Hệ thống Quản lý Câu lạc bộ Sinh viên Tích hợp AI (Đề tài 28)  
**Nhóm 15**: La Văn Quyền & Nguyễn Đức Anh  

---

## 1. PROMPT PHÂN TÍCH YÊU CẦU & BẮT LỖI NGHIỆP VỤ (REQUIREMENTS ANALYSIS)

### 💬 Prompt gửi AI (Mary - BA Agent):
```text
System: Bạn là chuyên gia phân tích nghiệp vụ phần mềm (BA). 
Hãy đọc Đề tài 28: Hệ thống quản lý câu lạc bộ sinh viên có tích hợp AI. 
Hãy liệt kê danh sách điểm đau (Pain Points) của Ban chủ nhiệm CLB và đề xuất danh sách Use Cases cốt lõi cần phải có.
```

### 🤖 Phản hồi của AI:
> **Điểm đau cốt lõi**:
> 1. Trưởng ban tốn quá nhiều thời gian nhắn tin hỏi lịch rảnh và kỹ năng từng người để phân công nhiệm vụ thủ công.
> 2. Điểm danh bằng giấy dễ thất thoát và gian lận.
> 3. Khó khăn trong việc viết thông báo truyền thông sự kiện hấp dẫn sinh viên.
> 
> **Danh sách Use Cases đề xuất**:
> - `UC001`: Đăng nhập & Phân quyền RBAC 3 cấp (BCN/Leader/Member).
> - `UC002`: Quản lý Hồ sơ, Skill Matrix & Lịch rảnh.
> - `UC003`: Quản lý Sự kiện & Điểm danh QR Code tự động.
> - `UC004`: Quản lý Nhiệm vụ Kanban Board.
> - `UC005`: AI Gợi ý Phân công Nhiệm vụ.
> - `UC006`: AI Sinh bài đăng Thông báo.
> - `UC007`: AI Tóm tắt Kết quả Hoạt động.
> - `UC008`: Bảng xếp hạng Đóng góp Thành viên.

---

## 2. PROMPT THIẾT KẾ CƠ SỞ DỮ LIỆU ERD (DATABASE DESIGN)

### 💬 Prompt gửi AI (Winston - System Architect Agent):
```text
System: Bạn là Kiến trúc sư Hệ thống. Dựa trên danh sách Use Cases trên, hãy thiết kế Sơ đồ Cơ sở Dữ liệu quan hệ ERD chuẩn 3NF bao gồm các bảng: users, departments, activities, attendances, tasks, task_assignments, ai_logs.
```

### 🤖 Phản hồi của AI:
> Thiết kế 7 bảng CSDL:
> - `users`: `id`, `full_name`, `email`, `password_hash`, `role`, `department_id`, `skills` (JSON), `free_slots` (JSON).
> - `departments`: `id`, `name`, `description`.
> - `activities`: `id`, `title`, `description`, `start_time`, `end_time`, `location`, `status`, `qr_code_hash`.
> - `attendances`: `id`, `activity_id`, `user_id`, `checkin_time`, `status`.
> - `tasks`: `id`, `activity_id`, `title`, `required_skill`, `deadline`, `status`.
> - `task_assignments`: `id`, `task_id`, `user_id`, `ai_suggested`, `match_score`, `assigned_by`.
> - `ai_logs`: `id`, `user_id`, `prompt_type`, `input_data`, `output_result`, `created_at`.
