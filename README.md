# Nhóm 28: Hệ thống Quản lý Câu lạc bộ Sinh viên Tích hợp AI Agent
> **Môn học:** Ứng dụng Trí tuệ Nhân tạo trong Phát triển Phần mềm (AI SDLC)  
> **Nhóm thực hiện:** Nhóm 28 (02 Sinh viên)  
> **Thời gian thực hiện:** Từ 27/07/2026 đến 27/09/2026 (9 tuần)

---

## 👥 1. THÀNH VIÊN NHÓM & PHÂN CÔNG VAI TRÒ

| STT | Họ và Tên | Vai trò chính | Nhiệm vụ phụ trách |
| :---: | :--- | :--- | :--- |
| **1** | **La Văn Quyền** | **Trưởng nhóm / Lead Dev / System Architect** | - Thiết kế Kiến trúc Hệ thống, CSDL PostgreSQL, Docker Compose.<br>- Lập trình Backend Flask + Pydantic V2 + JWT Authentication.<br>- Tích hợp Dual-Engine AI (Google Gemini / OpenAI + Local Rule Fallback). |
| **2** | **Nguyễn Đức Anh** | **Thành viên / BA / UX Designer / QA Tester** | - Thu thập yêu cầu, viết tài liệu Q&A, SRS, Báo cáo Khảo sát (KT1).<br>- Thiết kế UI/UX Screen Flow, lập trình giao diện React-Vite.<br>- Xây dựng kịch bản kiểm thử chức năng & Edge cases cho AI Engine. |

---

## 📚 2. TRỌN BỘ TÀI LIỆU DỰ ÁN (PROJECT DOCUMENTATION)

Toàn bộ tài liệu chính thức theo chuẩn đề cương môn học được lưu trữ tại thư mục [`docs/`](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/docs):

| STT | Mã Tài liệu | Tên Tài liệu Báo cáo | Định dạng | Trạng thái |
| :---: | :--- | :--- | :---: | :---: |
| **01** | `01_project-plan` | [Kế hoạch Thực hiện Dự án (Project Plan - WBS 9 tuần)](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/docs/01_GenAI_SoftwareDevelopment_project-plan.docx) | `.docx` | ✅ Hoàn thiện |
| **02** | `02_requirements-qa` | [Bảng Câu hỏi & Giải đáp Yêu cầu Nghiệp vụ (Requirements Q&A)](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/docs/02_GenAI_SoftwareDevelopment_requirements-qa.docx) | `.docx` | ✅ Hoàn thiện |
| **03** | `03_requirements-spec` | [Đặc tả Yêu cầu Phần mềm (SRS - Software Requirements Specification)](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/docs/03_GenAI_SoftwareDevelopment_requirements-specification.docx) | `.docx` | ✅ Hoàn thiện |
| **04** | `04_object-oriented-design` | [Thiết kế Hướng đối tượng & Mô hình lớp (OOD Class Diagram)](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/docs/04_GenAI_SoftwareDevelopment_object-oriented-design.docx) | `.docx` | ✅ Hoàn thiện |
| **05** | `05_functional-testing` | [Kế hoạch & Kịch bản Kiểm thử Chức năng (Functional Testing)](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/docs/05_GenAI_SoftwareDevelopment_functional-testing.docx) | `.docx` | ✅ Hoàn thiện (25/25 Pass) |
| **06** | `06_screenflow_db` | [Thiết kế Luồng Màn hình (Screen Flow) & Sơ đồ CSDL (ERD)](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/docs/06_GenAI_SoftwareDevelopment_screenflow_db.docx) | `.docx` | ✅ Hoàn thiện |
| **07** | `07_user-guide` | [Hướng dẫn Sử dụng & Vận hành Hệ thống (User Guide)](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/docs/07_GenAI_SoftwareDevelopment_user-guide.docx) | `.docx` | ✅ Hoàn thiện |
| **08** | `08_survey_req_analysis` | [Báo cáo Khảo sát & Phân tích Yêu cầu Chức năng / Phi chức năng (KT1 Scope)](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/docs/08_KhaoSat_PhanTich_YeuCau_ChucNang_PhiChucNang.docx) | `.docx` & [`.md`](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/docs/08_KhaoSat_PhanTich_YeuCau_ChucNang_PhiChucNang.md) | ✅ Hoàn thiện |

---

## 🤖 3. MINH CHỨNG ỨNG DỤNG AI TRONG SDLC (AI PROOFS)

Thư mục [`ai_proofs/`](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/ai_proofs) lưu trữ đầy đủ minh chứng áp dụng AI xuyên suốt các giai đoạn:
- 📄 [Báo cáo Tổng hợp Minh chứng Sử dụng AI](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/ai_proofs/BAO_CAO_MINH_CHUNG_SU_DUNG_AI_SDLC.md)
- 🔹 **KT1 (Khảo sát & Thiết kế):** [`ai_proofs/KT1_Requirements_Design_Prompts.md`](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/ai_proofs/KT1_Requirements_Design_Prompts.md)
- 🔹 **KT2 (Lập trình & Sinh code):** [`ai_proofs/KT2_Code_Generation_Prompts.md`](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/ai_proofs/KT2_Code_Generation_Prompts.md)
- 🔹 **KT3 (Prompt Engineering & Test):** [`ai_proofs/KT3_AI_Prompt_Engineering_Logs.md`](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/ai_proofs/KT3_AI_Prompt_Engineering_Logs.md)

---

## 🛠️ 4. KIẾN TRÚC CÔNG NGHỆ & TÍNH NĂNG

### Công nghệ sử dụng:
- **Backend:** Flask (Python 3.11+) + SQLAlchemy ORM + Pydantic V2 + JWT Authentication + Bcrypt.
- **Frontend:** React + Vite + Vanilla CSS Component System.
- **Database:** PostgreSQL 16 (chuẩn hóa quan hệ 7 bảng).
- **Deployment:** Docker & Docker Compose orchestrate 3 containers (`postgres_db`, `flask_backend`, `react_frontend`).
- **AI Dual-Engine:** Google Gemini API / OpenAI API kết hợp Local Rule-based Fallback Engine chạy offline.

### 6 Chức năng Nghiệp vụ (FR-SYS) + 3 Chức năng AI (FR-AI):
1. **FR-SYS-01:** Đăng nhập, Xác thực JWT & Phân quyền RBAC 3 vai trò (Admin / Leader / Member).
2. **FR-SYS-02:** Quản lý Hồ sơ, Ma trận Kỹ năng (Skill Matrix) & Lịch rảnh (Free Slots).
3. **FR-SYS-03:** Quản lý Ban Chuyên môn & Điều chuyển Nhân sự.
4. **FR-SYS-04:** Quản lý Sự kiện & Điểm danh Mã QR Code độc bản.
5. **FR-SYS-05:** Quản lý Nhiệm vụ qua Kanban Board (To-Do / In-Progress / Done) siết chặt quyền hạn.
6. **FR-SYS-06:** Thống kê Hoạt động & Bảng xếp hạng Đóng góp (Leaderboard).
7. **FR-AI-01:** AI Sinh bài đăng Thông báo Sự kiện đa phong cách kèm emoji.
8. **FR-AI-02:** AI Tóm tắt Kết quả Hoạt động & Phản hồi cuộc họp (3 phần: Ưu điểm, Tồn tại, Đề xuất).
9. **FR-AI-03:** AI Gợi ý Phân công Nhiệm vụ Thông minh (Matchmaking % + Lý do).

---

## 🚀 5. HƯỚNG DẪN KHỞI CHẠY HỆ THỐNG

### Cách 1: Chạy bằng Docker Compose (Khuyến nghị)
```bash
# Khởi động toàn bộ 3 services (PostgreSQL, Backend, Frontend)
docker-compose up --build -d

# Truy cập ứng dụng:
# Frontend: http://localhost:5173 (hoặc http://localhost:80)
# Backend API: http://localhost:8000
```

### Cách 2: Chạy Thủ công từng Service (Development)

**Backend:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python seed_data.py        # Khởi tạo DB & dữ liệu mẫu
python run.py              # Chạy server tại http://localhost:8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev                # Chạy dev server tại http://localhost:5173
```

---

## 🔑 6. TÀI KHOẢN TRẢI NGHIỆM HỆ THỐNG (DEMO ACCOUNTS)

| Vai trò | Email đăng nhập | Mật khẩu | Phân quyền truy cập |
| :--- | :--- | :--- | :--- |
| **Ban Chủ nhiệm (Admin)** | `admin@club.edu.vn` | `admin123` | Toàn quyền quản trị hệ thống, quản lý ban, phân quyền thành viên |
| **Trưởng ban (Leader)** | `leader@club.edu.vn` | `leader123` | Tạo sự kiện, tạo task, điểm danh QR, sử dụng 3 công cụ AI Hub |
| **Thành viên (Member)** | `member@club.edu.vn` | `member123` | Cập nhật Skill/Free Slots, quét QR điểm danh, cập nhật task của mình |
