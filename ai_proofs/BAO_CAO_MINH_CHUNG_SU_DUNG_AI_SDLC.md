# BÁO CÁO MINH CHỨNG SỬ DỤNG AI TRONG QUY TRÌNH SDLC
**Đề tài 28: Hệ thống Quản lý Câu lạc bộ Sinh viên Tích hợp AI**  
**Nhóm 15: La Văn Quyền (Trưởng nhóm) & Nguyễn Đức Anh (Thành viên)**

---

## 📌 1. TỔNG QUAN PHƯƠNG PHÁP MINH CHỨC SỬ DỤNG AI

Đề tài 28 yêu cầu **"Sử dụng AI trong toàn bộ quy trình phát triển phần mềm (SDLC) và lưu minh chứng sử dụng AI"**. Nhóm 15 thực hiện minh chứng theo 2 hình thức:

1. **Minh chứng Quy trình SDLC (Development Time)**: Lưu trữ các câu lệnh Prompting, Nhật ký trao đổi với AI Agents (BMAD Method) qua từng giai đoạn KT1, KT2, KT3, Cuối kỳ trong thư mục [`ai_proofs/`](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/ai_proofs).
2. **Minh chứng Vận hành Hệ thống (Runtime AI Logs)**: Lưu trữ toàn bộ lịch sử Prompt & Kết quả do AI sinh ra khi người dùng gọi các tính năng AI trong CSDL bảng `ai_logs`.

---

## 🚀 2. MINH CHỨNG SỬ DỤNG AI THEO TỪNG GIAI ĐOẠN SDLC

### 🔹 Giai đoạn 1 (KT1): AI trong Khảo sát & Thiết kế Yêu cầu (Requirements & Design)
- **Công cụ / Agent sử dụng**: BMAD BA Agent (Mary) & System Architect Agent (Winston).
- **Nhiệm vụ AI thực hiện**: 
  - Phân tích đề bài 28, phân tích điểm đau (Pain points) của Ban Chủ nhiệm CLB.
  - Gợi ý ma trận Use Cases và thiết kế Sơ đồ CSDL ERD 7 bảng chuẩn 3NF.
- **Minh chứng cụ thể**:
  - File Prompt & Phân tích Use Case: [`ai_proofs/KT1_Requirements_Design_Prompts.md`](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/ai_proofs/KT1_Requirements_Design_Prompts.md)
  - File Báo cáo SRS & ERD đã tạo: [`03_requirements-specification.docx`](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/docs/03_GenAI_SoftwareDevelopment_requirements-specification.docx), [`06_screenflow_db.docx`](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/docs/06_GenAI_SoftwareDevelopment_screenflow_db.docx).

### 🔹 Giai đoạn 2 (KT2): AI trong Lập trình & Sinh Mã nguồn (Code Generation)
- **Công cụ / Agent sử dụng**: BMAD Senior Dev Agent (Amelia).
- **Nhiệm vụ AI thực hiện**:
  - Sinh mã nguồn Backend Flask RESTful API cho Auth, Members, Activities, Tasks.
  - Sinh cấu trúc CSDL SQLAlchemy Models & Pydantic Schemas.
  - Sinh giao diện React UI (Vite + Tailwind/CSS) với bảng Kanban Board & QRCode Modal.
- **Minh chứng cụ thể**:
  - File Nhật ký Prompt sinh code: [`ai_proofs/KT2_Code_Generation_Prompts.md`](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/ai_proofs/KT2_Code_Generation_Prompts.md)
  - Mã nguồn Backend & Frontend trong repository: [`backend/`](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/backend), [`frontend/`](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/frontend).

### 🔹 Giai đoạn 3 (KT3): AI trong Prompt Engineering & Kiểm thử (Testing)
- **Công cụ / Agent sử dụng**: BMAD QA Agent & AI Service Engine (`app/services/ai_service.py`).
- **Nhiệm vụ AI thực hiện**:
  - Thiết kế Prompt mẫu cho 3 chức năng AI (Sinh thông báo, Tóm tắt hoạt động, Gợi ý phân công).
  - Tự động sinh 25 Test Cases kiểm thử chức năng & kiểm thử ngoại lệ AI (Handling missing skills /schedule conflicts).
- **Minh chứng cụ thể**:
  - Bảng CSDL lưu vết runtime: Bảng `ai_logs` trong CSDL `student_club.db`.
  - File Nhật ký Prompt AI Engine: [`ai_proofs/KT3_AI_Prompt_Engineering_Logs.md`](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/ai_proofs/KT3_AI_Prompt_Engineering_Logs.md)
  - File Báo cáo Kiểm thử: [`05_functional-testing.docx`](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/docs/05_GenAI_SoftwareDevelopment_functional-testing.docx).

### 🔹 Giai đoạn 4 (Cuối kỳ): AI trong Lập Tài liệu Báo cáo & Hướng dẫn (Documentation)
- **Nhiệm vụ AI thực hiện**:
  - Tự động sinh và đồng bộ định dạng trọn bộ 8 file báo cáo `.docx` chuẩn mẫu GD&ĐT.
  - Viết tài liệu Hướng dẫn sử dụng (`07_user-guide.docx`).
- **Minh chứng cụ thể**:
  - Trọn bộ 8 file tài liệu trong thư mục [`docs/`](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/docs).

---

## 📊 3. MINH CHỨNG LƯU VẾT VẬN HÀNH AI (RUNTIME AI LOGS SCHEMAS)

Mỗi lần người dùng kích hoạt các chức năng AI trên giao diện web, hệ thống tự động ghi nhật ký vào bảng `ai_logs` với cấu trúc:

| Trường CSDL | Kiểu dữ liệu | Mô tả minh chứng |
| :--- | :--- | :--- |
| `id` | Integer | ID minh chứng duy nhất |
| `user_id` | Integer | ID người dùng thực hiện gọi AI |
| `prompt_type` | String | Loại tính năng AI (`ANNOUNCEMENT`, `SUMMARY`, `RECOMMEND`) |
| `input_data` | Text (JSON) | Dữ liệu đầu vào thô gửi sang AI Engine |
| `output_result` | Text (JSON) | Kết quả văn bản/phân công do AI sinh ra |
| `created_at` | DateTime | Dấu thời gian thực thi chính xác |

---

## 🎯 KẾT LUẬN
Nhóm 15 đã đáp ứng **100% yêu cầu lưu minh chứng sử dụng AI trong SDLC** thông qua cả bộ file nhật ký lưu trữ minh chứng trong dự án và hệ thống tự động lưu vết trong CSDL.
