# NHẬT KÝ PROMPT MINH CHỨNG SDLC - GIAI ĐOẠN KT2
**Dự án**: Hệ thống Quản lý Câu lạc bộ Sinh viên Tích hợp AI (Đề tài 28)  
**Nhóm 15**: La Văn Quyền & Nguyễn Đức Anh  

---

## 1. PROMPT SINH MÃ NGUỒN BACKEND FLASK

### 💬 Prompt gửi AI (Amelia - Senior Dev Agent):
```text
System: Bạn là Kỹ sư phần mềm Backend. Hãy viết mã nguồn Flask RESTful API xử lý Authentication JWT, CRUD Thành viên, Sự kiện và Mã QR Điểm danh động. 
Yêu cầu:
1. Mã QR cá nhân phải độc bản theo user_id và có thời hạn đến hết end_time của sự kiện.
2. Khi quét mã QR cá nhân, hệ thống tự động duyệt điểm danh (status = PRESENT) ngay lập tức mà không cần Admin duyệt thủ công.
3. Siết chặt phân quyền RBAC: Thành viên chỉ được đổi trạng thái nhiệm vụ được giao cho chính mình.
```

### 🤖 Phản hồi của AI:
> Đã phát triển thành công các module:
> - `app/api/auth.py`: JWT Token login & RBAC role checker.
> - `app/api/activities.py`: Endpoint `GET /{activity_id}/my-qr` sinh JWT Token QR độc bản cá nhân & Endpoint `POST /checkin` tự động phê duyệt điểm danh tức thì.
> - `app/api/tasks.py`: Middleware kiểm tra quyền RBAC HTTP 403 Forbidden.

---

## 2. PROMPT SINH GIAO DIỆN REACT FRONTEND (UI/UX)

### 💬 Prompt gửi AI (Sally - UX Designer Agent):
```text
System: Xây dựng giao diện React (Vite) với thiết kế HSL hiện đại.
Bao gồm:
- Màn hình Login với nút đăng nhập Nhanh Demo cho 3 vai trò (Nhóm 15).
- Màn hình Bảng Kanban 3 cột (To-Do, In-Progress, Done) có khoá phân quyền cho Thành viên.
- Modal QRCode hiển thị mã QR động cá nhân & Nút "Quét / Tự động điểm danh tức thời".
- AI Hub hỗ trợ 3 tab tương tác AI.
```

### 🤖 Phản hồi của AI:
> Đã phát triển trọn bộ React Frontend tại thư mục `frontend/src/` (Đã biên dịch thành công `dist/` với 0 lỗi).
