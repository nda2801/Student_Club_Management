# HỆ THỐNG CÁC GIAI ĐOẠN THỰC HIỆN DỰ ÁN (PROJECT SDLC MILESTONES)
## ĐỀ TÀI 28: HỆ THỐNG QUẢN LÝ CÂU LẠC BỘ SINH VIÊN CÓ TÍCH HỢP AI

---

**Thông tin Dự án:**
- **Đề tài số:** 28 (Quản lý CLB Sinh viên tích hợp AI)
- **Lớp / Nhóm:** Nhóm 15 (Nhóm 02 Sinh viên)
- **Thành viên thực hiện:**
  - **La Văn Quyền** (Trưởng nhóm - Lead Developer / System Architect)
  - **Nguyễn Đức Anh** (Thành viên - Business Analyst / UX Designer / QA Tester)
- **Công nghệ Thống nhất:** Flask 3.1+ (Python 3.11/3.13) + Pydantic V2 + JWT Auth + React 18 + Vite + PostgreSQL 16 + Docker Compose + Dual-Engine AI (Google Gemini Cloud API & Local Rule-based Fallback Matcher).
- **Tổng thời gian thực hiện:** 10 Tuần (Từ 27/07/2026 đến 04/10/2026).

---

## 🗺️ TỔNG QUAN 4 GIAI ĐOẠN PHÁT TRIỂN (SDLC ROADMAP)

```
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│                    TIẾN TRÌNH 4 GIAI ĐOẠN THỰC HIỆN DỰ ÁN (ĐỀ TÀI 28 - NHÓM 15)                   │
├───────────────────────┬───────────────────────┬──────────────────────────┬────────────────────────┤
│ GIAI ĐOẠN KT1         │ GIAI ĐOẠN KT2         │ GIAI ĐOẠN KT3            │ GIAI ĐOẠN KT4 / CUỐI KỲ│
│ (Tuần 1 - Tuần 3)     │ (Tuần 4 - Tuần 6)     │ (Tuần 7 - Tuần 8)        │ (Tuần 9 - Tuần 10)     │
├───────────────────────┼───────────────────────┼──────────────────────────┼────────────────────────┤
│ • Khảo sát 6 Điểm đau │ • Cấu hình Docker DB  │ • Tích hợp Google Gemini │ • Hướng dẫn Sử dụng    │
│ • 6 FR-SYS & 3 FR-AI  │ • Flask Auth & JWT    │ • Local Fallback Matcher │ • Slide Thuyết trình 5p│
│ • 14 NFRs ISO 25010   │ • Member & Skill Mat. │ • Prompt Security 5 tầng │ • Video Demo Vận hành  │
│ • 12 Use Cases        │ • Event Dynamic QR    │ • Automated E2E Testing  │ • Báo cáo Nghiệm thu   │
│ • 19 Biểu đồ UML      │ • Kanban Board RBAC   │ • Load Testing 200 VUs   │ • Bàn giao Source Code │
│ • Ma trận RTM KT1     │ • Test Plan KT2       │ • Tối ưu P95 Latency     │ • Bảo vệ Đồ án         │
└───────────────────────┴───────────────────────┴──────────────────────────┴────────────────────────┘
```

---

## 📂 CẤU TRÚC THƯ MỤC CHI TIẾT THEO TỪNG GIAI ĐOẠN

### 📁 1. [Giai đoạn KT1: Khảo sát, Đặc tả Yêu cầu & Thiết kế UML (Tuần 1 - 3)](./GiaiDoan_KT1_KhaoSat_YeuCau_ThietKe_Tuan1_Tuan3/)
- **Mục tiêu:** Khảo sát hiện trạng, phân tích 6 điểm đau, đặc tả 9 yêu cầu chức năng (6 FR-SYS, 3 FR-AI), 14 tiêu chuẩn chất lượng NFR ISO/IEC 25010, phân rã 12 Use Cases, vẽ trọn bộ 19 biểu đồ UML và lập ma trận truy vết RTM.
- **Hồ sơ tài liệu chính:**
  - [`01_GenAI_SoftwareDevelopment_project-plan.docx`](./GiaiDoan_KT1_KhaoSat_YeuCau_ThietKe_Tuan1_Tuan3/01_GenAI_SoftwareDevelopment_project-plan.docx) — Kế hoạch thực hiện dự án 10 tuần.
  - [`02_GenAI_SoftwareDevelopment_requirements-qa.docx`](./GiaiDoan_KT1_KhaoSat_YeuCau_ThietKe_Tuan1_Tuan3/02_GenAI_SoftwareDevelopment_requirements-qa.docx) — Biên bản phỏng vấn, khảo sát & phân tích điểm đau.
  - [`03_GenAI_SoftwareDevelopment_requirements-specification.docx`](./GiaiDoan_KT1_KhaoSat_YeuCau_ThietKe_Tuan1_Tuan3/03_GenAI_SoftwareDevelopment_requirements-specification.docx) — Đặc tả yêu cầu phần mềm (SRS).
  - [`04_GenAI_SoftwareDevelopment_object-oriented-design.docx`](./GiaiDoan_KT1_KhaoSat_YeuCau_ThietKe_Tuan1_Tuan3/04_GenAI_SoftwareDevelopment_object-oriented-design.docx) — Thiết kế hướng đối tượng (OOD) & Class Diagram.
  - [`08_KhaoSat_PhanTich_YeuCau_ChucNang_PhiChucNang.docx`](./GiaiDoan_KT1_KhaoSat_YeuCau_ThietKe_Tuan1_Tuan3/08_KhaoSat_PhanTich_YeuCau_ChucNang_PhiChucNang.docx) — Báo cáo tổng hợp toàn diện KT1 (1.15 MB kèm ảnh biểu đồ đầy đủ).
  - [`08_KhaoSat_PhanTich_YeuCau_ChucNang_PhiChucNang.md`](./GiaiDoan_KT1_KhaoSat_YeuCau_ThietKe_Tuan1_Tuan3/08_KhaoSat_PhanTich_YeuCau_ChucNang_PhiChucNang.md) — File Markdown gốc.
  - [`plantuml/`](./GiaiDoan_KT1_KhaoSat_YeuCau_ThietKe_Tuan1_Tuan3/plantuml/) — Thư mục chứa trọn bộ 19 file mã nguồn PlantUML sạch.

---

### 📁 2. [Giai đoạn KT2: Phát triển Hệ thống Cốt lõi & Docker Container (Tuần 4 - 6)](./GiaiDoan_KT2_PhatTrien_Core_Backend_Frontend_Docker_Tuan4_Tuan6/)
- **Mục tiêu:** Xây dựng hệ thống Backend Flask RESTful API, Frontend React-Vite SPA, khởi tạo CSDL PostgreSQL 16 và container hóa qua Docker Compose.
- **Hồ sơ tài liệu chính:**
  - [`05_GenAI_SoftwareDevelopment_functional-testing.docx`](./GiaiDoan_KT2_PhatTrien_Core_Backend_Frontend_Docker_Tuan4_Tuan6/05_GenAI_SoftwareDevelopment_functional-testing.docx) — Kế hoạch kiểm thử chức năng & Danh mục Test Cases (25+ test cases).
  - [`06_GenAI_SoftwareDevelopment_screenflow_db.docx`](./GiaiDoan_KT2_PhatTrien_Core_Backend_Frontend_Docker_Tuan4_Tuan6/06_GenAI_SoftwareDevelopment_screenflow_db.docx) — Thiết kế luồng màn hình UI/UX & Cấu trúc CSDL PostgreSQL.
- **Các mô-đun phát triển:**
  - **Tuần 4:** Docker Compose (3 container: frontend, backend, db) + Flask Auth API + Mã hóa Bcrypt + JWT Middleware + CSDL PostgreSQL Models (`users`, `departments`).
  - **Tuần 5:** API Quản lý Thành viên, Skill Matrix, Lịch rảnh (Free Slots) + API Tạo sự kiện & Sinh mã Dynamic QR Code độc bản + API Quét QR Check-in.
  - **Tuần 6:** Bảng nhiệm vụ Kanban Board kéo thả trên React 18 + Kiểm soát RBAC sửa Task (chặn 403 Forbidden) + Tính điểm Contribution Score & Leaderboard.

---

### 📁 3. [Giai đoạn KT3: Tích hợp Trí tuệ Nhân tạo & Kiểm thử Toàn diện (Tuần 7 - 8)](./GiaiDoan_KT3_TichHop_AI_DualEngine_KiemThu_Tuan7_Tuan8/)
- **Mục tiêu:** Hiện thực hóa kiến trúc AI Dual-Engine, kết nối Cloud LLM API và xây dựng Local Rule-based Fallback Engine, kiểm thử tải và bảo mật Prompt Injection.
- **Nội dung thực hiện:**
  - **FR-AI-01:** AI Sinh bài đăng thông báo sự kiện đa phong cách (Hào hứng, Trang trọng, Thân thiện) kèm emoji.
  - **FR-AI-02:** AI Tóm tắt kết quả hoạt động và phản hồi cuộc họp 3 phần (Ưu điểm, Tồn tại, Đề xuất).
  - **FR-AI-03:** AI Smart Matchmaking phân công nhiệm vụ dựa trên độ tương đồng Skill Matrix + Free Slots + Cân bằng tải.
  - **Dual-Engine Fallback:** Cơ chế chịu lỗi tự động chuyển sang Heuristic Rule Matcher cục bộ trong < 100ms khi mất mạng hoặc hết quota.
  - **Kiểm thử hiệu năng:** Load testing 200 concurrent users với Locust, đo đạc P95 latency $\le$ 500ms.

---

### 📁 4. [Giai đoạn KT4 / Cuối kỳ: Đóng gói, Hướng dẫn & Nghiệm thu Tổng kết (Tuần 9 - 10)](./GiaiDoan_KT4_DongGoi_BaoCao_NghiemThu_Tuan9_Tuan10/)
- **Mục tiêu:** Hoàn thiện tài liệu hướng dẫn sử dụng, xây dựng slide thuyết trình, quay video demo và bảo vệ đồ án trước Hội đồng.
- **Hồ sơ tài liệu chính:**
  - [`07_GenAI_SoftwareDevelopment_user-guide.docx`](./GiaiDoan_KT4_DongGoi_BaoCao_NghiemThu_Tuan9_Tuan10/07_GenAI_SoftwareDevelopment_user-guide.docx) — Tài liệu Hướng dẫn sử dụng chi tiết cho 3 vai trò (Admin, Leader, Member).
  - Kịch bản thuyết trình 5 phút & Bộ câu hỏi phản biện bảo vệ đồ án.
  - Video demo quy trình vận hành toàn diện trên Docker.
  - Bàn giao mã nguồn hoàn chỉnh trên Git Repository.

---

## 🎯 BẢNG ĐỐI SOÁT TÀI LIỆU TOÀN DIỆN (DOCUMENT MASTER INDEX)

| Mã Tài liệu | Tên Tài liệu Kỹ thuật | Giai đoạn Phụ trách | Tình trạng |
| :---: | :--- | :---: | :---: |
| **DOC-01** | Kế hoạch Thực hiện Dự án (Project Plan) | KT1 (Tuần 1 - 3) | **HOÀN THÀNH 100%** |
| **DOC-02** | Báo cáo Khảo sát Hiện trạng & QA Phỏng vấn | KT1 (Tuần 1 - 3) | **HOÀN THÀNH 100%** |
| **DOC-03** | Đặc tả Yêu cầu Phần mềm (SRS) | KT1 (Tuần 1 - 3) | **HOÀN THÀNH 100%** |
| **DOC-04** | Thiết kế Hướng đối tượng & UML Models (OOD) | KT1 (Tuần 1 - 3) | **HOÀN THÀNH 100%** |
| **DOC-05** | Kế hoạch Kiểm thử Chức năng (Test Plan & Cases) | KT2 (Tuần 4 - 6) | **HOÀN THÀNH 100%** |
| **DOC-06** | Thiết kế Luồng Màn hình & CSDL PostgreSQL | KT2 (Tuần 4 - 6) | **HOÀN THÀNH 100%** |
| **DOC-07** | Tài liệu Hướng dẫn Sử dụng Hệ thống (User Guide) | KT4 (Tuần 9 - 10) | **HOÀN THÀNH 100%** |
| **DOC-08** | Báo cáo Tổng hợp Khảo sát & Phân tích KT1 | KT1 (Tuần 1 - 3) | **HOÀN THÀNH 100% (1.15 MB)** |
