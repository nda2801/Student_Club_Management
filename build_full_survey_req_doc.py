# -*- coding: utf-8 -*-
"""
Script to generate the Complete Survey & Requirements Analysis Document (Doc 08)
specifically tailored for the KT1 milestone (End of Week 3 of the Project Plan).
Outputs both Markdown (.md) and Word Document (.docx) with embedded Table of Contents (Mục lục)
and full embedded PlantUML code blocks loaded directly from verified docs/plantuml/ files.
"""

import os
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

docs_dir = r"D:\DTC245200328\Nam3\Ki1\UngDungAI\Student_Club_Management\docs"
plantuml_dir = os.path.join(docs_dir, "plantuml")

def load_puml(filename):
    """Loads clean, verified PlantUML code from docs/plantuml directory."""
    path = os.path.join(plantuml_dir, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return ""

# Read all diagrams
puml_painpoint = load_puml("painpoint_to_solution.puml")
puml_ai_flow = load_puml("ai_functional_flow.puml")
puml_uc_overall = load_puml("usecase_overall.puml")
puml_uc_sub1 = load_puml("usecase_sub1_auth.puml")
puml_uc_sub2 = load_puml("usecase_sub2_member.puml")
puml_uc_sub3 = load_puml("usecase_sub3_event.puml")
puml_uc_sub4 = load_puml("usecase_sub4_task.puml")
puml_uc_sub5 = load_puml("usecase_sub5_ai.puml")
puml_class = load_puml("class_diagram.puml")
puml_act_auth = load_puml("activity_auth_login.puml")
puml_act_qr = load_puml("activity_qr_attendance.puml")
puml_act_ai = load_puml("activity_ai_matching.puml")
puml_seq_auth = load_puml("sequence_auth_login.puml")
puml_seq_qr = load_puml("sequence_qr_checkin.puml")
puml_seq_ai = load_puml("sequence_ai_matchmaking.puml")
puml_seq_kanban = load_puml("sequence_kanban_rbac.puml")
puml_state_task = load_puml("state_task_lifecycle.puml")
puml_state_act = load_puml("state_activity_lifecycle.puml")
puml_deploy = load_puml("deployment_docker.puml")

# -------------------------------------------------------------
# 1. MARKDOWN CONTENT (EMBEDDED BOTH MERMAID & PLANTUML)
# -------------------------------------------------------------
md_template = """# BÁO CÁO KHẢO SÁT VÀ PHÂN TÍCH YÊU CẦU PHẦN MỀM
## (GIAI ĐOẠN KT1: TỪ TUẦN 1 ĐẾN HẾT TUẦN 3 THEO KẾ HOẠCH DỰ ÁN)
### YÊU CẦU CHỨC NĂNG, YÊU CẦU PHI CHỨC NĂNG, MÔ HÌNH USE CASE VÀ MÔ HÌNH HÓA UML

---

**Đề tài 28:** Hệ thống quản lý câu lạc bộ sinh viên có tích hợp AI  
**Lớp / Nhóm thực hiện:** Nhóm 15 - Nhóm 02 Sinh viên  
**Thành viên nhóm:**  
- **La Văn Quyền** (Trưởng nhóm - Lead Developer / System Architect)  
- **Nguyễn Đức Anh** (Thành viên - Business Analyst / UX Designer / QA Tester)  
**Phạm vi mốc thời gian báo cáo:** Giai đoạn KT1 (Từ 27/07/2026 đến 16/08/2026 - Hết Tuần 3)  
**Mục đích tài liệu:** Tổng kết kết quả khảo sát hiện trạng, phân tích chi tiết 02 nhóm yêu cầu (Chức năng & Phi chức năng), thiết kế hoàn chỉnh hệ thống biểu đồ Use Case (Tổng thể & Phân hệ), xây dựng trọn bộ biểu đồ UML (Class, Activity, Sequence, State Machine, Component & Deployment Diagrams) chèn trực tiếp mã nguồn biểu đồ (**Mermaid** & **PlantUML**) và xác lập ma trận truy vết yêu cầu (RTM) làm căn cứ triển khai mã nguồn giai đoạn KT2.

**Kiến trúc Công nghệ Thống nhất:**
- **Backend:** Flask (Python 3.11+) + Pydantic V2 + JWT Authentication + Gunicorn WSGI.
- **Frontend:** React + Vite + CSS Responsive Component System.
- **Cơ sở dữ liệu:** PostgreSQL 16 (chuẩn hóa quan hệ qua SQLAlchemy ORM).
- **Containerization:** Docker & Docker Compose (Orchestration 3 services: PostgreSQL DB, Flask Backend, React Frontend).
- **AI Engine:** Dual-Engine Architecture (Cloud LLM: Google Gemini API / OpenAI API kết hợp Local Rule-based Fallback Engine).

---

## MỤC LỤC TỔNG QUAN

1. [CHƯƠNG 1: TỔNG QUAN KHẢO SÁT HIỆN TRẠNG (TUẦN 1)](#chương-1-tổng-quan-khảo-sát-hiện-trạng-tuần-1)
   - 1.1 Mục tiêu và Phương pháp khảo sát quy trình quản lý CLB
   - 1.2 Phân loại Tác nhân Người dùng & Tác nhân Hệ thống (Actors)
   - 1.3 Thống kê Kết quả Khảo sát & Phân tích 06 Điểm đau (Pain Points)
   - 1.4 Ma trận Nhu cầu Người dùng và Đề xuất Giải pháp Tích hợp AI (Kèm Code Mermaid & PlantUML)
2. [CHƯƠNG 2: PHÂN TÍCH YÊU CẦU CHỨC NĂNG (FUNCTIONAL REQUIREMENTS - TUẦN 2)](#chương-2-phân-tích-yêu-cầu-chức-năng-functional-requirements---tuần-2)
   - 2.1 Nhóm Yêu cầu Chức năng Nghiệp vụ Quản lý Hệ thống (FR-SYS)
   - 2.2 Nhóm Yêu cầu Chức năng Trí tuệ Nhân tạo (FR-AI) (Kèm Code Mermaid & PlantUML)
3. [CHƯƠNG 3: PHÂN TÍCH YÊU CẦU PHI CHỨC NĂNG & TIÊU CHÍ NGHIỆM THU (NON-FUNCTIONAL REQUIREMENTS - TUẦN 2)](#chương-3-phân-tích-yêu-cầu-phi-chức-năng--tiêu-chí-nghiệm-thu-non-functional-requirements---tuần-2)
   - 3.1 Bảng Đặc tả Tiêu chuẩn Chất lượng ISO/IEC 25010 kèm Acceptance Criteria & Test Method
   - 3.2 Đặc tả Cơ chế Bảo mật AI & Phòng chống Prompt Injection Đa tầng
4. [CHƯƠNG 4: MÔ HÌNH HÓA CA SỬ DỤNG (USE CASE MODELING - TUẦN 3)](#chương-4-mô-hình-hóa-ca-sử-dụng-use-case-modeling---tuần-3)
   - 4.1 Danh mục Phân rã 12 Use Cases Cốt lõi
   - 4.2 Biểu đồ Use Case Tổng thể Toàn Hệ thống (Kèm Mã Mermaid & PlantUML)
   - 4.3 Biểu đồ Use Case Chi tiết theo từng Phân hệ (Kèm Mã Mermaid & PlantUML)
     - 4.3.1 Phân hệ 1: Xác thực & Phân quyền Hệ thống (Kèm Code Mermaid & PlantUML)
     - 4.3.2 Phân hệ 2: Quản lý Hồ sơ Thành viên & Ban Chuyên môn (Kèm Code Mermaid & PlantUML)
     - 4.3.3 Phân hệ 3: Quản lý Sự kiện & Điểm danh QR Độc bản (Kèm Code Mermaid & PlantUML)
     - 4.3.4 Phân hệ 4: Quản lý Nhiệm vụ & Bảng Kanban (Kèm Code Mermaid & PlantUML)
     - 4.3.5 Phân hệ 5: Trợ lý Trí tuệ Nhân tạo & Báo cáo Thống kê (Kèm Code Mermaid & PlantUML)
   - 4.4 Bảng Đặc tả Ca Sử dụng Mẫu Chi tiết (Use Case Specifications: UC04, UC05/UC10, UC06)
   - 4.5 Ma trận Phân loại Mức độ Ưu tiên theo Phương pháp MoSCoW
5. [CHƯƠNG 5: MÔ HÌNH HÓA VÀ THIẾT KẾ HỆ THỐNG BẰNG CÁC BIỂU ĐỒ UML (UML MODELING & SYSTEM DESIGN - TUẦN 3)](#chương-5-mô-hình-hóa-và-thiết-kế-hệ-thống-bằng-các-biểu-đồ-uml-uml-modeling--system-design---tuần-3)
   - 5.1 Biểu đồ Lớp Phân tích & Thực thể (UML Class Diagram - Kèm Mã Mermaid & PlantUML)
   - 5.2 Biểu đồ Hoạt động (UML Activity Diagrams - Kèm Mã Mermaid & PlantUML)
     - 5.2.1 Activity Diagram: Đăng nhập, Xác thực JWT & Phân quyền RBAC (Kèm Code)
     - 5.2.2 Activity Diagram: Tổ chức Hoạt động & Điểm danh Tự động bằng Mã QR Độc bản (Kèm Code)
     - 5.2.3 Activity Diagram: AI Gợi ý Phân công Nhiệm vụ với Dual-Engine Fallback (Kèm Code)
   - 5.3 Biểu đồ Tuần tự (UML Sequence Diagrams - Kèm Mã Mermaid & PlantUML)
     - 5.3.1 Sequence Diagram: Xác thực Đăng nhập & Cấp JWT Token (Kèm Code)
     - 5.3.2 Sequence Diagram: Quét Mã QR Điểm danh Sự kiện Realtime (Kèm Code)
     - 5.3.3 Sequence Diagram: AI Gợi ý Phân công Nhiệm vụ với Cơ chế Dual-Engine Fallback (Kèm Code)
     - 5.3.4 Sequence Diagram: Cập nhật Trạng thái Task trên Kanban Board với Kiểm soát RBAC (Kèm Code)
   - 5.4 Biểu đồ Máy Trạng thái (UML State Machine Diagrams - Kèm Mã Mermaid & PlantUML)
     - 5.4.1 State Machine Diagram: Vòng đời Trạng thái Nhiệm vụ (Task Lifecycle - Kèm Code)
     - 5.4.2 State Machine Diagram: Vòng đời Trạng thái Hoạt động / Sự kiện (Activity Lifecycle - Kèm Code)
   - 5.5 Biểu đồ Thành phần & Triển khai (UML Component & Deployment Diagram - Kèm Mã Mermaid & PlantUML)
6. [CHƯƠNG 6: MA TRẬN TRUY VẾT YÊU CẦU (RTM) & KẾ HOẠCH BÀN GIAO GIAI ĐOẠN KT2 (TUẦN 3)](#chương-6-ma-trận-truy-vết-yêu-cầu-rtm--kế-hoạch-bàn-giao-giai-đoạn-kt2-tuần-3)
7. [KẾT LUẬN GIAI ĐOẠN KT1 (HẾT TUẦN 3)](#kết-luận-giai-đoạn-kt1-hết-tuần-3)

---

## CHƯƠNG 1: TỔNG QUAN KHẢO SÁT HIỆN TRẠNG (TUẦN 1)

### 1.1 Mục tiêu và Phương pháp khảo sát quy trình quản lý CLB
Trong khuôn khổ **Tuần 1** của Kế hoạch thực hiện dự án, đội ngũ BA đã tiến hành khảo sát thực trạng vận hành của các Câu lạc bộ sinh viên nhằm làm rõ yêu cầu nghiệp vụ và xác định điểm nghẽn quy trình:
1. **Phỏng vấn sâu (Deep Interview):** Phỏng vấn trực tiếp 06 đại diện Ban Chủ nhiệm (Chủ nhiệm, Phó Chủ nhiệm) và 08 Trưởng ban chuyên môn của các CLB sinh viên tiêu biểu để thu thập quy trình vận hành và khó khăn thực tế.
2. **Khảo sát qua biểu mẫu câu hỏi:** Thu thập ý kiến từ 120 sinh viên thuộc 4 Ban chuyên môn (*Truyền thông*, *Sự kiện*, *Chuyên môn*, *Đối ngoại*) về trải nghiệm tham gia hoạt động, nhận nhiệm vụ và điểm danh.
3. **Quan sát trực tiếp quy trình (Direct Observation):** Ghi nhận thực tế quy trình họp tuần, cách thức phân chia nhiệm vụ sự kiện và phương pháp ký tên điểm danh truyền thống.

### 1.2 Phân loại Tác nhân Người dùng & Tác nhân Hệ thống (Actors)

#### 1.2.1 Chân dung Người dùng (User Personas)

| Tác nhân (Actor) | Vai trò trong CLB | Mục tiêu cốt lõi | Khó khăn / Điểm đau chính |
| :--- | :--- | :--- | :--- |
| **Ban Chủ nhiệm (Admin)** | Lãnh đạo cao nhất của CLB | - Nắm bắt bức tranh tổng thể hoạt động CLB.<br>- Quản lý cơ cấu ban, phân quyền thành viên.<br>- Đánh giá chính xác mức độ đóng góp để khen thưởng. | - Dữ liệu phân tán trên nhiều file Excel, Google Sheet rời rạc.<br>- Không có số liệu đo lường cụ thể về độ tích cực của từng thành viên.<br>- Báo cáo tổng kết cuối kỳ mất nhiều ngày tổng hợp. |
| **Trưởng ban (Leader)** | Quản lý ban chuyên môn, điều phối sự kiện | - Phân công nhiệm vụ nhanh chóng, đúng người đúng việc.<br>- Điểm danh thành viên tham gia sự kiện nhanh gọn.<br>- Soạn bài đăng truyền thông thu hút sinh viên. | - Mất 2-3 giờ/sự kiện để nhắn tin hỏi lịch rảnh và kỹ năng của từng người.<br>- Điểm danh giấy tốn thời gian, dễ sót hoặc nhầm lẫn.<br>- Soạn bài truyền thông cạn ý tưởng, văn phong đơn điệu. |
| **Thành viên (Member)** | Thực hiện nhiệm vụ, tham gia hoạt động | - Nắm rõ nhiệm vụ được giao và thời hạn hoàn thành.<br>- Đăng ký kỹ năng sở trường và lịch rảnh để được giao việc phù hợp.<br>- Điểm danh dễ dàng qua điện thoại. | - Bị giao việc trùng lịch học hoặc không đúng sở trường.<br>- Bỏ sót nhiệm vụ do thông báo bị trôi trên nhóm chat.<br>- Không thấy được điểm số đóng góp của bản thân. |

#### 1.2.2 Tác nhân Hệ thống & Dịch vụ Bên ngoài (System Actors & External Services)

| Tác nhân Kỹ thuật | Loại tác nhân | Vai trò & Trách nhiệm Kỹ thuật | Cơ chế Tương tác / Giao thức |
| :--- | :--- | :--- | :--- |
| **Google Gemini / OpenAI API** | External Cloud AI Service | - Xử lý ngôn ngữ tự nhiên (NLP) phục vụ sinh bài đăng truyền thông, tóm tắt báo cáo và phân tích tương đồng kỹ năng. | Giao thức RESTful HTTPS API (JSON Payload), xác thực qua API Key và biến môi trường `.env`. |
| **Local Rule-based Fallback Engine** | Internal Subsystem | - Cung cấp cơ chế dự phòng cục bộ dựa trên tập luật (Rule-based) và thuật toán heuristic khi mất mạng Internet hoặc lỗi quota API bên ngoài. | Xử lý nội bộ tại tầng Service (In-Memory Rule Matching Engine). |
| **Database Subsystem (PostgreSQL)** | Internal Data Layer | - Lưu trữ và đảm bảo tính toàn vẹn dữ liệu quan hệ người dùng, ban, sự kiện, điểm danh, nhiệm vụ và nhật ký AI. | PostgreSQL 16 chạy trong Docker Container qua SQLAlchemy ORM. |

### 1.3 Thống kê Kết quả Khảo sát & Phân tích 06 Điểm đau (Pain Points)

| STT | Vấn đề / Điểm đau (Pain Point) | Tỷ lệ ghi nhận | Mức độ ảnh hưởng | Giải pháp yêu cầu hệ thống |
| :---: | :--- | :---: | :---: | :--- |
| **01** | **Phân công nhiệm vụ thủ công, thiếu thông tin kỹ năng & lịch rảnh:** Trưởng ban phân công cảm tính, thành viên thường từ chối vì trùng lịch học hoặc không đúng năng lực. | **92%** Trưởng ban | **Rất cao** *(Lãng phí 2-3h/sự kiện)* | Xây dựng Hồ sơ Ma trận Kỹ năng (Skill Matrix) + Lịch rảnh cá nhân (Free Slots) kết hợp **Tính năng AI Gợi ý phân công tự động** (FR-AI-03). |
| **02** | **Điểm danh thủ công bằng giấy / Google Form chậm chạp:** Đầu mỗi sự kiện thường ùn tắc hàng dài chờ ký tên, dễ xảy ra tình trạng điểm danh hộ hoặc thất lạc danh sách. | **78%** Sự kiện | **Cao** *(Mất 15-20 phút đầu buổi)* | Tính năng **Tạo mã QR Code độc bản cho sự kiện** và cho phép thành viên quét QR trên điện thoại để điểm danh tức thì (FR-SYS-04). |
| **03** | **Theo dõi tiến độ phân tán qua Zalo/Messenger:** Nhiệm vụ bị trôi tin nhắn, ban chủ nhiệm không nắm được task nào đang làm, task nào chậm deadline. | **85%** Ban Chủ nhiệm | **Rất cao** *(Đánh giá cảm tính, trễ hạn)* | Tích hợp **Bảng Kanban Board trực quan** (To-Do, In-Progress, Done) có siết chặt phân quyền RBAC và đo lường thời gian (FR-SYS-05). |
| **04** | **Soạn thảo bài đăng truyền thông tốn thời gian, văn phong nghèo nàn:** Ban Truyền thông mất nhiều thời gian nghĩ caption, chưa thu hút được đông đảo sinh viên. | **88%** Ban Truyền thông | **Trung bình** | Tính năng **AI Sinh bài viết thông báo sự kiện** hỗ trợ nhiều Tone giọng (Hào hứng, Trang trọng, Thân thiện...) và tự động thêm emoji (FR-AI-01). |
| **05** | **Tổng hợp báo cáo và tóm tắt phản hồi sau sự kiện rời rạc:** Biên bản họp dài dòng, các phản hồi góp ý của thành viên không được đúc kết thành bài học kinh nghiệm. | **80%** Trưởng ban | **Trung bình** | Tính năng **AI Tóm tắt kết quả hoạt động** tự động trích xuất ưu/nhược điểm và hành động cải tiến từ ghi chú (FR-AI-02). |
| **06** | **Thiếu cơ chế ghi nhận và vinh danh thành viên tích cực:** Đánh giá cuối kỳ dựa trên cảm tính của BCN, gây mất động lực cho các thành viên nhiệt huyết. | **76%** Thành viên | **Cao** *(Giảm gắn kết thành viên)* | Xây dựng công thức tính **Điểm đóng góp (Contribution Score)** tự động và hiển thị **Bảng xếp hạng (Leaderboard)** minh bạch (FR-SYS-06). |

### 1.4 Ma trận Nhu cầu Người dùng và Đề xuất Giải pháp Tích hợp AI

#### A. Mã Biểu đồ Mermaid:
```mermaid
graph TD
    subgraph Khảo sát Thực trạng (Pain Points - Tuần 1)
        P1[Phân công thủ công, sai kỹ năng & trùng lịch]
        P2[Điểm danh giấy chậm, dễ gian lận]
        P3[Quản lý task phân tán qua chat, trễ hạn]
        P4[Viết bài truyền thông tốn thời gian]
        P5[Tóm tắt báo cáo & phản hồi rời rạc]
        P6[Đánh giá đóng góp cảm tính]
    end

    subgraph Giải pháp Chức năng (Đặc tả SRS - Tuần 2)
        S1[FR-SYS-02 Skill Matrix + FR-AI-03 AI Smart Matchmaking]
        S2[FR-SYS-04 Dynamic QR Check-in System]
        S3[FR-SYS-05 Kanban Task Board with RBAC Enforcement]
        S4[FR-AI-01 AI Event Announcement Generator]
        S5[FR-AI-02 AI Activity & Feedback Summarizer]
        S6[FR-SYS-06 Contribution Score & Leaderboard]
    end

    P1 --> S1
    P2 --> S2
    P3 --> S3
    P4 --> S4
    P5 --> S5
    P6 --> S6
```

#### B. Mã Biểu đồ PlantUML:
```plantuml
__PUML_PAINPOINT__
```

---

## CHƯƠNG 2: PHÂN TÍCH YÊU CẦU CHỨC NĂNG (FUNCTIONAL REQUIREMENTS - TUẦN 2)

Trong **Tuần 2**, nhóm tiến hành chuẩn hóa và phân loại các yêu cầu chức năng thành 2 nhóm lớn:

### 2.1 Nhóm Yêu cầu Chức năng Nghiệp vụ Quản lý Hệ thống (FR-SYS)

| Mã Yêu cầu | Tên Chức năng | Mô tả Chi tiết Nghiệp vụ | Tác nhân & Phân quyền |
| :--- | :--- | :--- | :--- |
| **FR-SYS-01** | **Đăng nhập & Phân quyền RBAC** | Xác thực tài khoản Email/Password, cấp token JWT, phân quyền 3 vai trò (`ADMIN`, `LEADER`, `MEMBER`). Kiểm soát truy cập chuẩn API semantics:<br>- Trả về **`HTTP 401 Unauthorized`** nếu chưa xác thực hoặc token JWT không hợp lệ / hết hạn.<br>- Trả về **`HTTP 403 Forbidden`** nếu đã xác thực thành công nhưng không đủ quyền thực hiện thao tác. | Tất cả Tác nhân |
| **FR-SYS-02** | **Quản lý Hồ sơ, Skill & Free Slots** | Thành viên cập nhật thông tin cá nhân, Ma trận Kỹ năng chuyên môn (Photoshop, MC, Setup, Content...) và Lịch rảnh cố định các buổi trong tuần (Free Slots). Dữ liệu được xác thực nghiêm ngặt bằng Pydantic Schema. | Thành viên, Admin |
| **FR-SYS-03** | **Quản lý Ban Chuyên môn & Nhân sự** | Ban Chủ nhiệm tạo ban mới, cập nhật mô tả, điều chuyển thành viên giữa các ban (Truyền thông, Sự kiện, Chuyên môn, Đối ngoại...) và bổ nhiệm Trưởng ban. | Ban Chủ nhiệm (Admin) |
| **FR-SYS-04** | **Quản lý Sự kiện & Điểm danh QR** | Tạo sự kiện mới, tự động sinh mã QR Code độc bản. Cho phép thành viên quét mã QR trên điện thoại để ghi nhận điểm danh tức thì, chống điểm danh trùng lặp bằng ràng buộc khóa duy nhất trên PostgreSQL. | Trưởng ban, Thành viên |
| **FR-SYS-05** | **Quản lý Nhiệm vụ & Kanban Board** | Quản lý vòng đời task qua 3 cột trạng thái (*To-Do, In-Progress, Done*). Ràng buộc RBAC: Leader giao việc & đổi status mọi task; Member chỉ được đổi status task của mình. | Admin, Leader, Member |
| **FR-SYS-06** | **Thống kê & Bảng xếp hạng Đóng góp** | Tự động tính điểm đóng góp cá nhân và hiển thị Leaderboard TOP thành viên xuất sắc.<br>- *Công thức MVP (KT1/KT2):* Score = (Check-in * 10) + (Task Done * 20).<br>- *Định hướng V2.0:* Bổ sung trọng số độ khó task (W trong [1.0, 2.0]) và hệ số đúng hạn (K trong [0.5, 1.0]). | Tất cả Tác nhân |

### 2.2 Nhóm Yêu cầu Chức năng Trí tuệ Nhân tạo (FR-AI)

#### A. Mã Biểu đồ Mermaid:
```mermaid
graph LR
    subgraph Luồng Xử lý AI Thiết kế tại Tuần 2
        In1[Thông tin thô sự kiện] --> AI1[FR-AI-01: AI Sinh Thông báo] --> Out1[Bài viết truyền thông sinh động + Emoji]
        In2[Ghi chú họp & Phản hồi] --> AI2[FR-AI-02: AI Tóm tắt Kết quả] --> Out2[Báo cáo 3 phần: Ưu điểm, Tồn tại, Đề xuất]
        In3[Task List + Skill Matrix + Free Slots] --> AI3[FR-AI-03: AI Gợi ý Phân công] --> Out3[Bảng Matchmaking % & Lý do đề xuất]
    end
```

#### B. Mã Biểu đồ PlantUML:
```plantuml
__PUML_AI_FLOW__
```

| Mã Yêu cầu | Tên Chức năng AI | Mục đích & Mô tả Xử lý | Dữ liệu Đầu vào / Đầu ra |
| :--- | :--- | :--- | :--- |
| **FR-AI-01** | **AI Sinh Bài đăng Thông báo** | AI đóng vai trò Trưởng ban Truyền thông, phân tích thông tin thô sự kiện để tự động soạn bài đăng mạng xã hội thu hút sinh viên kèm emoji. | **Input:** Tên, Mô tả, Thời gian, Địa điểm, Tone giọng (*Hào hứng, Trang trọng, Thân thiện*).<br>**Output:** Văn bản truyền thông hoàn chỉnh. |
| **FR-AI-02** | **AI Tóm tắt Kết quả Hoạt động** | AI đóng vai trò Thư ký tổng hợp, đọc ghi chú cuộc họp và danh sách ý kiến phản hồi để đúc kết báo cáo tổng kết súc tích. | **Input:** Ghi chú họp, danh sách ý kiến phản hồi.<br>**Output:** Báo cáo 3 phần (*Kết quả nổi bật, Hạn chế, Đề xuất cải tiến*). |
| **FR-AI-03** | **AI Gợi ý Phân công Nhiệm vụ** | AI phân tích độ tương đồng giữa yêu cầu công việc với Kỹ năng & Lịch rảnh của thành viên, kết hợp cân bằng tải để đưa ra danh sách ghép cặp tối ưu. | **Input:** Danh sách Task, Danh sách Kỹ năng & Lịch rảnh thành viên.<br>**Output:** Danh sách gợi ý ghép cặp kèm Match Score (%) và lý do. |

---

## CHƯƠNG 3: PHÂN TÍCH YÊU CẦU PHI CHỨC NĂNG & TIÊU CHÍ NGHIỆM THU (NON-FUNCTIONAL REQUIREMENTS - TUẦN 2)

### 3.1 Bảng Đặc tả Tiêu chuẩn Chất lượng ISO/IEC 25010 kèm Acceptance Criteria & Test Method

| Mã NFR | Nhóm Tiêu chuẩn | Tiêu chí & Chỉ số Đo lường Chi tiết | Phương án Kỹ thuật Thiết kế (Flask + PostgreSQL + Docker) | Tiêu chí Nghiệm thu (Acceptance Criteria) & Phương pháp Kiểm thử (Test Method) |
| :---: | :--- | :--- | :--- | :--- |
| **NFR-PERF-01** | Hiệu năng *(Performance)* | - Thời gian phản hồi API CRUD: **P95 $\le$ 500ms**.<br>- Thời gian xử lý AI Engine: **P95 $\le$ 5.0s** (Cloud LLM) & **P99 $\le$ 500ms** (Local Fallback).<br>- Tốc độ First Contentful Paint (FCP): **< 1.2s**. | Flask WSGI với Gunicorn 4 workers, PostgreSQL Indexing khóa ngoại và Vite code-splitting. | **Test Method:** Postman Runner / Apache Benchmark.<br>**Acceptance:** 95% request API CRUD hoàn thành $\le$ 500ms; FCP đo qua Lighthouse $\le$ 1.2s. |
| **NFR-PERF-02** | Hiệu năng *(Performance)* | - Hỗ trợ ít nhất **200 người dùng truy cập đồng thời (200 Concurrent Users / VUs)** trong đợt cao điểm điểm danh mà không nghẽn hệ thống. | Flask Stateless RESTful API, PostgreSQL Connection Pool (pool_size=10, max_overflow=20) chạy trên Docker. | **Test Method:** Load Testing bằng Locust / k6 (5 phút với 200 VUs trên PostgreSQL Container).<br>**Acceptance:** Error Rate $< 1\%$, P95 latency $< 1.0$s tại mức 200 VUs. |
| **NFR-SEC-01** | Bảo mật *(Security)* | - Mật khẩu người dùng được băm an toàn bằng thuật toán chuyên dụng **bcrypt** ($cost \ge 12$, auto-salted). Tuyệt đối không lưu plaintext. | Module `security.py` sử dụng thư viện `bcrypt` tiêu chuẩn của Python. | **Test Method:** Unit Test Auth & Database Dump Security Audit.<br>**Acceptance:** 100% mật khẩu được băm bcrypt, không có bất kỳ plaintext password nào trong PostgreSQL. |
| **NFR-SEC-02** | Bảo mật *(Security)* | - Xác thực bằng **JWT (JSON Web Token)** với thời hạn 7 ngày, ký bằng Secret Key 256-bit. | Middleware `@jwt_required` xác thực JWT trên từng request qua Authorization Header. | **Test Method:** Integration Test với Token hợp lệ, Token hết hạn, Token giả mạo.<br>**Acceptance:** Trả về đúng `HTTP 401 Unauthorized` khi token không hợp lệ hoặc hết hạn. |
| **NFR-SEC-03** | Bảo mật *(Security)* | - Phân quyền **RBAC nghiêm ngặt tại Backend (API Level)**. Chặn Member đổi task của người khác. | Decorator `@roles_required` kết hợp kiểm tra Task Owner trong Flask Blueprint. | **Test Method:** Security API Test giả lập Member gửi lệnh PUT/DELETE task của người khác.<br>**Acceptance:** Hệ thống từ chối và trả về đúng `HTTP 403 Forbidden`. |
| **NFR-SEC-04** | Bảo mật AI *(AI Security)* | - Phòng thủ **Prompt Injection**, chống rò rỉ dữ liệu nhạy cảm và kiểm soát tính toàn vẹn đầu ra của AI. | Thiết kế 5 tầng bảo vệ: Phân tách Context, Giới hạn dữ liệu, Sanitization, Pydantic Output Validation, Human-in-the-loop. | **Test Method:** Adversarial Prompt Injection Test suites.<br>**Acceptance:** AI không thực thi lệnh override ("Ignore instructions"), không làm lộ system context. |
| **NFR-REL-01** | Độ tin cậy *(Reliability)* | - Độ sẵn sàng của hệ thống (**Uptime**) đạt tối thiểu **99.5%** trong suốt kỳ vận hành. | Đóng gói Docker Container độc lập, cơ chế restart policy `always` và logging tập trung. | **Test Method:** Continuous Health-check Endpoint Monitoring `/api/health`.<br>**Acceptance:** Uptime đo lường đạt $\ge 99.5\%$. |
| **NFR-REL-02** | Độ tin cậy *(Reliability)* | - **Cơ chế chịu lỗi Dual-Engine Fallback:** Hệ thống tự động chuyển sang **Local Rule-based Fallback Engine** khi mất mạng hoặc hết quota API. | Dual-Engine: Google Gemini Cloud LLM + Local Rule-based Matcher. | **Test Method:** Ngắt kết nối mạng Internet khi gọi chức năng AI.<br>**Acceptance:** Hệ thống chuyển sang Fallback trong $< 100$ms và trả về kết quả hợp lệ. |
| **NFR-REL-03** | Tính toàn vẹn *(Data Integrity)* | - Ràng buộc khóa ngoại `ON DELETE SET NULL`, `UNIQUE(activity_id, user_id)` chống điểm danh trùng. | Ràng buộc toàn vẹn cơ sở dữ liệu trên PostgreSQL Data Models. | **Test Method:** Database Constraint Testing.<br>**Acceptance:** PostgreSQL báo lỗi IntegrityError khi cố ý ghi dữ liệu trùng lặp. |
| **NFR-USA-01** | Trải nghiệm *(Usability)* | - Giao diện chuẩn **Responsive Web Design**, hiển thị tối ưu trên Desktop, Tablet và Mobile. | Thiết kế CSS Component System theo nguyên lý Mobile-First, độ tương phản WCAG 2.1. | **Test Method:** Cross-Device Testing trên Chrome DevTools (Desktop, iPad, iPhone/Android).<br>**Acceptance:** Không bị tràn màn hình ngang (horizontal scrollbar) trên màn hình $\ge 360$px. |
| **NFR-USA-02** | Trải nghiệm *(Usability)* | - Thao tác đạt chuẩn **3-Click Rule**; tích hợp nút Quick Demo Login và Toast Notification tức thì. | Tối ưu hóa luồng tương tác UX, cung cấp tài khoản thử nghiệm nhanh cho từng vai trò. | **Test Method:** Usability Testing & User Walkthrough.<br>**Acceptance:** Người dùng truy cập bất kỳ tính năng chính nào trong không quá 3 lượt click. |
| **NFR-MNT-01** | Bảo trì *(Maintainability)*| - Mã nguồn phân tầng rõ ràng (Flask Blueprint $\rightarrow$ Service $\rightarrow$ Model $\rightarrow$ Pydantic Schema). | Tuân thủ nguyên lý Clean Architecture & Separation of Concerns. | **Test Method:** Static Code Analysis & Peer Review.<br>**Acceptance:** 100% Endpoint tuân thủ cấu trúc phân tầng và quy ước Pydantic. |
| **NFR-MNT-02** | Khả năng triển khai *(Deployability & Containerization)* | - Hệ thống được đóng gói hoàn chỉnh bằng **Docker & Docker Compose** (PostgreSQL + Flask Backend + React-Vite Frontend). | Tối ưu hóa multi-stage build trong Dockerfile cho Frontend (Nginx) và Backend (Python 3.11 Slim). | **Test Method:** Triển khai tự động bằng lệnh `docker-compose up --build`.<br>**Acceptance:** 100% Core Regression Suite (25+ test cases) pass thành công trên môi trường Dockerized PostgreSQL. |
| **NFR-COMP-01**| Tương thích *(Compatibility)*| - Tương thích hoàn toàn với tất cả các trình duyệt hiện đại (Chrome, Edge, Firefox, Safari). | Tuân thủ chuẩn HTML5, CSS3 và ECMAScript 6+. | **Test Method:** Cross-Browser Testing trên Chrome, Edge, Safari, Firefox.<br>**Acceptance:** Mọi tính năng hoạt động đồng nhất, không phát sinh lỗi script trên Console. |

### 3.2 Đặc tả Cơ chế Bảo mật AI & Phòng chống Prompt Injection Đa tầng
Để giải quyết triệt để rủi ro bảo mật mô hình ngôn ngữ lớn (LLM Security Risks), hệ thống áp dụng chiến lược phòng thủ 5 tầng:
1. **Strict Context Separation (Phân tách ngữ cảnh nghiêm ngặt):** Tách bạch hoàn toàn giữa `System Instructions` và `User Input` qua cấu trúc Message Object chuẩn (`role: system`, `role: user`).
2. **Data Minimization & Boundary Limiting (Thu hẹp phạm vi dữ liệu):** Chỉ cung cấp trường dữ liệu cần thiết cho AI; tuyệt đối không gửi mật khẩu, JWT token, email nhạy cảm hay API keys vào prompt.
3. **Input Sanitization & Length Guard (Lọc đầu vào & Giới hạn độ dài):** Giới hạn độ dài, escape các chuỗi delimiter nhằm chặn các câu lệnh override chỉ thị.
4. **Output Schema Validation (Kiểm tra cấu trúc đầu ra):** Sử dụng Pydantic Schema để ép kiểu và xác thực chặt chẽ định dạng JSON từ AI trước khi xử lý.
5. **Least Privilege & Human-in-the-loop (Kiểm soát quyền & Xác nhận của con người):** AI chỉ đề xuất tư vấn; mọi quyết định quan trọng (gán việc, đăng bài) đều cần Leader/Admin phê duyệt.

---

## CHƯƠNG 4: MÔ HÌNH HÓA CA SỬ DỤNG (USE CASE MODELING - TUẦN 3)

### 4.1 Danh mục Phân rã 12 Use Cases Cốt lõi

| STT | Mã Use Case | Tên Ca Sử dụng (Use Case Name) | Phân hệ (Subsystem / Package) | Tác nhân chính (Primary Actor) | Tác nhân hỗ trợ / Kỹ thuật |
| :---: | :---: | :--- | :--- | :--- | :--- |
| **01** | `UC01` | Đăng nhập & Xác thực JWT | Quản trị Hệ thống & Phân quyền | Người dùng (All Users) | Database Subsystem |
| **02** | `UC02` | Cập nhật Hồ sơ, Skill Matrix & Lịch rảnh | Quản lý Thành viên & Ban | Thành viên, Admin | Database Subsystem |
| **03** | `UC03` | Tra cứu Lịch sử Hoạt động & Leaderboard | Trợ lý AI & Báo cáo Thống kê | Người dùng (All Users) | Database Subsystem |
| **04** | `UC04` | Quản lý Sự kiện & Sinh mã QR Độc bản | Sự kiện & Điểm danh QR | Trưởng ban, Admin | Database Subsystem |
| **05** | `UC05` | Quản lý Nhiệm vụ & Kanban Board | Quản lý Nhiệm vụ & Kanban | Trưởng ban, Admin | Database Subsystem |
| **06** | `UC06` | AI Gợi ý Phân công Nhiệm vụ Thông minh | Trợ lý AI & Báo cáo Thống kê | Trưởng ban, Admin | Cloud LLM / Fallback Engine |
| **07** | `UC07` | AI Sinh Bài đăng Thông báo Sự kiện | Trợ lý AI & Báo cáo Thống kê | Trưởng ban, Admin | Cloud LLM / Fallback Engine |
| **08** | `UC08` | AI Tóm tắt Kết quả Hoạt động & Phản hồi | Trợ lý AI & Báo cáo Thống kê | Trưởng ban, Admin | Cloud LLM / Fallback Engine |
| **09** | `UC09` | Quét mã QR Điểm danh Sự kiện | Sự kiện & Điểm danh QR | Thành viên | Database Subsystem |
| **10** | `UC10` | Cập nhật Tiến độ Task của bản thân | Quản lý Nhiệm vụ & Kanban | Thành viên | Database Subsystem |
| **11** | `UC11` | Quản lý Cơ cấu Ban Chuyên môn | Quản lý Thành viên & Ban | Ban Chủ nhiệm (Admin) | Database Subsystem |
| **12** | `UC12` | Quản lý & Phân quyền Thành viên | Quản trị Hệ thống & Phân quyền | Ban Chủ nhiệm (Admin) | Database Subsystem |

### 4.2 Biểu đồ Use Case Tổng thể Toàn Hệ thống (System Use Case Diagram)

#### A. Mã Biểu đồ Mermaid:
```mermaid
flowchart TD
    User([fa:fa-user Người dùng chung])
    Admin([fa:fa-user-tie Ban Chủ nhiệm / Admin])
    Leader([fa:fa-user-shield Trưởng ban / Leader])
    Member([fa:fa-user-graduate Thành viên / Member])
    AIService([fa:fa-robot Google Gemini AI API / Fallback])

    Admin -->|Thừa kế| User
    Leader -->|Thừa kế| User
    Member -->|Thừa kế| User

    subgraph Sub1["[Package 1] Phân hệ Xác thực & Phân quyền (Auth & RBAC)"]
        UC01(["UC01: Đăng nhập & Xác thực JWT"])
        UC12(["UC12: Quản lý & Phân quyền Tài khoản"])
        UC_V(["<<include>> Xác thực JWT Token & Phân quyền"])
    end

    subgraph Sub2["[Package 2] Phân hệ Quản lý Thành viên & Ban Chuyên môn"]
        UC02(["UC02: Cập nhật Hồ sơ, Skill & Free Slots"])
        UC11(["UC11: Quản lý Cơ cấu Ban Chuyên môn"])
    end

    subgraph Sub3["[Package 3] Phân hệ Quản lý Sự kiện & Điểm danh QR"]
        UC04(["UC04: Quản lý Sự kiện & Sinh mã QR"])
        UC09(["UC09: Quét mã QR Điểm danh"])
        UC_QR(["<<include>> Sinh chuỗi định danh QR độc bản"])
    end

    subgraph Sub4["[Package 4] Phân hệ Quản lý Nhiệm vụ & Kanban Board"]
        UC05(["UC05: Quản lý Nhiệm vụ & Kanban Board"])
        UC10(["UC10: Cập nhật Tiến độ Task của mình"])
        UC_RBAC(["<<include>> Kiểm tra quyền sở hữu Task"])
    end

    subgraph Sub5["[Package 5] Phân hệ Trợ lý AI & Báo cáo Thống kê"]
        UC06(["UC06: AI Gợi ý Phân công Nhiệm vụ"])
        UC07(["UC07: AI Sinh Bài đăng Thông báo"])
        UC08(["UC08: AI Tóm tắt Kết quả Hoạt động"])
        UC03(["UC03: Tra cứu Lịch sử & Leaderboard"])
    end

    User --- UC01
    User --- UC03

    Member --- UC02
    Member --- UC09
    Member --- UC10

    Leader --- UC04
    Leader --- UC05
    Leader --- UC06
    Leader --- UC07
    Leader --- UC08

    Admin --- UC11
    Admin --- UC12

    AIService --- UC06
    AIService --- UC07
    AIService --- UC08

    UC04 -.->|<<include>>| UC_QR
    UC09 -.->|<<include>>| UC_V
    UC10 -.->|<<include>>| UC_RBAC
    UC05 -.->|<<extend>>| UC06
    UC04 -.->|<<extend>>| UC07
```

#### B. Mã Biểu đồ PlantUML ([`docs/plantuml/usecase_overall.puml`](file:///D:/DTC245200328/Nam3/Ki1/UngDungAI/Student_Club_Management/docs/plantuml/usecase_overall.puml)):
```plantuml
__PUML_UC_OVERALL__
```

---

### 4.3 Biểu đồ Use Case Chi tiết theo từng Phân hệ (Subsystem Use Case Diagrams)

#### 4.3.1 Phân hệ 1: Quản trị Tài khoản & Phân quyền Hệ thống (Authentication & RBAC Subsystem)
```plantuml
__PUML_UC_SUB1__
```

#### 4.3.2 Phân hệ 2: Quản lý Hồ sơ Thành viên & Ban Chuyên môn (Member & Department Subsystem)
```plantuml
__PUML_UC_SUB2__
```

#### 4.3.3 Phân hệ 3: Quản lý Sự kiện & Điểm danh QR Độc bản (Event & QR Check-in Subsystem)
```plantuml
__PUML_UC_SUB3__
```

#### 4.3.4 Phân hệ 4: Quản lý Nhiệm vụ & Bảng Kanban (Kanban Task Management Subsystem)
```plantuml
__PUML_UC_SUB4__
```

#### 4.3.5 Phân hệ 5: Trợ lý Trí tuệ Nhân tạo & Báo cáo Thống kê (AI Services & Analytics Subsystem)
```plantuml
__PUML_UC_SUB5__
```

---

### 4.4 Bảng Đặc tả Ca Sử dụng Mẫu Chi tiết (Use Case Specifications)

#### 4.4.1 Use Case Specification 01: Quản lý Sự kiện & Sinh mã QR Điểm danh (UC04 / FR-SYS-04)

| Thuộc tính | Nội dung Chi tiết |
| :--- | :--- |
| **Mã Use Case** | `UC-SPEC-01` (Tương ứng `FR-SYS-04` / `UC04`) |
| **Tên Use Case** | Quản lý Sự kiện & Sinh mã QR Điểm danh Độc bản |
| **Tác nhân chính** | Trưởng ban (`LEADER`), Ban Chủ nhiệm (`ADMIN`) |
| **Tiền điều kiện** | Người dùng đã đăng nhập thành công với vai trò Leader hoặc Admin. |
| **Hậu điều kiện** | Sự kiện mới được tạo trong CSDL PostgreSQL kèm chuỗi mã QR Code độc bản và hiển thị trên Dashboard. |
| **Luồng sự kiện chính (Main Flow)** | 1. Người dùng chọn chức năng "Quản lý Sự kiện" $\rightarrow$ Nhấn "Tạo Sự kiện mới".<br>2. Hệ thống hiển thị biểu mẫu (Tên sự kiện, Ban tổ chức, Thời gian bắt đầu/kết thúc, Địa điểm, Mô tả).<br>3. Người dùng nhập thông tin hợp lệ và nhấn "Lưu sự kiện".<br>4. Hệ thống sinh mã nhận diện duy nhất (`activity_id`), tự động tạo chuỗi định danh QR độc bản.<br>5. Hệ thống lưu sự kiện vào PostgreSQL và kết xuất hình ảnh mã QR Code lên màn hình để Leader trình chiếu. |
| **Luồng rẽ nhánh (Alternative Flow)** | 3a. Người dùng muốn cập nhật thông tin sự kiện cũ: Chọn sự kiện $\rightarrow$ Sửa thông tin $\rightarrow$ Hệ thống cập nhật và giữ nguyên mã QR ban đầu. |
| **Luồng ngoại lệ (Exception Flow)** | 3b. Người dùng nhập thiếu trường bắt buộc hoặc thời gian kết thúc trước thời gian bắt đầu: Hệ thống hiển thị thông báo lỗi Validation (Pydantic) và yêu cầu nhập lại. |
| **Quy tắc nghiệp vụ (Business Rules)** | - Mã QR là độc bản cho từng sự kiện.<br>- Chỉ tài khoản có vai trò Leader hoặc Admin mới có quyền tạo sự kiện và lấy mã QR. |

#### 4.4.2 Use Case Specification 02: Quản lý Nhiệm vụ qua Kanban Board & Siết chặt RBAC (UC05 & UC10 / FR-SYS-05)

| Thuộc tính | Nội dung Chi tiết |
| :--- | :--- |
| **Mã Use Case** | `UC-SPEC-02` (Tương ứng `FR-SYS-05` / `UC05` & `UC10`) |
| **Tên Use Case** | Quản lý Nhiệm vụ, Phân công & Cập nhật Trạng thái Kanban Board |
| **Tác nhân chính** | Ban Chủ nhiệm (`ADMIN`), Trưởng ban (`LEADER`), Thành viên (`MEMBER`) |
| **Tiền điều kiện** | Người dùng đã đăng nhập với JWT hợp lệ; sự kiện hoặc ban chuyên môn đã tồn tại. |
| **Hậu điều kiện** | Trạng thái nhiệm vụ được cập nhật trên Kanban Board và đồng bộ vào PostgreSQL. |
| **Luồng sự kiện chính (Main Flow)** | 1. Người dùng mở màn hình "Kanban Board" của Ban/Sự kiện.<br>2. Hệ thống tải danh sách nhiệm vụ phân bố theo 3 cột: *To-Do, In-Progress, Done*.<br>3. Người dùng kéo-thả task hoặc đổi trạng thái task sang cột mới.<br>4. Hệ thống kiểm tra quyền hạn (RBAC):<br>   - Nếu là Admin/Leader: Cho phép thay đổi trạng thái mọi task và gán người làm.<br>   - Nếu là Member: Chỉ cho phép đổi trạng thái của task do chính mình phụ trách (`assignee_id == current_user.id`).<br>5. Hệ thống cập nhật PostgreSQL và hiển thị thông báo Toast thành công. |
| **Luồng rẽ nhánh (Alternative Flow)** | 3a. Trưởng ban tạo task mới: Nhấn "Thêm Task" $\rightarrow$ Nhập tiêu đề, deadline, chọn thành viên phụ trách $\rightarrow$ Task xuất hiện tại cột *To-Do*. |
| **Luồng ngoại lệ (Exception Flow)** | 4a. Thành viên cố ý gọi API sửa task của người khác: Backend chặn và trả về mã lỗi `HTTP 403 Forbidden` kèm thông báo "Bạn không có quyền chỉnh sửa nhiệm vụ này". |
| **Quy tắc nghiệp vụ (Business Rules)** | - Thành viên thường không được quyền tạo task mới hoặc đổi người phụ trách task.<br>- Khi task chuyển sang *Done*, hệ thống ghi nhận thời điểm hoàn thành để phục vụ tính điểm đóng góp. |

#### 4.4.3 Use Case Specification 03: AI Gợi ý Phân công Nhiệm vụ Thông minh (UC06 / FR-AI-03)

| Thuộc tính | Nội dung Chi tiết |
| :--- | :--- |
| **Mã Use Case** | `UC-SPEC-03` (Tương ứng `FR-AI-03` / `UC06`) |
| **Tên Use Case** | AI Gợi ý Phân công Nhiệm vụ Thông minh (Smart Matchmaking) |
| **Tác nhân chính** | Trưởng ban (`LEADER`), Ban Chủ nhiệm (`ADMIN`), External AI Service |
| **Tiền điều kiện** | Đã có danh sách nhiệm vụ cần làm và hồ sơ thành viên có đăng ký Skill Matrix & Lịch rảnh. |
| **Hậu điều kiện** | Bảng đề xuất ghép cặp nhân sự kèm Match Score (%) và lý do rõ ràng được hiển thị cho Leader duyệt. |
| **Luồng sự kiện chính (Main Flow)** | 1. Trưởng ban truy cập màn hình phân công nhiệm vụ $\rightarrow$ Nhấn nút "AI Gợi ý Phân công".<br>2. Backend Flask thu thập danh sách Task chưa phân công cùng Ma trận Kỹ năng & Lịch rảnh của các thành viên trong Ban.<br>3. Backend đóng gói Context chuẩn hóa và gửi yêu cầu tới AI Engine.<br>4. AI Engine tính toán độ tương đồng kỹ năng, kiểm tra trùng lịch, cân bằng tải công việc và sinh danh sách gợi ý.<br>5. Backend validate định dạng JSON qua Pydantic và trả về giao diện bảng gợi ý ghép cặp kèm Match Score (%) và lý do tường minh.<br>6. Trưởng ban duyệt danh sách: Có thể chấp nhận toàn bộ hoặc chỉnh sửa người phụ trách trước khi nhấn "Áp dụng phân công". |
| **Luồng rẽ nhánh (Alternative Flow)** | 4a. Mất kết nối Internet hoặc lỗi Quota Cloud AI: Hệ thống tự động kích hoạt **Local Rule-based Fallback Engine** dựa trên thuật toán so khớp từ khóa và slot rảnh để trả kết quả ngay lập tức ($< 100$ms). |
| **Luồng ngoại lệ (Exception Flow)** | 2a. Ban chưa có thành viên nào khai báo kỹ năng: Hệ thống hiển thị thông báo hướng dẫn thành viên cập nhật Skill Matrix trước khi dùng AI. |
| **Quy tắc nghiệp vụ (Business Rules)** | - AI chỉ đóng vai trò Trợ lý tư vấn đề xuất, quyết định phân công cuối cùng thuộc về Trưởng ban (Human-in-the-loop).<br>- Toàn bộ lịch sử Prompt và Output được lưu vào bảng `ai_logs` trong PostgreSQL để phục vụ đánh giá và tinh chỉnh. |

### 4.5 Ma trận Phân loại Mức độ Ưu tiên theo Phương pháp MoSCoW

| Phân loại MoSCoW | Danh sách Yêu cầu Chức năng & Phi chức năng Tương ứng | Cam kết Phạm vi Giai đoạn KT2 & KT3 |
| :--- | :--- | :--- |
| **MUST HAVE**<br>*(Bắt buộc cốt lõi)* | - `FR-SYS-01`: Đăng nhập, Xác thực JWT & Phân quyền RBAC 3 vai trò.<br>- `FR-SYS-02`: Quản lý Hồ sơ, Kỹ năng (Skill Matrix) & Lịch rảnh (Free Slots).<br>- `FR-SYS-04`: Quản lý Sự kiện & Điểm danh Mã QR Code độc bản.<br>- `FR-SYS-05`: Quản lý Nhiệm vụ qua Kanban Board & Siết chặt RBAC.<br>- `FR-AI-03`: AI Gợi ý Phân công Nhiệm vụ Thông minh.<br>- `NFR-SEC-01` & `NFR-SEC-03`: Bảo mật mật khẩu (Bcrypt) & RBAC API. | **Cam kết hoàn thành 100% trong Tuần 4 - 6 (KT2)** |
| **SHOULD HAVE**<br>*(Nên có - Giá trị gia tăng)* | - `FR-AI-01`: AI Sinh bài đăng thông báo sự kiện đa phong cách.<br>- `FR-AI-02`: AI Tóm tắt kết quả hoạt động và phản hồi cuộc họp.<br>- `FR-SYS-06`: Thống kê & Bảng xếp hạng Đóng góp (Leaderboard).<br>- `NFR-REL-02`: Cơ chế AI Dual-Engine Fallback (chạy cả Offline & Online).<br>- `NFR-USA-01`: Giao diện Responsive tối ưu trên thiết bị di động. | **Cam kết hoàn thành 100% trong Tuần 6 - 7 (KT2/KT3)** |
| **COULD HAVE**<br>*(Có thể bổ sung sau)* | - Tự động đẩy thông báo bài đăng qua Zalo Official Account / Telegram Bot.<br>- Xuất báo cáo điểm danh và thống kê nhiệm vụ ra file Excel / PDF.<br>- Tính năng bình chọn (Voting/Poll) trực tuyến trong sự kiện. | *Định hướng nghiên cứu mở rộng trong Phiên bản v2.0* |
| **WON'T HAVE**<br>*(Không thực hiện đợt này)* | - Tích hợp cổng thanh toán trực tuyến (VNPay, MoMo) để thu quỹ CLB.<br>- Tính năng Video Call trực tuyến nội bộ trong ứng dụng.<br>- Hệ thống nhận diện khuôn mặt điểm danh (Face ID). | *Không thuộc phạm vi Đề tài 28* |

---

## CHƯƠNG 5: MÔ HÌNH HÓA VÀ THIẾT KẾ HỆ THỐNG BẰNG CÁC BIỂU ĐỒ UML (UML MODELING & SYSTEM DESIGN - TUẦN 3)

### 5.1 Biểu đồ Lớp Phân tích & Thực thể (UML Class Diagram / Domain Entity Model)
```plantuml
__PUML_CLASS__
```

---

### 5.2 Biểu đồ Hoạt động (UML Activity Diagrams)

#### 5.2.1 Activity Diagram 01: Quy trình Đăng nhập, Xác thực JWT & Phân quyền RBAC
```plantuml
__PUML_ACT_AUTH__
```

#### 5.2.2 Activity Diagram 02: Quy trình Tổ chức Sự kiện & Điểm danh Tự động bằng Mã QR Độc bản
```plantuml
__PUML_ACT_QR__
```

#### 5.2.3 Activity Diagram 03: Quy trình AI Smart Matchmaking với Dual-Engine Fallback
```plantuml
__PUML_ACT_AI__
```

---

### 5.3 Biểu đồ Tuần tự (UML Sequence Diagrams)

#### 5.3.1 Sequence Diagram 01: Xác thực Đăng nhập & Cấp JWT Token
```plantuml
__PUML_SEQ_AUTH__
```

#### 5.3.2 Sequence Diagram 02: Quét Mã QR Điểm danh Sự kiện Realtime
```plantuml
__PUML_SEQ_QR__
```

#### 5.3.3 Sequence Diagram 03: AI Gợi ý Phân công Nhiệm vụ với Dual-Engine Fallback
```plantuml
__PUML_SEQ_AI__
```

#### 5.3.4 Sequence Diagram 04: Cập nhật Trạng thái Task trên Kanban Board với Kiểm soát RBAC
```plantuml
__PUML_SEQ_KANBAN__
```

---

### 5.4 Biểu đồ Máy Trạng thái (UML State Machine Diagrams)

#### 5.4.1 State Machine Diagram 01: Vòng đời Trạng thái Nhiệm vụ (Task Lifecycle)
```plantuml
__PUML_STATE_TASK__
```

#### 5.4.2 State Machine Diagram 02: Vòng đời Trạng thái Sự kiện (Activity Lifecycle)
```plantuml
__PUML_STATE_ACT__
```

---

### 5.5 Biểu đồ Thành phần & Triển khai (UML Component & Deployment Diagram)
```plantuml
__PUML_DEPLOY__
```

---

## CHƯƠNG 6: MA TRẬN TRUY VẾT YÊU CẦU (RTM) & KẾ HOẠCH BÀN GIAO GIAI ĐOẠN KT2 (TUẦN 3)

| Mã Yêu cầu | Nguồn gốc Khảo sát | Tác nhân Áp dụng | Use Case Ánh xạ | Lớp UML / Bảng PostgreSQL | Kế hoạch Triển khai Code Flask & React (KT2) |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **FR-SYS-01** | Pain Point #3 (Bảo mật & Phân quyền) | All Actors | `UC01`, `UC12` | Class `User` $\rightarrow$ Table `users` | Tuần 4: Lập trình Flask Auth Blueprint, JWT & Security Middleware |
| **FR-SYS-02** | Pain Point #1 (Thiếu Skill & Free Slots) | Member, Admin | `UC02`, `UC12` | Class `User` $\rightarrow$ Table `users` (`skills, free_slots`) | Tuần 5: Lập trình Flask Members Blueprint & Pydantic Schema Validation |
| **FR-SYS-03** | Nhu cầu cơ cấu tổ chức & quản lý nhân sự | Admin | `UC11`, `UC12` | Class `Department` $\rightarrow$ Table `departments` | Tuần 5: Lập trình CRUD Ban chuyên môn & Phân bổ thành viên |
| **FR-SYS-04** | Pain Point #2 (Điểm danh giấy chậm, gian lận) | Leader, Member | `UC04`, `UC09` | Class `Activity`, `Attendance` $\rightarrow$ Table `activities`, `attendances` | Tuần 5: Lập trình Dynamic QR Generation & API Quét QR Check-in |
| **FR-SYS-05** | Pain Point #3 (Theo dõi task rời rạc, trễ hạn) | Leader, Member | `UC05`, `UC10` | Class `Task`, `TaskAssignment` $\rightarrow$ Table `tasks`, `task_assignments` | Tuần 6: Lập trình Kanban Board & Kiểm soát RBAC Update Task |
| **FR-SYS-06** | Pain Point #6 (Đánh giá đóng góp cảm tính) | All Actors | `UC03` | Class `Attendance`, `Task` $\rightarrow$ Tables `attendances`, `tasks` | Tuần 6: Lập trình Dashboard Stats & Leaderboard Realtime |
| **FR-AI-01** | Pain Point #4 (Viết bài truyền thông tốn thời gian) | Leader, Admin | `UC07` | Class `AIService`, `AILog` $\rightarrow$ Table `ai_logs` | Tuần 7: Tích hợp Prompt AI Sinh bài đăng đa Tone giọng |
| **FR-AI-02** | Pain Point #5 (Tóm tắt họp & phản hồi rời rạc) | Leader, Admin | `UC08` | Class `AIService`, `AILog` $\rightarrow$ Table `ai_logs` | Tuần 7: Tích hợp Prompt AI Tóm tắt biên bản 3 phần |
| **FR-AI-03** | Pain Point #1 (Phân công thủ công sai kỹ năng) | Leader, Admin | `UC06` | Class `AIService`, `TaskAssignment`, `AILog` | Tuần 7: Tích hợp Thuật toán AI Matchmaking & Dual-Engine Fallback |

---

## KẾT LUẬN GIAI ĐOẠN KT1 (HẾT TUẦN 3)

1. **Về mặt Khảo sát & Phân tích (Tuần 1 & 2):** Nhóm đã hoàn thành xuất sắc công tác khảo sát thực trạng, xác định chính xác 06 Điểm đau và chuẩn hóa thành **06 Yêu cầu Chức năng Quản lý (FR-SYS)**, **03 Yêu cầu Chức năng AI (FR-AI)** và **14 Tiêu chí Phi chức năng (NFR)** theo chuẩn ISO/IEC 25010 với đầy đủ tiêu chí nghiệm thu và phương pháp kiểm thử.
2. **Về mặt Thiết kế & Mô hình hóa UML (Tuần 3):** Đã hoàn tất trọn bộ mô hình hóa Ca sử dụng (Biểu đồ Use Case Tổng thể, 5 Biểu đồ Use Case Phân hệ, 12 Use Cases & 03 Use Case Specifications chi tiết) và hệ thống Biểu đồ UML toàn diện (Class Diagram, 3 Activity Diagrams, 4 Sequence Diagrams, 2 State Machine Diagrams, Component & Deployment Diagram) chèn trực tiếp đầy đủ mã nguồn **Mermaid** & **PlantUML**.
3. **Sẵn sàng chuyển giao sang Giai đoạn KT2:** Toàn bộ tài liệu khảo sát và phân tích yêu cầu này đóng vai trò là "Kim chỉ nam" kỹ thuật vững chắc để đội ngũ phát triển nhóm 15 bắt đầu bước vào giai đoạn lập trình mã nguồn Backend Flask, Frontend React-Vite, PostgreSQL Database và cấu hình Docker Compose từ **Tuần 4**.
"""

md_content = md_template
md_content = md_content.replace("__PUML_PAINPOINT__", puml_painpoint)
md_content = md_content.replace("__PUML_AI_FLOW__", puml_ai_flow)
md_content = md_content.replace("__PUML_UC_OVERALL__", puml_uc_overall)
md_content = md_content.replace("__PUML_UC_SUB1__", puml_uc_sub1)
md_content = md_content.replace("__PUML_UC_SUB2__", puml_uc_sub2)
md_content = md_content.replace("__PUML_UC_SUB3__", puml_uc_sub3)
md_content = md_content.replace("__PUML_UC_SUB4__", puml_uc_sub4)
md_content = md_content.replace("__PUML_UC_SUB5__", puml_uc_sub5)
md_content = md_content.replace("__PUML_CLASS__", puml_class)
md_content = md_content.replace("__PUML_ACT_AUTH__", puml_act_auth)
md_content = md_content.replace("__PUML_ACT_QR__", puml_act_qr)
md_content = md_content.replace("__PUML_ACT_AI__", puml_act_ai)
md_content = md_content.replace("__PUML_SEQ_AUTH__", puml_seq_auth)
md_content = md_content.replace("__PUML_SEQ_QR__", puml_seq_qr)
md_content = md_content.replace("__PUML_SEQ_AI__", puml_seq_ai)
md_content = md_content.replace("__PUML_SEQ_KANBAN__", puml_seq_kanban)
md_content = md_content.replace("__PUML_STATE_TASK__", puml_state_task)
md_content = md_content.replace("__PUML_STATE_ACT__", puml_state_act)
md_content = md_content.replace("__PUML_DEPLOY__", puml_deploy)

# Save Markdown file
md_file_path = os.path.join(docs_dir, "08_KhaoSat_PhanTich_YeuCau_ChucNang_PhiChucNang.md")
with open(md_file_path, "w", encoding="utf-8") as f:
    f.write(md_content)
print(f"SUCCESSFULLY GENERATED MARKDOWN WITH COMPLETE EMBEDDED CODES: {md_file_path}")

# -------------------------------------------------------------
# 2. WORD (.DOCX) STRUCTURE AND GENERATION (KT1 SCOPE)
# -------------------------------------------------------------
p8_sections_kt1 = [
    ("MỤC LỤC TỔNG QUAN TÀI LIỆU", [
        "CHƯƠNG 1: TỔNG QUAN KHẢO SÁT HIỆN TRẠNG (TUẦN 1)",
        "  1.1 Mục tiêu và Phương pháp khảo sát quy trình quản lý CLB",
        "  1.2 Phân loại Tác nhân Người dùng & Tác nhân Hệ thống (Actors)",
        "    1.2.1 Chân dung Người dùng (User Personas)",
        "    1.2.2 Tác nhân Hệ thống & Dịch vụ Bên ngoài (System Actors)",
        "  1.3 Thống kê Kết quả Khảo sát & Phân tích 06 Điểm đau (Pain Points)",
        "  1.4 Ma trận Nhu cầu Người dùng và Đề xuất Giải pháp Tích hợp AI (Kèm Code Biểu đồ)",
        "CHƯƠNG 2: PHÂN TÍCH YÊU CẦU CHỨC NĂNG (TUẦN 2)",
        "  2.1 Nhóm Yêu cầu Chức năng Nghiệp vụ Quản lý Hệ thống (FR-SYS)",
        "  2.2 Nhóm Yêu cầu Chức năng Trí tuệ Nhân tạo (FR-AI) (Kèm Code Biểu đồ)",
        "CHƯƠNG 3: PHÂN TÍCH YÊU CẦU PHI CHỨC NĂNG & TIÊU CHÍ NGHIỆM THU (TUẦN 2)",
        "  3.1 Bảng Đặc tả Tiêu chuẩn Chất lượng ISO/IEC 25010 (14 Tiêu chí NFR)",
        "  3.2 Đặc tả Cơ chế Bảo mật AI & Phòng chống Prompt Injection Đa tầng",
        "CHƯƠNG 4: MÔ HÌNH HÓA CA SỬ DỤNG (USE CASE MODELING - TUẦN 3)",
        "  4.1 Danh mục Phân rã 12 Use Cases Cốt lõi của Toàn Hệ thống",
        "  4.2 Biểu đồ Use Case Tổng thể Toàn Hệ thống (System Use Case Diagram)",
        "  4.3 Biểu đồ Use Case Chi tiết theo từng Phân hệ (05 Phân hệ Chức năng)",
        "    4.3.1 Phân hệ 1: Xác thực & Phân quyền Hệ thống (Auth & RBAC)",
        "    4.3.2 Phân hệ 2: Quản lý Hồ sơ Thành viên & Ban Chuyên môn",
        "    4.3.3 Phân hệ 3: Quản lý Sự kiện & Điểm danh QR Độc bản",
        "    4.3.4 Phân hệ 4: Quản lý Nhiệm vụ & Bảng Kanban Board",
        "    4.3.5 Phân hệ 5: Trợ lý Trí tuệ Nhân tạo & Báo cáo Thống kê",
        "  4.4 Bảng Đặc tả Ca Sử dụng Mẫu Chi tiết (UC04, UC05/UC10, UC06)",
        "  4.5 Ma trận Phân loại Mức độ Ưu tiên theo Phương pháp MoSCoW",
        "CHƯƠNG 5: MÔ HÌNH HÓA VÀ THIẾT KẾ HỆ THỐNG BẰNG CÁC BIỂU ĐỒ UML (TUẦN 3)",
        "  5.1 Biểu đồ Lớp Phân tích & Thực thể CSDL (UML Class Diagram)",
        "  5.2 Biểu đồ Hoạt động (UML Activity Diagrams - 03 Quy trình Cốt lõi)",
        "    5.2.1 Activity Diagram 01: Đăng nhập, Xác thực Bcrypt & Cấp Token JWT",
        "    5.2.2 Activity Diagram 02: Tổ chức Sự kiện & Điểm danh Tự động bằng Mã QR Độc bản",
        "    5.2.3 Activity Diagram 03: AI Gợi ý Phân công Nhiệm vụ với Dual-Engine Fallback",
        "  5.3 Biểu đồ Tuần tự (UML Sequence Diagrams - 04 Tương tác Thời gian thực)",
        "    5.3.1 Sequence Diagram 01: Xác thực Đăng nhập & Cấp JWT Token",
        "    5.3.2 Sequence Diagram 02: Quét Mã QR Điểm danh Sự kiện Realtime",
        "    5.3.3 Sequence Diagram 03: AI Gợi ý Phân công Nhiệm vụ với Dual-Engine Fallback",
        "    5.3.4 Sequence Diagram 04: Cập nhật Trạng thái Task trên Kanban Board với RBAC Guard",
        "  5.4 Biểu đồ Máy Trạng thái (UML State Machine Diagrams - 02 Vòng đời Thực thể)",
        "    5.4.1 State Machine Diagram 01: Vòng đời Trạng thái Nhiệm vụ (Task Lifecycle)",
        "    5.4.2 State Machine Diagram 02: Vòng đời Trạng thái Sự kiện (Activity Lifecycle)",
        "  5.5 Biểu đồ Thành phần & Triển khai Docker Architecture (Component & Deployment Diagram)",
        "CHƯƠNG 6: MA TRẬN TRUY VẾT YÊU CẦU (RTM) & KẾ HOẠCH BÀN GIAO GIAI ĐOẠN KT2 (TUẦN 3)",
        "KẾT LUẬN GIAI ĐOẠN KT1 (HẾT TUẦN 3)"
    ]),
    ("CHƯƠNG 1: TỔNG QUAN KHẢO SÁT HIỆN TRẠNG (TUẦN 1)", [
        "1.1 Mục tiêu và Phương pháp khảo sát quy trình quản lý CLB:",
        "Trong khuôn khổ Tuần 1 của Kế hoạch thực hiện dự án, đội ngũ BA đã tiến hành khảo sát toàn diện thực trạng vận hành của các Câu lạc bộ sinh viên nhằm làm rõ yêu cầu nghiệp vụ với 3 phương pháp chính:",
        " - Phỏng vấn sâu (Deep Interview): Phỏng vấn trực tiếp 06 thành viên Ban Chủ nhiệm và 08 Trưởng ban chuyên môn của các CLB sinh viên tiêu biểu để thu thập quy trình vận hành và khó khăn thực tế.",
        " - Khảo sát qua biểu mẫu câu hỏi: Thu thập ý kiến phản hồi từ 120 sinh viên thuộc 4 Ban chuyên môn (Truyền thông, Sự kiện, Chuyên môn, Đối ngoại) về trải nghiệm tham gia hoạt động, nhận nhiệm vụ và điểm danh.",
        " - Quan sát trực tiếp quy trình (Direct Observation): Ghi nhận thực tế quy trình họp tuần, cách thức phân chia nhiệm vụ sự kiện và phương pháp ký tên điểm danh truyền thống.",
        "1.2 Phân loại Tác nhân Người dùng & Tác nhân Hệ thống (Actors):",
        "1.2.1 Chân dung Người dùng (User Personas):",
        ('table',
         ["Tác nhân (Actor)", "Vai trò trong CLB", "Mục tiêu cốt lõi", "Khó khăn / Điểm đau chính"],
         [
             ["Ban Chủ nhiệm (Admin)", "Lãnh đạo cao nhất của CLB", "Nắm bắt bức tranh tổng thể hoạt động CLB; Quản lý cơ cấu ban, phân quyền; Đánh giá chính xác mức độ đóng góp để khen thưởng.", "Dữ liệu phân tán trên nhiều file Excel/Drive; Không có số liệu đo lường độ tích cực; Báo cáo tổng kết cuối kỳ mất nhiều ngày."],
             ["Trưởng ban (Leader)", "Quản lý ban chuyên môn, điều phối sự kiện", "Phân công nhiệm vụ nhanh chóng, đúng người đúng việc; Điểm danh sự kiện nhanh gọn; Soạn bài đăng truyền thông thu hút.", "Mất 2-3h/sự kiện để hỏi lịch rảnh & kỹ năng; Điểm danh giấy tốn thời gian, dễ sót hoặc nhầm lẫn; Soạn bài truyền thông cạn ý tưởng."],
             ["Thành viên (Member)", "Thực hiện nhiệm vụ, tham gia hoạt động", "Nắm rõ nhiệm vụ được giao và deadline; Cập nhật kỹ năng sở trường và lịch rảnh; Điểm danh dễ dàng qua điện thoại.", "Bị giao việc trùng lịch học/trái sở trường; Bỏ sót task do trôi tin nhắn chat; Không thấy được điểm số đóng góp của bản thân."]
         ]
        ),
        "1.2.2 Tác nhân Hệ thống & Dịch vụ Bên ngoài (System Actors & External Services):",
        ('table',
         ["Tác nhân Kỹ thuật", "Loại tác nhân", "Vai trò & Trách nhiệm Kỹ thuật", "Cơ chế Tương tác / Giao thức"],
         [
             ["Google Gemini / OpenAI API", "External Cloud AI Service", "Xử lý ngôn ngữ tự nhiên (NLP) phục vụ sinh bài đăng truyền thông, tóm tắt báo cáo và phân tích tương đồng kỹ năng.", "Giao thức RESTful HTTPS API (JSON Payload), xác thực qua API Key và biến môi trường .env."],
             ["Local Rule-based Fallback Engine", "Internal Subsystem", "Cung cấp cơ chế dự phòng cục bộ dựa trên tập luật (Rule-based) và thuật toán heuristic khi mất mạng Internet hoặc lỗi quota API bên ngoài.", "Xử lý nội bộ tại tầng Service (In-Memory Rule Matching Engine)."],
             ["Database Subsystem (PostgreSQL)", "Internal Data Layer", "Lưu trữ và đảm bảo tính toàn vẹn dữ liệu quan hệ người dùng, ban, sự kiện, điểm danh, nhiệm vụ và nhật ký AI.", "PostgreSQL 16 chạy trong Docker Container qua SQLAlchemy ORM."]
         ]
        ),
        "1.3 Thống kê Kết quả Khảo sát Thực trạng & 06 Điểm đau (Pain Points):",
        ('table',
         ["STT", "Vấn đề / Điểm đau (Pain Point)", "Tỷ lệ ghi nhận", "Mức độ ảnh hưởng", "Giải pháp yêu cầu hệ thống"],
         [
             ["1", "Phân công nhiệm vụ thủ công qua tin nhắn, không nắm rõ lịch rảnh & kỹ năng thành viên", "92% Trưởng ban", "Rất cao (Lãng phí 2-3h/sự kiện)", "Xây dựng Hồ sơ Ma trận Kỹ năng (Skill Matrix) + Lịch rảnh kết hợp Tính năng AI Gợi ý phân công tự động (FR-AI-03)."],
             ["2", "Điểm danh bằng giấy / Google Form bị chậm, dễ sót hoặc gian lận điểm danh hộ", "78% Sự kiện", "Cao (Mất 15-20 phút đầu buổi)", "Tính năng Tạo mã QR Code độc bản cho sự kiện và cho phép thành viên quét QR trên điện thoại để điểm danh tức thì (FR-SYS-04)."],
             ["3", "Ban chủ nhiệm khó theo dõi tiến độ nhiệm vụ và đánh giá mức độ đóng góp thành viên", "85% Ban Chủ nhiệm", "Rất cao (Đánh giá cảm tính)", "Tích hợp Bảng Kanban Board trực quan (To-Do, In-Progress, Done) có siết chặt phân quyền RBAC và đo lường thời gian (FR-SYS-05)."],
             ["4", "Viết bài thông báo truyền thông sự kiện tốn thời gian, văn phong chưa thu hút", "88% Ban Truyền thông", "Trung bình", "Tính năng AI Sinh bài viết thông báo sự kiện hỗ trợ nhiều Tone giọng (Hào hứng, Trang trọng, Thân thiện...) và tự động chèn emoji (FR-AI-01)."],
             ["5", "Tổng hợp tóm tắt kết quả cuộc họp và phản hồi thành viên bị rời rạc", "80% Trưởng ban", "Trung bình", "Tính năng AI Tóm tắt kết quả hoạt động tự động trích xuất ưu/nhược điểm và hành động cải tiến từ ghi chú (FR-AI-02)."],
             ["6", "Thiếu cơ chế ghi nhận và vinh danh thành viên tích cực minh bạch", "76% Thành viên", "Cao (Giảm gắn kết thành viên)", "Xây dựng công thức tính Điểm đóng góp (Contribution Score) tự động và hiển thị Bảng xếp hạng (Leaderboard) minh bạch (FR-SYS-06)."]
         ]
        ),
        "1.4 Ma trận Nhu cầu Người dùng và Đề xuất Giải pháp Tích hợp AI (Kèm Code Biểu đồ):",
        ('code', "painpoint_to_solution.puml", puml_painpoint)
    ]),
    ("CHƯƠNG 2: PHÂN TÍCH YÊU CẦU CHỨC NĂNG (FUNCTIONAL REQUIREMENTS - TUẦN 2)", [
        "Trong Tuần 2, nhóm tiến hành chuẩn hóa và phân loại các yêu cầu chức năng thành 2 nhóm lớn:",
        "2.1 Danh mục Yêu cầu Chức năng Nghiệp vụ Quản lý Hệ thống (FR-SYS):",
        ('table',
         ["Mã Yêu cầu", "Tên Chức năng", "Mô tả Chi tiết Yêu cầu Chức năng", "Phân quyền Tác nhân"],
         [
             ["FR-SYS-01", "Đăng nhập & Phân quyền RBAC", "Xác thực tài khoản Email/Password, cấp token JWT, phân quyền 3 vai trò (Admin, Leader, Member). Kiểm soát API: HTTP 401 Unauthorized nếu chưa đăng nhập/token sai; HTTP 403 Forbidden nếu không đủ quyền.", "Tất cả Tác nhân"],
             ["FR-SYS-02", "Quản lý Hồ sơ, Skill & Free Slots", "Cập nhật thông tin cá nhân, Ma trận Kỹ năng (Photoshop, MC, Setup, Content...) và Lịch rảnh cố định các buổi trong tuần (Free Slots). Dữ liệu validate bằng Pydantic Schema.", "Thành viên / Admin"],
             ["FR-SYS-03", "Quản lý Ban chuyên môn & Nhân sự", "Tạo ban mới, sửa thông tin ban, điều chuyển thành viên vào các Ban (Truyền thông, Sự kiện, Chuyên môn, Đối ngoại...) và bổ nhiệm Trưởng ban.", "Ban Chủ nhiệm (Admin)"],
             ["FR-SYS-04", "Quản lý Sự kiện & Điểm danh QR", "Tạo sự kiện mới, tự động sinh mã QR Code độc bản. Thành viên quét QR để điểm danh tức thì, chống điểm danh trùng lặp.", "Trưởng ban / Thành viên"],
             ["FR-SYS-05", "Quản lý Nhiệm vụ & Kanban Board", "Tạo task, theo dõi tiến độ 3 cột (To-Do, In-Progress, Done). Siết chặt phân quyền: Admin/Leader phân công & đổi status mọi task; Member chỉ được đổi status task của mình.", "Admin / Leader / Member"],
             ["FR-SYS-06", "Thống kê & Bảng xếp hạng", "Tính điểm đóng góp (MVP: Check-in*10 + Task hoàn thành*20; Định hướng V2.0: thêm trọng số độ khó và hệ số đúng hạn) và hiển thị Leaderboard TOP đóng góp thành viên.", "Tất cả Tác nhân"]
         ]
        ),
        "2.2 Danh mục Yêu cầu Chức năng Tích hợp AI (FR-AI):",
        ('table',
         ["Mã Yêu cầu", "Tên Chức năng AI", "Mô tả Chi tiết Yêu cầu Chức năng AI", "Đầu vào / Đầu ra"],
         [
             ["FR-AI-01", "AI Sinh Bài đăng Thông báo", "AI phân tích thông tin thô sự kiện để tự động soạn văn bản truyền thông sinh động với emoji và nhiều Tone giọng (Hào hứng, Trang trọng, Thân thiện).", "Input: Tên, Mô tả, Thời gian, Địa điểm, Tone giọng.\nOutput: Văn bản truyền thông hoàn chỉnh."],
             ["FR-AI-02", "AI Tóm tắt Kết quả Hoạt động", "AI đọc ghi chú cuộc họp và phản hồi của thành viên để tổng hợp báo cáo tóm tắt ưu/nhược điểm và hướng khắc phục.", "Input: Ghi chú họp, danh sách phản hồi.\nOutput: Báo cáo tóm tắt 3 phần súc tích."],
             ["FR-AI-03", "AI Gợi ý Phân công Nhiệm vụ", "AI phân tích danh sách Task và Skill Matrix + Lịch rảnh của thành viên để tính Match Score (%) và gợi ý phân công tối ưu.", "Input: Task list, Member skills, Free slots.\nOutput: Danh sách gợi ý ghép cặp + Lý do tường minh."]
         ]
        ),
        "Mã nguồn Biểu đồ Luồng dữ liệu AI (Pipeline Flow):",
        ('code', "ai_functional_flow.puml", puml_ai_flow)
    ]),
    ("CHƯƠNG 3: PHÂN TÍCH YÊU CẦU PHI CHỨC NĂNG & TIÊU CHÍ NGHIỆM THU (NON-FUNCTIONAL REQUIREMENTS - TUẦN 2)", [
        "Yêu cầu phi chức năng quy định các tiêu chuẩn chất lượng, ràng buộc kỹ thuật và tiêu chí vận hành của hệ thống theo chuẩn ISO/IEC 25010 kèm Tiêu chí nghiệm thu (Acceptance Criteria) và Phương pháp kiểm thử (Test Method):",
        ('table',
         ["Mã NFR", "Nhóm Tiêu chuẩn", "Tiêu chí & Chỉ số Đo lường Chi tiết", "Phương án Kỹ thuật Thiết kế (Flask + PostgreSQL + Docker)", "Tiêu chí Nghiệm thu & Phương pháp Kiểm thử"],
         [
             ["NFR-PERF-01", "Hiệu năng (Performance)", "Thời gian phản hồi API CRUD: P95 <= 500ms; Thời gian phản hồi AI Engine: P95 <= 5.0s (Cloud LLM) và P99 <= 500ms (Local Fallback). Tốc độ load trang FCP < 1.2s.", "Flask WSGI với Gunicorn 4 workers, PostgreSQL Indexing khóa ngoại và React Vite bundling.", "Test Method: Postman Runner / Apache Benchmark.\nAcceptance: 95% request API CRUD hoàn thành <= 500ms; FCP đo qua Lighthouse <= 1.2s."],
             ["NFR-PERF-02", "Hiệu năng (Performance)", "Hỗ trợ ít nhất 200 người dùng truy cập đồng thời (200 Concurrent Users / VUs) trong các đợt cao điểm điểm danh mà không nghẽn hệ thống.", "Stateless RESTful API trên Flask, PostgreSQL Connection Pool (pool_size=10, max_overflow=20) chạy trên Docker.", "Test Method: Load Testing bằng Locust / k6 (5 phút với 200 VUs trên PostgreSQL Container).\nAcceptance: Error Rate < 1%, P95 latency < 1.0s tại mức 200 VUs."],
             ["NFR-SEC-01", "Bảo mật (Security)", "Mật khẩu người dùng được băm an toàn bằng thuật toán chuyên dụng bcrypt (cost >= 12, auto-salted). Tuyệt đối không lưu plaintext password.", "Module security.py sử dụng thư viện bcrypt tiêu chuẩn của Python.", "Test Method: Unit Test Auth & Database Dump Security Audit.\nAcceptance: 100% mật khẩu được băm bcrypt, không có plaintext."],
             ["NFR-SEC-02", "Bảo mật (Security)", "Xác thực API bằng JWT Token với thời hạn 7 ngày, ký bằng Secret Key mạnh (256-bit).", "Middleware @jwt_required xác thực JWT trên từng request qua Authorization Header.", "Test Method: Integration Test Token hợp lệ / hết hạn / giả mạo.\nAcceptance: Trả về đúng HTTP 401 Unauthorized khi token không hợp lệ hoặc hết hạn."],
             ["NFR-SEC-03", "Bảo mật (Security)", "Phân quyền RBAC nghiêm ngặt tại Backend (API Level). Chặn Member sửa task của người khác với HTTP 403 Forbidden.", "Decorator @roles_required kết hợp kiểm tra Task Owner trong Flask Blueprint.", "Test Method: Security API Test giả lập Member sửa task người khác.\nAcceptance: Backend từ chối với đúng HTTP 403 Forbidden."],
             ["NFR-SEC-04", "Bảo mật AI (AI Security)", "Phòng thủ Prompt Injection, chống rò rỉ dữ liệu nhạy cảm và kiểm soát toàn vẹn đầu ra AI.", "Thiết kế 5 tầng: Phân tách Context, Giới hạn dữ liệu, Sanitization, Pydantic Validation, Human-in-the-loop.", "Test Method: Adversarial Prompt Injection Test suites.\nAcceptance: AI không thực thi lệnh override, không rò rỉ system context."],
             ["NFR-REL-01", "Độ tin cậy (Reliability)", "Tỷ lệ hoạt động liên tục (Uptime) >= 99.5%. Hệ thống tự phục hồi lỗi runtime.", "Đóng gói Docker Container độc lập, restart policy always và logging tập trung.", "Test Method: Continuous Health-check Endpoint Monitoring /api/health.\nAcceptance: Uptime đo lường đạt >= 99.5%."],
             ["NFR-REL-02", "Độ tin cậy (Reliability)", "Cơ chế chịu lỗi Dual-Engine Fallback: Tự động chuyển sang Local Rule-based Fallback Engine khi mất mạng hoặc hết quota API.", "Dual-Engine: Gemini/OpenAI Cloud + Local Rule-based Fallback Matcher.", "Test Method: Ngắt kết nối mạng Internet khi gọi chức năng AI.\nAcceptance: Hệ thống chuyển sang Fallback trong < 100ms và trả về kết quả hợp lệ."],
             ["NFR-REL-03", "Độ tin cậy (Reliability)", "Đảm bảo tính toàn vẹn dữ liệu: Ràng buộc khóa ngoại ON DELETE SET NULL, UNIQUE(activity_id, user_id).", "Cấu hình ràng buộc toàn vẹn trên PostgreSQL Data Models.", "Test Method: Database Constraint Testing.\nAcceptance: Database báo lỗi IntegrityError khi ghi dữ liệu trùng."],
             ["NFR-USA-01", "Giao diện (Usability)", "Giao diện chuẩn Responsive tương thích Mobile & Desktop. Màu sắc chuẩn HSL, font Plus Jakarta Sans.", "Thiết kế UI Component System chuẩn UX, độ tương phản WCAG 2.1.", "Test Method: Responsive Chrome DevTools (Desktop, Tablet, Mobile).\nAcceptance: Không bị tràn màn hình ngang trên thiết bị >= 360px."],
             ["NFR-USA-02", "Giao diện (Usability)", "Thao tác đạt chuẩn 3-Click Rule; có nút Quick Demo Login và Toast notification tức thì.", "Tối ưu hóa hành trình người dùng, phản hồi trực quan.", "Test Method: Usability Testing & User Walkthrough.\nAcceptance: Người dùng truy cập tính năng chính trong <= 3 click."],
             ["NFR-MNT-01", "Bảo trì (Maintainability)", "Mã nguồn phân tầng rõ ràng (Flask Blueprint -> Service -> Model -> Pydantic Schema).", "Tuân thủ Clean Architecture & Pydantic Data Schema validation.", "Test Method: Static Code Analysis & Peer Review.\nAcceptance: 100% Endpoint tuân thủ cấu trúc phân tầng."],
             ["NFR-MNT-02", "Triển khai & Mở rộng (Deployment & Docker)", "Hệ thống được đóng gói hoàn chỉnh bằng Docker & Docker Compose (PostgreSQL + Flask + React-Vite).", "Sử dụng multi-stage Dockerfile cho Frontend (Nginx) và Backend (Gunicorn/Flask).", "Test Method: Triển khai tự động bằng docker-compose up --build.\nAcceptance: 100% Core Regression Test Suite (25+ tests) pass trên môi trường Dockerized PostgreSQL."],
             ["NFR-COMP-01", "Tương thích (Compatibility)", "Tương thích hoàn toàn các trình duyệt Chrome, Edge, Firefox, Safari.", "Tuân thủ chuẩn HTML5, CSS3, ECMAScript 6+.", "Test Method: Cross-Browser Testing trên Chrome, Edge, Safari, Firefox.\nAcceptance: Mọi tính năng hoạt động đồng nhất, không phát sinh lỗi console."]
         ]
        )
    ]),
    ("CHƯƠNG 4: MÔ HÌNH HÓA CA SỬ DỤNG (USE CASE MODELING - TUẦN 3)", [
        "Trong Tuần 3, nhóm hoàn thiện mô hình hóa Use Case, phân rã 12 ca sử dụng cốt lõi, xây dựng Biểu đồ Use Case Tổng thể & Phân hệ, cùng bảng đặc tả chi tiết cho các Use Case quan trọng nhất:",
        "4.1 Danh mục Phân rã 12 Use Cases Cốt lõi của Hệ thống:",
        ('table',
         ["Mã UC", "Tên Ca Sử dụng (Use Case Name)", "Phân hệ Chức năng (Package)", "Tác nhân chính (Primary Actor)", "Tác nhân hỗ trợ / Hệ thống"],
         [
             ["UC01", "Đăng nhập & Xác thực JWT", "Xác thực & Phân quyền", "Người dùng (All Users)", "Database Subsystem"],
             ["UC02", "Cập nhật Hồ sơ, Skill Matrix & Lịch rảnh", "Quản lý Thành viên & Ban", "Thành viên / Admin", "Database Subsystem"],
             ["UC03", "Tra cứu Lịch sử Hoạt động & Leaderboard", "Trợ lý AI & Báo cáo", "Người dùng (All Users)", "Database Subsystem"],
             ["UC04", "Quản lý Sự kiện & Sinh mã QR Độc bản", "Sự kiện & Điểm danh QR", "Trưởng ban / Admin", "Database Subsystem"],
             ["UC05", "Quản lý Nhiệm vụ & Kanban Board", "Quản lý Nhiệm vụ & Kanban", "Trưởng ban / Admin", "Database Subsystem"],
             ["UC06", "AI Gợi ý Phân công Nhiệm vụ Thông minh", "Trợ lý AI & Báo cáo", "Trưởng ban / Admin", "Cloud LLM / Fallback Engine"],
             ["UC07", "AI Sinh Bài đăng Thông báo Sự kiện", "Trợ lý AI & Báo cáo", "Trưởng ban / Admin", "Cloud LLM / Fallback Engine"],
             ["UC08", "AI Tóm tắt Kết quả Hoạt động & Phản hồi", "Trợ lý AI & Báo cáo", "Trưởng ban / Admin", "Cloud LLM / Fallback Engine"],
             ["UC09", "Quét mã QR Điểm danh Sự kiện", "Sự kiện & Điểm danh QR", "Thành viên", "Database Subsystem"],
             ["UC10", "Cập nhật Tiến độ Task của bản thân", "Quản lý Nhiệm vụ & Kanban", "Thành viên", "Database Subsystem"],
             ["UC11", "Quản lý Cơ cấu Ban Chuyên môn", "Quản lý Thành viên & Ban", "Ban Chủ nhiệm (Admin)", "Database Subsystem"],
             ["UC12", "Quản lý & Phân quyền Thành viên", "Xác thực & Phân quyền", "Ban Chủ nhiệm (Admin)", "Database Subsystem"]
         ]
        ),
        "4.2 Biểu đồ Use Case Tổng thể Toàn Hệ thống (System Use Case Diagram):",
        " - Cấu trúc 5 Gói / Phân hệ (Packages): (1) Phân hệ Xác thực & Phân quyền; (2) Phân hệ Quản lý Thành viên & Ban; (3) Phân hệ Sự kiện & Điểm danh QR; (4) Phân hệ Nhiệm vụ & Kanban Board; (5) Phân hệ Trợ lý AI & Báo cáo Thống kê.",
        " - Quan hệ Thừa kế Tác nhân: Ban Chủ nhiệm (Admin), Trưởng ban (Leader) và Thành viên (Member) đều thừa kế từ Người dùng chung (Authenticated User).",
        " - Quan hệ phụ thuộc: UC04 include 'Sinh mã QR độc bản'; UC09 include 'Xác thực JWT'; UC10 include 'RBAC Check Task Owner'; UC05 extend 'UC06 AI Gợi ý Phân công'; UC04 extend 'UC07 AI Sinh Bài đăng'.",
        ('code', "usecase_overall.puml", puml_uc_overall),
        "4.3 Biểu đồ Use Case Chi tiết theo từng Phân hệ (05 Phân hệ Chức năng):",
        "4.3.1 Phân hệ 1: Xác thực & Phân quyền Hệ thống (Auth & RBAC):",
        ('code', "usecase_sub1_auth.puml", puml_uc_sub1),
        "4.3.2 Phân hệ 2: Quản lý Hồ sơ Thành viên & Ban Chuyên môn:",
        ('code', "usecase_sub2_member.puml", puml_uc_sub2),
        "4.3.3 Phân hệ 3: Quản lý Sự kiện & Điểm danh QR Độc bản:",
        ('code', "usecase_sub3_event.puml", puml_uc_sub3),
        "4.3.4 Phân hệ 4: Quản lý Nhiệm vụ & Bảng Kanban Board:",
        ('code', "usecase_sub4_task.puml", puml_uc_sub4),
        "4.3.5 Phân hệ 5: Trợ lý Trí tuệ Nhân tạo & Báo cáo Thống kê:",
        ('code', "usecase_sub5_ai.puml", puml_uc_sub5),
        "4.4 Bảng Đặc tả Ca Sử dụng Mẫu (Use Case Specifications):",
        "4.4.1 Use Case Specification 01: Quản lý Sự kiện & Sinh mã QR Điểm danh (UC04 / FR-SYS-04):",
        ('table',
         ["Thuộc tính", "Nội dung Chi tiết Đặc tả Use Case"],
         [
             ["Mã Use Case", "UC-SPEC-01 (Tương ứng FR-SYS-04 / UC04)"],
             ["Tên Use Case", "Quản lý Sự kiện & Sinh mã QR Điểm danh Độc bản"],
             ["Tác nhân chính", "Trưởng ban (Leader), Ban Chủ nhiệm (Admin)"],
             ["Tiền điều kiện", "Người dùng đã đăng nhập thành công với vai trò Leader hoặc Admin."],
             ["Hậu điều kiện", "Sự kiện mới được tạo trong CSDL PostgreSQL kèm chuỗi mã QR Code độc bản và hiển thị trên Dashboard."],
             ["Luồng sự kiện chính", "1. Người dùng chọn chức năng 'Quản lý Sự kiện' -> Nhấn 'Tạo Sự kiện mới'.\n2. Hệ thống hiển thị biểu mẫu (Tên sự kiện, Ban tổ chức, Thời gian bắt đầu/kết thúc, Địa điểm, Mô tả).\n3. Người dùng nhập thông tin hợp lệ và nhấn 'Lưu sự kiện'.\n4. Hệ thống sinh mã nhận diện duy nhất (activity_id), tự động tạo chuỗi định danh QR độc bản.\n5. Hệ thống lưu sự kiện vào PostgreSQL và kết xuất hình ảnh mã QR Code lên màn hình để Leader trình chiếu."],
             ["Luồng rẽ nhánh", "3a. Người dùng muốn cập nhật sự kiện cũ: Chọn sự kiện -> Sửa thông tin -> Hệ thống cập nhật và giữ nguyên mã QR ban đầu."],
             ["Luồng ngoại lệ", "3b. Người dùng nhập thiếu trường bắt buộc hoặc thời gian kết thúc trước thời gian bắt đầu: Hệ thống báo lỗi Validation (Pydantic) và yêu cầu nhập lại."],
             ["Quy tắc nghiệp vụ", "- Mã QR là độc bản cho từng sự kiện.\n- Chỉ tài khoản có vai trò Leader hoặc Admin mới có quyền tạo sự kiện và lấy mã QR."]
         ]
        ),
        "4.4.2 Use Case Specification 02: Quản lý Nhiệm vụ qua Kanban Board & Siết chặt RBAC (UC05 & UC10 / FR-SYS-05):",
        ('table',
         ["Thuộc tính", "Nội dung Chi tiết Đặc tả Use Case"],
         [
             ["Mã Use Case", "UC-SPEC-02 (Tương ứng FR-SYS-05 / UC05 & UC10)"],
             ["Tên Use Case", "Quản lý Nhiệm vụ, Phân công & Cập nhật Trạng thái Kanban Board"],
             ["Tác nhân chính", "Ban Chủ nhiệm (Admin), Trưởng ban (Leader), Thành viên (Member)"],
             ["Tiền điều kiện", "Người dùng đã đăng nhập với JWT hợp lệ; sự kiện hoặc ban chuyên môn đã tồn tại."],
             ["Hậu điều kiện", "Trạng thái nhiệm vụ được cập nhật trên Kanban Board và đồng bộ vào PostgreSQL."],
             ["Luồng sự kiện chính", "1. Người dùng mở màn hình 'Kanban Board' của Ban/Sự kiện.\n2. Hệ thống tải danh sách nhiệm vụ phân bố theo 3 cột: To-Do, In-Progress, Done.\n3. Người dùng kéo-thả task hoặc đổi trạng thái task sang cột mới.\n4. Hệ thống kiểm tra quyền hạn (RBAC):\n   - Nếu là Admin/Leader: Cho phép thay đổi trạng thái mọi task và gán người làm.\n   - Nếu là Member: Chỉ cho phép đổi trạng thái của task do chính mình phụ trách (assignee_id == current_user.id).\n5. Hệ thống cập nhật PostgreSQL và hiển thị thông báo Toast thành công."],
             ["Luồng rẽ nhánh", "3a. Trưởng ban tạo task mới: Nhấn 'Thêm Task' -> Nhập tiêu đề, deadline, chọn thành viên phụ trách -> Task xuất hiện tại cột To-Do."],
             ["Luồng ngoại lệ", "4a. Thành viên cố ý gọi API sửa task của người khác: Backend chặn và trả về mã lỗi HTTP 403 Forbidden kèm thông báo 'Bạn không có quyền chỉnh sửa nhiệm vụ này'."],
             ["Quy tắc nghiệp vụ", "- Thành viên thường không được quyền tạo task mới hoặc đổi người phụ trách task.\n- Khi task chuyển sang Done, hệ thống ghi nhận thời điểm hoàn thành để phục vụ tính điểm đóng góp."]
         ]
        ),
        "4.4.3 Use Case Specification 03: AI Gợi ý Phân công Nhiệm vụ Thông minh (UC06 / FR-AI-03):",
        ('table',
         ["Thuộc tính", "Nội dung Chi tiết Đặc tả Use Case"],
         [
             ["Mã Use Case", "UC-SPEC-03 (Tương ứng FR-AI-03 / UC06)"],
             ["Tên Use Case", "AI Gợi ý Phân công Nhiệm vụ Thông minh (Smart Matchmaking)"],
             ["Tác nhân chính", "Trưởng ban (Leader), Ban Chủ nhiệm (Admin), External AI Service"],
             ["Tiền điều kiện", "Đã có danh sách nhiệm vụ cần làm và hồ sơ thành viên có đăng ký Skill Matrix & Lịch rảnh."],
             ["Hậu điều kiện", "Bảng đề xuất ghép cặp nhân sự kèm Match Score (%) và lý do rõ ràng được hiển thị cho Leader duyệt."],
             ["Luồng sự kiện chính", "1. Trưởng ban truy cập màn hình phân công nhiệm vụ -> Nhấn nút 'AI Gợi ý Phân công'.\n2. Backend Flask thu thập danh sách Task chưa phân công cùng Ma trận Kỹ năng & Lịch rảnh của các thành viên trong Ban.\n3. Backend đóng gói Context chuẩn hóa và gửi yêu cầu tới AI Engine.\n4. AI Engine tính toán độ tương đồng kỹ năng, kiểm tra trùng lịch, cân bằng tải công việc và sinh danh sách gợi ý.\n5. Backend validate định dạng JSON qua Pydantic và trả về giao diện bảng gợi ý ghép cặp kèm Match Score (%) và lý do tường minh.\n6. Trưởng ban duyệt danh sách: Có thể chấp nhận toàn bộ hoặc chỉnh sửa người phụ trách trước khi nhấn 'Áp dụng phân công'.\n7. Backend cập nhật PostgreSQL và đồng bộ Kanban Board."],
             ["Luồng rẽ nhánh", "4a. Mất kết nối Internet hoặc lỗi Quota Cloud AI: Hệ thống tự động kích hoạt Local Rule-based Fallback Engine dựa trên thuật toán so khớp từ khóa và slot rảnh để trả kết quả ngay lập tức (< 100ms)."],
             ["Luồng ngoại lệ", "2a. Ban chưa có thành viên nào khai báo kỹ năng: Hệ thống hiển thị thông báo hướng dẫn thành viên cập nhật Skill Matrix trước khi dùng AI."],
             ["Quy tắc nghiệp vụ", "- AI chỉ đóng vai trò Trợ lý tư vấn đề xuất, quyết định phân công cuối cùng thuộc về Trưởng ban (Human-in-the-loop).\n- Toàn bộ lịch sử Prompt và Output được lưu vào bảng ai_logs trong PostgreSQL để phục vụ đánh giá và tinh chỉnh."]
         ]
        ),
        "4.5 Ma trận Phân loại Mức độ Ưu tiên theo Phương pháp MoSCoW:",
        ('table',
         ["Mức độ Ưu tiên", "Danh sách Yêu cầu Chức năng & Phi chức năng Tương ứng", "Cam kết Phạm vi Giai đoạn KT2 & KT3"],
         [
             ["Must Have (Bắt buộc cốt lõi)", "FR-SYS-01 (Flask Auth JWT & RBAC), FR-SYS-02 (Member/Skill Matrix), FR-SYS-04 (QR Check-in), FR-SYS-05 (Kanban Task RBAC), FR-AI-03 (AI Phân công), NFR-SEC-01 & NFR-SEC-03 (Bảo mật Bcrypt & RBAC).", "Cam kết hoàn thành 100% trong Tuần 4 - 6 (KT2)."],
             ["Should Have (Nên có)", "FR-AI-01 (AI Sinh thông báo), FR-AI-02 (AI Tóm tắt), FR-SYS-06 (Bảng xếp hạng đóng góp), NFR-REL-02 (Local Rule-based Fallback Engine), NFR-USA-01 (Responsive UI).", "Cam kết hoàn thành 100% trong Tuần 6 - 7 (KT2/KT3)."],
             ["Could Have (Có thể bổ sung)", "Tích hợp gửi thông báo qua Zalo OA / Telegram Bot, Export báo cáo Excel / PDF, Bình chọn trực tuyến.", "Định hướng nghiên cứu mở rộng trong Phiên bản v2.0."],
             ["Won't Have (Chưa làm đợt này)", "Thanh toán lệ phí CLB qua cổng VNPay/Momo trực tuyến, Video Call trực tiếp trong app, Điểm danh Face ID.", "Không thuộc phạm vi Đề tài 28."]
         ]
        )
    ]),
    ("CHƯƠNG 5: MÔ HÌNH HÓA VÀ THIẾT KẾ HỆ THỐNG BẰNG CÁC BIỂU ĐỒ UML (UML MODELING & SYSTEM DESIGN - TUẦN 3)", [
        "Trong Tuần 3, nhóm hoàn thiện toàn diện bộ biểu đồ phân tích và thiết kế hướng đối tượng chuẩn UML 2.5:",
        "5.1 Biểu đồ Lớp Phân tích & Thực thể (UML Class Diagram / Domain Entity Model):",
        ('table',
         ["Tên Lớp (Class Name)", "Thuộc tính (Attributes)", "Phương thức (Methods)", "Mô tả Vai trò & Quan hệ"],
         [
             ["User", "+ id: int\n+ email: str\n+ password_hash: str\n+ full_name: str\n+ role: RoleEnum\n+ department_id: int\n+ skills: List[str]\n+ free_slots: List[str]\n+ created_at: datetime", "+ authenticate(password) bool\n+ update_profile(skills, slots) void\n+ calculate_contribution_score() int", "Thực thể Người dùng (Admin, Leader, Member). Quan hệ: N-1 với Department, 1-N với Attendance, 1-N với TaskAssignment."],
             ["Department", "+ id: int\n+ name: str\n+ description: str\n+ leader_id: int", "+ get_members() List[User]\n+ add_member(user_id) void\n+ get_active_tasks() List[Task]", "Thực thể Ban Chuyên môn (Truyền thông, Sự kiện, Đối ngoại, Chuyên môn). Quan hệ: 1-N với User, 1-N với Task."],
             ["Activity", "+ id: int\n+ title: str\n+ description: str\n+ location: str\n+ start_time: datetime\n+ end_time: datetime\n+ qr_code_token: str\n+ status: ActivityStatus\n+ created_by: int", "+ generate_qr_code() str\n+ get_attendance_rate() float\n+ close_activity() void", "Thực thể Sự kiện / Hoạt động CLB. Quan hệ: 1-N với Attendance, 1-N với Task."],
             ["Attendance", "+ id: int\n+ activity_id: int\n+ user_id: int\n+ checkin_time: datetime\n+ method: str", "+ verify_qr(token) bool\n+ record_checkin() void", "Thực thể Điểm danh. Khóa Unique(activity_id, user_id) chống điểm danh trùng lặp."],
             ["Task", "+ id: int\n+ activity_id: int\n+ department_id: int\n+ title: str\n+ description: str\n+ required_skills: List[str]\n+ deadline: datetime\n+ status: TaskStatus\n+ created_by: int", "+ assign_member(user_id) void\n+ update_status(new_status) void\n+ is_overdue() bool", "Thực thể Nhiệm vụ Kanban. Quan hệ: 1-1 với TaskAssignment, N-1 với Department, N-1 với Activity."],
             ["TaskAssignment", "+ id: int\n+ task_id: int\n+ user_id: int\n+ match_score: float\n+ is_ai_suggested: bool\n+ suggestion_reason: str\n+ assigned_at: datetime", "+ confirm_assignment() void", "Thực thể Phân công công việc ghi nhận đề xuất AI và duyệt của Leader."],
             ["AILog", "+ id: int\n+ feature_type: str\n+ prompt_text: str\n+ response_payload: dict\n+ engine_used: str\n+ execution_time_ms: int\n+ created_at: datetime", "+ log_interaction() void", "Lưu vết toàn bộ Prompt và Output của AI phục vụ đánh giá và bảo mật."],
             ["AIService", "+ api_key: str\n+ model_name: str\n+ fallback_engine: Object", "+ suggest_assignments(tasks, members)\n+ generate_announcement(event, tone)\n+ summarize_activity(notes, feedbacks)", "Lớp dịch vụ trung gian tích hợp Google Gemini API và Local Rule-based Fallback Engine."]
         ]
        ),
        "Mã nguồn Biểu đồ Lớp Phân tích (Class Diagram):",
        ('code', "class_diagram.puml", puml_class),
        "5.2 Danh mục Biểu đồ Hoạt động (UML Activity Diagrams):",
        " - 5.2.1 Activity Diagram 01: Quy trình Đăng nhập, Xác thực JWT & Phân quyền RBAC:",
        ('code', "activity_auth_login.puml", puml_act_auth),
        " - 5.2.2 Activity Diagram 02: Quy trình Tổ chức Sự kiện & Điểm danh Tự động bằng Mã QR Độc bản:",
        ('code', "activity_qr_attendance.puml", puml_act_qr),
        " - 5.2.3 Activity Diagram 03: Quy trình AI Smart Matchmaking với Dual-Engine Fallback:",
        ('code', "activity_ai_matching.puml", puml_act_ai),
        "5.3 Danh mục Biểu đồ Tuần tự (UML Sequence Diagrams):",
        " - 5.3.1 Sequence Diagram 01: Luồng Xác thực Đăng nhập & Cấp JWT Token:",
        ('code', "sequence_auth_login.puml", puml_seq_auth),
        " - 5.3.2 Sequence Diagram 02: Luồng Quét Mã QR Điểm danh Sự kiện Realtime:",
        ('code', "sequence_qr_checkin.puml", puml_seq_qr),
        " - 5.3.3 Sequence Diagram 03: Luồng AI Gợi ý Phân công Nhiệm vụ với Dual-Engine Fallback:",
        ('code', "sequence_ai_matchmaking.puml", puml_seq_ai),
        " - 5.3.4 Sequence Diagram 04: Luồng Cập nhật Trạng thái Task trên Kanban Board với Kiểm soát RBAC:",
        ('code', "sequence_kanban_rbac.puml", puml_seq_kanban),
        "5.4 Danh mục Biểu đồ Máy Trạng thái (UML State Machine Diagrams):",
        " - 5.4.1 State Machine Diagram 01: Vòng đời Trạng thái Nhiệm vụ (Task Lifecycle):",
        ('code', "state_task_lifecycle.puml", puml_state_task),
        " - 5.4.2 State Machine Diagram 02: Vòng đời Trạng thái Sự kiện (Activity Lifecycle):",
        ('code', "state_activity_lifecycle.puml", puml_state_act),
        "5.5 Biểu đồ Thành phần & Triển khai Docker Architecture (Component & Deployment Diagram):",
        ('code', "deployment_docker.puml", puml_deploy)
    ]),
    ("CHƯƠNG 6: MA TRẬN TRUY VẾT YÊU CẦU (RTM) & KẾ HOẠCH BÀN GIAO GIAI ĐOẠN KT2 (TUẦN 3)", [
        "Tại thời điểm kết thúc Tuần 3, toàn bộ các yêu cầu đã được ánh xạ chặt chẽ sang Use Cases, thiết kế mô hình dữ liệu PostgreSQL và phân bổ kế hoạch lập trình cụ thể cho Giai đoạn KT2 (Bắt đầu từ Tuần 4):",
        ('table',
         ["Mã Yêu cầu", "Nguồn gốc Khảo sát", "Tác nhân Áp dụng", "Use Case Ánh xạ", "Bảng PostgreSQL / Lớp UML", "Kế hoạch Triển khai Code Flask (KT2)"],
         [
             ["FR-SYS-01", "Pain Point #3 (Bảo mật & Phân quyền)", "Tất cả Tác nhân", "UC01, UC12", "Class User -> Bảng users", "Tuần 4: Lập trình Flask Auth Blueprint, JWT & Security Middleware."],
             ["FR-SYS-02", "Pain Point #1 (Thiếu Skill & Free Slots)", "Member, Admin", "UC02, UC12", "Class User -> Bảng users (skills, free_slots)", "Tuần 5: Lập trình Flask Members Blueprint & Pydantic Schema Validation."],
             ["FR-SYS-03", "Nhu cầu cơ cấu tổ chức & quản lý nhân sự", "Admin", "UC11, UC12", "Class Department -> Bảng departments", "Tuần 5: Lập trình CRUD Ban chuyên môn & Phân bổ thành viên."],
             ["FR-SYS-04", "Pain Point #2 (Điểm danh giấy chậm, gian lận)", "Leader, Member", "UC04, UC09", "Class Activity, Attendance -> Bảng activities, attendances", "Tuần 5: Lập trình Sinh mã QR & API Quét QR Check-in."],
             ["FR-SYS-05", "Pain Point #3 (Theo dõi task rời rạc, trễ hạn)", "Leader, Member", "UC05, UC10", "Class Task, TaskAssignment -> Bảng tasks, task_assignments", "Tuần 6: Lập trình Kanban Board & Kiểm soát RBAC Update Task."],
             ["FR-SYS-06", "Pain Point #6 (Đánh giá đóng góp cảm tính)", "Tất cả Tác nhân", "UC03", "Class Attendance, Task -> Bảng attendances, tasks", "Tuần 6: Lập trình Dashboard Stats & Leaderboard Realtime."],
             ["FR-AI-01", "Pain Point #4 (Viết bài truyền thông tốn thời gian)", "Leader, Admin", "UC07", "Class AIService, AILog -> Bảng ai_logs", "Tuần 7: Tích hợp Prompt AI Sinh bài đăng đa Tone giọng."],
             ["FR-AI-02", "Pain Point #5 (Tóm tắt họp & phản hồi rời rạc)", "Leader, Admin", "UC08", "Class AIService, AILog -> Bảng ai_logs", "Tuần 7: Tích hợp Prompt AI Tóm tắt biên bản 3 phần."],
             ["FR-AI-03", "Pain Point #1 (Phân công thủ công sai kỹ năng)", "Leader, Admin", "UC06", "Class AIService, TaskAssignment -> Bảng task_assignments, ai_logs", "Tuần 7: Tích hợp Thuật toán AI Matchmaking & Dual-Engine Fallback."]
         ]
        ),
        "KẾT LUẬN GIAI ĐOẠN KT1 (HẾT TUẦN 3):",
        "1. Về mặt Khảo sát & Phân tích (Tuần 1 & 2): Nhóm đã hoàn thành xuất sắc công tác khảo sát thực trạng, xác định chính xác 06 Điểm đau và chuẩn hóa thành 06 Yêu cầu Chức năng Quản lý (FR-SYS), 03 Yêu cầu Chức năng AI (FR-AI) và 14 Tiêu chí Phi chức năng (NFR) theo chuẩn ISO/IEC 25010 với đầy đủ tiêu chí nghiệm thu và phương pháp kiểm thử.",
        "2. Về mặt Thiết kế & Chuẩn bị Bàn giao (Tuần 3): Đã hoàn tất trọn bộ mô hình hóa Ca sử dụng (Biểu đồ Use Case Tổng thể, 5 Biểu đồ Use Case Phân hệ, 12 Use Cases & 03 Use Case Specifications chi tiết) và hệ thống Biểu đồ UML toàn diện (Class Diagram, 3 Activity Diagrams, 4 Sequence Diagrams, 2 State Machine Diagrams, Component & Deployment Diagram) chèn đầy đủ mã nguồn Mermaid & PlantUML.",
        "3. Sẵn sàng chuyển giao sang Giai đoạn KT2: Toàn bộ tài liệu khảo sát và phân tích yêu cầu này đóng vai trò là 'Kim chỉ nam' kỹ thuật vững chắc để đội ngũ phát triển nhóm 15 bắt đầu bước vào giai đoạn lập trình mã nguồn Backend Flask, Frontend React-Vite, PostgreSQL Database và cấu hình Docker Compose từ Tuần 4."
    ])
]

# Set cell background shading
def set_cell_shading(cell, color_hex):
    from docx.oxml import parse_xml
    from docx.oxml.ns import nsdecls
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

# Set cell internal margins (padding in dxa: 20 dxa = 1 pt)
def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

# Generate Unified Docx Document with Larger, Highly Legible Font Sizes & Embedded Code Blocks
def generate_docx(file_name, doc_title, sections):
    doc = docx.Document()
    
    # Margins: 1 inch (2.54 cm)
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)
        
    # Title (18 pt Bold)
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run(doc_title)
    r_title.bold = True
    r_title.font.name = "Times New Roman"
    r_title.font.size = Pt(18)
    r_title.font.color.rgb = RGBColor(0, 51, 102)
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(10)
    
    # Metadata Block (12 pt & 11.5 pt)
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_meta.paragraph_format.line_spacing = 1.2
    p_meta.paragraph_format.space_after = Pt(14)
    
    runs_meta = [
        ("Nhóm 15 - Thành viên nhóm (Nhóm 2 SV)\n", True, 12),
        ("La Văn Quyền (Trưởng nhóm - Lead Dev / Architect)\n", False, 12),
        ("Nguyễn Đức Anh (Thành viên - BA / UX / QA)\n", False, 12),
        ("Tên ứng dụng: Hệ thống quản lý câu lạc bộ sinh viên có tích hợp AI\n", True, 12),
        ("Mốc thời gian báo cáo: Giai đoạn KT1 (Từ Tuần 1 đến hết Tuần 3: 27/07/2026 - 16/08/2026)", False, 11.5)
    ]
    for text, is_bold, sz in runs_meta:
        r = p_meta.add_run(text)
        r.font.name = "Times New Roman"
        r.bold = is_bold
        r.font.size = Pt(sz)
        
    # Sections
    for sec_heading, sec_items in sections:
        if sec_heading:
            p_h = doc.add_paragraph()
            p_h.paragraph_format.space_before = Pt(16)
            p_h.paragraph_format.space_after = Pt(6)
            p_h.paragraph_format.keep_with_next = True
            r_h = p_h.add_run(sec_heading)
            r_h.font.name = "Times New Roman"
            r_h.bold = True
            r_h.font.size = Pt(14.5)
            r_h.font.color.rgb = RGBColor(0, 70, 130)
            
        for item in sec_items:
            if isinstance(item, str):
                p_item = doc.add_paragraph()
                
                is_subheading = any(item.strip().startswith(prefix) for prefix in [
                    "1.1", "1.2", "1.3", "1.4", "2.1", "2.2", "3.1", "3.2", "4.1", "4.2", "4.3", "4.4", "5.1", "5.2", "5.3", "5.4", "5.5", "KẾT LUẬN"
                ])
                
                is_toc_item = sec_heading == "MỤC LỤC TỔNG QUAN TÀI LIỆU"
                is_bullet = item.strip().startswith("- ") or item.strip().startswith("• ")
                is_numbered = len(item.strip()) > 3 and item.strip()[:2].isdigit() and item.strip()[2] in ['.', ')']
                
                if is_toc_item:
                    p_item.paragraph_format.space_after = Pt(2)
                    p_item.paragraph_format.line_spacing = 1.15
                    if item.startswith("CHƯƠNG") or item.startswith("KẾT LUẬN"):
                        p_item.paragraph_format.space_before = Pt(4)
                        r_item = p_item.add_run(item)
                        r_item.font.name = "Times New Roman"
                        r_item.bold = True
                        r_item.font.size = Pt(12)
                        r_item.font.color.rgb = RGBColor(0, 51, 102)
                    else:
                        p_item.paragraph_format.left_indent = Inches(0.2)
                        r_item = p_item.add_run(item)
                        r_item.font.name = "Times New Roman"
                        r_item.font.size = Pt(11.5)
                        r_item.font.color.rgb = RGBColor(51, 65, 85)
                elif is_subheading:
                    p_item.paragraph_format.space_before = Pt(10)
                    p_item.paragraph_format.space_after = Pt(4)
                    p_item.paragraph_format.keep_with_next = True
                    r_item = p_item.add_run(item)
                    r_item.font.name = "Times New Roman"
                    r_item.bold = True
                    r_item.font.size = Pt(13.5)
                    r_item.font.color.rgb = RGBColor(0, 51, 102)
                elif is_bullet or is_numbered:
                    p_item.paragraph_format.left_indent = Inches(0.25)
                    p_item.paragraph_format.space_after = Pt(4)
                    p_item.paragraph_format.line_spacing = 1.25
                    
                    if ":" in item and len(item.split(":")[0]) < 60:
                        parts = item.split(":", 1)
                        r1 = p_item.add_run(parts[0] + ":")
                        r1.font.name = "Times New Roman"
                        r1.bold = True
                        r1.font.size = Pt(13)
                        
                        r2 = p_item.add_run(parts[1])
                        r2.font.name = "Times New Roman"
                        r2.font.size = Pt(13)
                    else:
                        r_item = p_item.add_run(item)
                        r_item.font.name = "Times New Roman"
                        r_item.font.size = Pt(13)
                else:
                    p_item.paragraph_format.space_after = Pt(6)
                    p_item.paragraph_format.line_spacing = 1.25
                    r_item = p_item.add_run(item)
                    r_item.font.name = "Times New Roman"
                    r_item.font.size = Pt(13)
                    
            elif isinstance(item, tuple) and item[0] == 'code':
                # Embedded Code Box in Word with Consolas Monospace Font
                file_title, code_str = item[1], item[2]
                
                p_c_title = doc.add_paragraph()
                p_c_title.paragraph_format.space_before = Pt(8)
                p_c_title.paragraph_format.space_after = Pt(2)
                p_c_title.paragraph_format.keep_with_next = True
                r_ct = p_c_title.add_run(f"📌 MÃ NGUỒN BIÊN DỊCH PLANTUML (Sao chép để xuất ảnh): {file_title}")
                r_ct.font.name = "Times New Roman"
                r_ct.bold = True
                r_ct.font.size = Pt(11.5)
                r_ct.font.color.rgb = RGBColor(0, 70, 130)
                
                tbl = doc.add_table(rows=1, cols=1)
                tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
                tbl.style = 'Table Grid'
                cell = tbl.cell(0, 0)
                set_cell_shading(cell, "F1F5F9")
                set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
                
                p_code = cell.paragraphs[0]
                p_code.paragraph_format.space_before = Pt(2)
                p_code.paragraph_format.space_after = Pt(2)
                p_code.paragraph_format.line_spacing = 1.15
                r_c = p_code.add_run(code_str)
                r_c.font.name = "Consolas"
                r_c.font.size = Pt(9.0)
                r_c.font.color.rgb = RGBColor(15, 23, 42)
                
                doc.add_paragraph()
                
            elif isinstance(item, tuple) and item[0] == 'table':
                headers, rows = item[1], item[2]
                table = doc.add_table(rows=1, cols=len(headers))
                table.alignment = WD_TABLE_ALIGNMENT.CENTER
                table.style = 'Table Grid'
                
                # Header Row
                hdr_cells = table.rows[0].cells
                for idx, heading in enumerate(headers):
                    hdr_cells[idx].text = heading
                    set_cell_shading(hdr_cells[idx], "EBF3FA")
                    set_cell_margins(hdr_cells[idx], top=120, bottom=120, left=150, right=150)
                    for p in hdr_cells[idx].paragraphs:
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p.paragraph_format.space_before = Pt(2)
                        p.paragraph_format.space_after = Pt(2)
                        for r in p.runs:
                            r.font.name = "Times New Roman"
                            r.bold = True
                            r.font.size = Pt(12)
                            r.font.color.rgb = RGBColor(0, 51, 102)
                            
                # Data Rows
                for row_idx, row_data in enumerate(rows):
                    row_cells = table.add_row().cells
                    for idx, cell_value in enumerate(row_data):
                        val_str = str(cell_value)
                        set_cell_margins(row_cells[idx], top=100, bottom=100, left=140, right=140)
                        
                        cell_paras = val_str.split("\n")
                        p0 = row_cells[idx].paragraphs[0]
                        
                        is_short_col = len(val_str) < 15 and ("FR-" in val_str or "NFR-" in val_str or "UC" in val_str or val_str.isdigit() or "Tuần" in val_str or "%" in val_str)
                        
                        for p_idx, para_text in enumerate(cell_paras):
                            p = row_cells[idx].add_paragraph() if p_idx > 0 else p0
                            p.paragraph_format.space_before = Pt(2)
                            p.paragraph_format.space_after = Pt(2)
                            p.paragraph_format.line_spacing = 1.15
                            
                            if is_short_col and idx in [0, 1, 3]:
                                 p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                            else:
                                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                                
                            if any(para_text.strip().startswith(kw) for kw in ["Input:", "Output:", "FR-", "NFR-", "UC-", "Must Have", "Should Have", "Could Have", "Won't Have", "1.", "2.", "3.", "4.", "5.", "6.", "Test Method:", "Acceptance:"]):
                                if ":" in para_text:
                                    parts = para_text.split(":", 1)
                                    r1 = p.add_run(parts[0] + ":")
                                    r1.font.name = "Times New Roman"
                                    r1.bold = True
                                    r1.font.size = Pt(11.5)
                                    
                                    r2 = p.add_run(parts[1])
                                    r2.font.name = "Times New Roman"
                                    r2.font.size = Pt(11.5)
                                else:
                                    r = p.add_run(para_text)
                                    r.font.name = "Times New Roman"
                                    if any(k in para_text for k in ["FR-", "NFR-", "UC-", "Must Have", "Should Have", "Ban Chủ nhiệm", "Trưởng ban", "Thành viên", "Google Gemini", "Local Rule-based", "Database Subsystem", "PostgreSQL", "Flask", "Docker"]):
                                        r.bold = True
                                    r.font.size = Pt(11.5)
                            else:
                                r = p.add_run(para_text)
                                r.font.name = "Times New Roman"
                                r.font.size = Pt(11.5)
                                
                doc.add_paragraph()
                
    docx_file_path = os.path.join(docs_dir, file_name)
    try:
        doc.save(docx_file_path)
        print(f"SUCCESSFULLY GENERATED DOCX WITH TOC & EMBEDDED CODES: {docx_file_path}")
    except PermissionError:
        alt_path = os.path.join(docs_dir, file_name.replace(".docx", "_updated.docx"))
        doc.save(alt_path)
        print(f"[Warning] File {docx_file_path} is open in Word. Saved to {alt_path}")

docx_file_name = "08_KhaoSat_PhanTich_YeuCau_ChucNang_PhiChucNang.docx"
docx_title = "BÁO CÁO KHẢO SÁT VÀ PHÂN TÍCH YÊU CẦU CỦA ỨNG DỤNG\n(GIAI ĐOẠN KT1: TỪ TUẦN 1 ĐẾN HẾT TUẦN 3)\nYÊU CẦU CHỨC NĂNG VÀ YÊU CẦU PHI CHỨC NĂNG"
generate_docx(docx_file_name, docx_title, p8_sections_kt1)
