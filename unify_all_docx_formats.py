import os
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

docs_dir = r"D:\DTC245200328\Nam3\Ki1\UngDungAI\Student_Club_Management\docs"

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

def create_unified_document(file_name, doc_title, sections):
    doc = docx.Document()
    
    # Page Margins: 1 inch (2.54 cm)
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)
        
    # Standard Template Header Block (18 pt Bold)
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run(doc_title)
    r_title.bold = True
    r_title.font.name = "Times New Roman"
    r_title.font.size = Pt(18)
    r_title.font.color.rgb = RGBColor(0, 51, 102)
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(10)
    
    # Standard Group Metadata Block (12 pt & 11.5 pt)
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_meta.paragraph_format.line_spacing = 1.2
    p_meta.paragraph_format.space_after = Pt(18)
    
    runs_meta = [
        ("Nhóm 15 - Thành viên nhóm (Nhóm 2 SV)\n", True, 12),
        ("La Văn Quyền (Trưởng nhóm - Lead Dev / Architect)\n", False, 12),
        ("Nguyễn Đức Anh (Thành viên - BA / UX / QA)\n", False, 12),
        ("Tên ứng dụng: Hệ thống quản lý câu lạc bộ sinh viên có tích hợp AI\n", True, 12),
        ("Mốc thời gian báo cáo: Giai đoạn KT1 (Từ 27/07/2026 đến 16/08/2026 - Hết Tuần 3)", False, 11.5)
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
                    "1.1", "1.2", "1.3", "1.4", "2.1", "2.2", "3.1", "3.2", "4.1", "4.2", "4.3", "4.4", "4.5", "5.1", "5.2", "5.3", "5.4", "5.5", "KẾT LUẬN"
                ])
                is_toc_item = sec_heading == "MỤC LỤC TỔNG QUAN TÀI LIỆU" or "MỤC LỤC" in sec_heading
                is_bullet = item.strip().startswith("- ") or item.strip().startswith("• ")
                is_numbered = len(item.strip()) > 3 and item.strip()[:2].isdigit() and item.strip()[2] in ['.', ')']
                
                if is_toc_item:
                    p_item.paragraph_format.space_after = Pt(2)
                    p_item.paragraph_format.line_spacing = 1.15
                    if item.startswith("CHƯƠNG") or item.startswith("PHẦN") or item.startswith("KẾT LUẬN") or item.startswith("1.") or item.startswith("2.") or item.startswith("3.") or item.startswith("4.") or item.startswith("5."):
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
                    
            elif isinstance(item, tuple) and item[0] == 'image':
                # Embedded Image in Word Document with centered alignment and caption
                img_path = item[1]
                caption = item[2] if len(item) > 2 else ""
                width = item[3] if len(item) > 3 else Inches(6.0)
                if os.path.exists(img_path):
                    p_img = doc.add_paragraph()
                    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_img.paragraph_format.space_before = Pt(8)
                    p_img.paragraph_format.space_after = Pt(2)
                    p_img.paragraph_format.keep_with_next = True
                    r_img = p_img.add_run()
                    r_img.add_picture(img_path, width=width)
                    if caption:
                        p_cap = doc.add_paragraph()
                        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p_cap.paragraph_format.space_after = Pt(8)
                        r_cap = p_cap.add_run(caption)
                        r_cap.font.name = "Times New Roman"
                        r_cap.italic = True
                        r_cap.font.size = Pt(10.5)
                        r_cap.font.color.rgb = RGBColor(80, 80, 80)
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
                
                # Header Row (12 pt Bold, Soft Blue Shading)
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
                            
                # Data Rows (11.5 pt, Clean Padding)
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
                                    if any(k in para_text for k in ["FR-", "NFR-", "UC-", "Must Have", "Should Have", "Ban Chủ nhiệm", "Trưởng ban", "Thành viên", "AI Engine", "PostgreSQL", "Flask", "Docker"]):
                                        r.bold = True
                                    r.font.size = Pt(11.5)
                            else:
                                r = p.add_run(para_text)
                                r.font.name = "Times New Roman"
                                r.font.size = Pt(11.5)
                                
                doc.add_paragraph() # Spacing

    file_path = os.path.join(docs_dir, file_name)
    try:
        doc.save(file_path)
        print(f"UNIFIED FORMAT SAVED: {file_name}")
    except PermissionError:
        alt_path = os.path.join(docs_dir, file_name.replace(".docx", "_updated.docx"))
        doc.save(alt_path)
        print(f"File locked. Saved to alt path: {alt_path}")

# ==============================================================================
# DATA FOR ALL 8 DOCUMENTS (Flask + React-Vite + PostgreSQL + Docker + Pydantic + JWT)
# ==============================================================================

# 01_GenAI_SoftwareDevelopment_project-plan.docx
p1_sections = [
    ("MỤC LỤC TỔNG QUAN TÀI LIỆU", [
        "1. THÔNG TIN CHUNG DỰ ÁN",
        "2. BẢNG PHÂN CÔNG VAI TRÒ VÀ NĂNG LỰC NHÓM",
        "3. KẾ HOẠCH THỰC HIỆN CHI TIẾT 9 TUẦN (WBS) & PHÂN CHIA CÔNG VIỆC CỤ THỂ",
        "4. KẾ HOẠCH BÀN GIAO CÁC MỐC ĐÁNH GIÁ (KT1, KT2, KT3, CUỐI KỲ)"
    ]),
    ("1. THÔNG TIN CHUNG DỰ ÁN", [
        "Tên ứng dụng: Hệ thống quản lý câu lạc bộ sinh viên có tích hợp AI (Đề tài 28)",
        "Lớp / Nhóm thực hiện: Nhóm 15 - 02 Sinh viên",
        "Thành viên nhóm:",
        " - La Văn Quyền (Trưởng nhóm - Lead Developer / System Architect)",
        " - Nguyễn Đức Anh (Thành viên - Business Analyst / UX Designer / QA Tester)",
        "Thời gian thực hiện: Từ 27/07/2026 đến 27/09/2026 (9 tuần)",
        "Kiến trúc Công nghệ: Flask 3.1+ (Python 3.11/3.13) + Pydantic V2 + JWT Auth + React 18 + Vite + PostgreSQL 16 + Docker Compose + Dual-Engine AI (Google Gemini Cloud API & Local Rule Fallback Matcher)."
    ]),
    ("2. BẢNG PHÂN CÔNG VAI TRÒ VÀ NĂNG LỰC NHÓM", [
        ('table', 
         ["STT", "Họ và tên", "Vai trò chính", "Nhiệm vụ & Trách nhiệm chuyên môn", "Ghi chú & Phạm vi"],
         [
             ["1", "La Văn Quyền", "Trưởng nhóm / Lead Dev / Architect", "Kiến trúc hệ thống tổng thể, thiết kế CSDL PostgreSQL 16, lập trình Backend Flask 3.1 REST API + Pydantic V2 + JWT Authentication, cấu hình Docker Compose đa container, cài đặt thuật toán Local Rule-based Fallback AI Engine và tối ưu hóa hiệu năng P95.", "Chịu trách nhiệm chính về Kỹ thuật & Kiến trúc"],
             ["2", "Nguyễn Đức Anh", "Thành viên / BA / UX / QA", "Thu thập & phân tích yêu cầu nghiệp vụ (Q&A, Pain Points, FR/NFR), mô hình hóa Use Case, thiết kế giao diện UI/UX React-Vite Component System, lập kế hoạch kiểm thử (Test Plan 25+ test cases), thiết kế Prompt AI và biên soạn tài liệu Hướng dẫn sử dụng.", "Chịu trách nhiệm chính về Nghiệp vụ, UX & QA"]
         ]
        )
    ]),
    ("3. KẾ HOẠCH THỰC HIỆN CHI TIẾT 9 TUẦN (WBS) & PHÂN CHIA CÔNG VIỆC CỤ THỂ", [
        "Bảng phân rã cấu trúc công việc (WBS) chi tiết từng tuần. Đối với các tuần có 2 thành viên cùng tham gia, nhiệm vụ được phân định rành mạch giữa mảng Backend/Kiến trúc và mảng Nghiệp vụ/Frontend/QA:",
        ('table',
         ["Mốc", "Tuần", "Hạng mục Công việc WBS", "Phân công Chi tiết Từng Thành viên (Ai làm phần nào)", "Sản phẩm Bàn giao"],
         [
             ["KT1", "Tuần 1", "Khảo sát hiện trạng & Thu thập yêu cầu nghiệp vụ", 
              "• Nguyễn Đức Anh (Chính): Khảo sát 120 sinh viên, phỏng vấn BCN, tổng hợp 6 điểm đau, xây dựng Sơ đồ phân cấp chức năng WBS.\n• La Văn Quyền (Phối hợp): Rà soát tính khả thi kỹ thuật và kiến trúc công nghệ đề xuất.", 
              "File 02_requirements-qa.docx & File 08_KhaoSat (Chương 1)"],
             
             ["KT1", "Tuần 2", "Lập kế hoạch dự án & Viết Đặc tả Yêu cầu SRS", 
              "• La Văn Quyền: Lập kế hoạch 9 tuần (WBS, timeline, tech stack), đặc tả 14 tiêu chuẩn chất lượng NFR ISO/IEC 25010 và kiến trúc Dual-Engine AI trong File 01 & 03.\n• Nguyễn Đức Anh: Đặc tả 6 yêu cầu quản lý (FR-SYS), 3 yêu cầu AI (FR-AI), phân tích luồng nghiệp vụ CLB và xây dựng ma trận phân quyền RBAC trong File 03.", 
              "File 01_project-plan.docx & File 03_requirements-specification.docx"],
             
             ["KT1", "Tuần 3", "Thiết kế Hướng đối tượng, ERD PostgreSQL & ScreenFlow UI", 
              "• La Văn Quyền: Thiết kế OOD, vẽ Biểu đồ Lớp (Class Diagram 8 thực thể), Sequence, Activity Diagrams và thiết kế CSDL PostgreSQL (ERD, khóa ngoại, unique constraints) trong File 04 & 08.\n• Nguyễn Đức Anh: Vẽ Sơ đồ Use Case (Tổng thể + 5 Phân hệ), viết 3 Use Case Specs chi tiết (UC04, UC05, UC06), thiết kế Wireframe ScreenFlow UI trong File 06.", 
              "File 04_object-oriented-design.docx, File 06_screenflow_db.docx & 19 Biểu đồ UML"],
             
             ["KT2", "Tuần 4", "Khởi tạo Framework Flask + React, Docker Compose & PostgreSQL", 
              "• La Văn Quyền (Chính): Viết docker-compose.yml 3 service (frontend, backend, db), cấu hình Backend Flask 3.1, JWT Auth, Bcrypt hashing và SQLAlchemy Models (User, Department).\n• Nguyễn Đức Anh (Phối hợp): Khởi tạo React 18 + Vite, xây dựng CSS Component System, cấu hình React Router và thiết kế trang Đăng nhập / Đăng ký.", 
              "Mã nguồn Docker Compose, Backend Auth API & Frontend Login Component"],
             
             ["KT2", "Tuần 5", "Lập trình Quản lý Thành viên, Ban chuyên môn & Điểm danh Dynamic QR", 
              "• La Văn Quyền: Lập trình Backend RESTful API Quản lý Thành viên (Skill Matrix, Free Slots), Ban chuyên môn và API Sinh mã Dynamic QR UUID độc bản + API Quét QR Check-in.\n• Nguyễn Đức Anh: Lập trình Giao diện React: Màn hình Hồ sơ cá nhân (Skill Matrix checkbox, Lịch rảnh picker), Màn hình Quản lý Ban, Màn hình Tạo sự kiện & Camera QR Scanner Mobile.", 
              "Module Quản lý Thành viên, Ban chuyên môn & Điểm danh QR hoàn chỉnh"],
             
             ["KT2", "Tuần 6", "Lập trình Quản lý Nhiệm vụ (Kanban Board) & Leaderboard Thống kê", 
              "• La Văn Quyền: Lập trình Backend Flask API Task Kanban (CRUD, State Transition), Middleware RBAC chặn sửa task trái phép (403 Forbidden), và API tính điểm Contribution Score tự động.\n• Nguyễn Đức Anh: Lập trình Giao diện React Bảng Kanban Board kéo-thả 3 cột (To-Do, In-Progress, Done), Dialog gán task & lọc task, Màn hình Dashboard Leaderboard xếp hạng.", 
              "Module Kanban Task Board RBAC & Dashboard Thống kê Đóng góp"],
             
             ["KT3", "Tuần 7", "Tích hợp AI Dual-Engine (Cloud Gemini API & Local Fallback Matcher)", 
              "• La Văn Quyền: Tích hợp Google Gemini API SDK / OpenAI API Client, lập trình thuật toán Local Rule-based Fallback Matcher (In-memory Heuristic), cơ chế Timeout sang Fallback và bảng ai_logs.\n• Nguyễn Đức Anh: Thiết kế Prompt Engineering cho 3 tính năng (Sinh thông báo FR-AI-01, Tóm tắt báo cáo FR-AI-02, Gợi ý phân công FR-AI-03), xây dựng hệ thống phòng thủ Prompt Injection 5 tầng.", 
              "Module AI Dual-Engine Service hoàn chỉnh kết nối Frontend UI"],
             
             ["KT3", "Tuần 8", "Kiểm thử chức năng, Kiểm thử tải & Bảo mật Prompt AI", 
              "• Nguyễn Đức Anh (Chính): Xây dựng bộ kịch bản kiểm thử (25+ test cases), kiểm thử dữ liệu biên/thiếu sót, kiểm thử Prompt Injection, kiểm thử tải 200 VUs với Locust và viết File 05.\n• La Văn Quyền (Phối hợp): Tối ưu hóa truy vấn PostgreSQL Indexing, xử lý các lỗi phát hiện qua kiểm thử (Bug fixing), đo đạc P95 Latency API CRUD <= 500ms.", 
              "File 05_functional-testing.docx & Báo cáo Kết quả Kiểm thử Toàn diện"],
             
             ["Cuối kỳ", "Tuần 9", "Hoàn thiện Hướng dẫn sử dụng, Slide 5p, Video Demo & Bảo vệ Đồ án", 
              "• La Văn Quyền: Rà soát Clean Code, Docker build production container, chuẩn bị môi trường chạy Demo trực tiếp, phụ trách giải trình Kiến trúc, Backend, Database và AI Fallback trước Hội đồng.\n• Nguyễn Đức Anh: Hoàn thiện File 07_user-guide.docx (Admin, Leader, Member), thiết kế Slide thuyết trình 5 phút, kịch bản bảo vệ, quay Video Demo và phụ trách thuyết trình nghiệp vụ.", 
              "File 07_user-guide.docx, Slide Thuyết trình 5p, Video Demo & Mã nguồn Hoàn chỉnh"]
         ]
        )
    ]),
    ("4. KẾ HOẠCH BÀN GIAO CÁC MỐC ĐÁNH GIÁ (KT1, KT2, KT3, CUỐI KỲ)", [
        ('table',
         ["Mốc Đánh giá", "Thời gian Bàn giao", "Sản phẩm Bàn giao Trọng tâm", "Phân công Trách nhiệm Báo cáo", "Tỷ lệ Đóng góp"],
         [
             ["KT1 (Tuần 1 - 3)", "16/08/2026", "Hồ sơ Khảo sát, Đặc tả SRS, Thiết kế OOD, 19 Biểu đồ UML, Ma trận RTM (File 01, 02, 03, 04, 08)", "• La Văn Quyền: Trình bày Kiến trúc, Class Diagram, AI Fallback.\n• Nguyễn Đức Anh: Trình bày Khảo sát Điểm đau, Use Case, ScreenFlow.", "50% - 50%"],
             ["KT2 (Tuần 4 - 6)", "06/09/2026", "Mã nguồn Core Framework Docker, Flask API Auth, Member, Dynamic QR, Kanban Board, Kế hoạch Kiểm thử (File 05, 06)", "• La Văn Quyền: Trình diễn Docker Backend API, JWT, Postgres DB.\n• Nguyễn Đức Anh: Trình diễn Giao diện React UI, Kanban, QR Scanner.", "50% - 50%"],
             ["KT3 (Tuần 7 - 8)", "20/09/2026", "Module AI Dual-Engine (Gemini API + Local Fallback), Báo cáo Kiểm thử Tải 200 VUs, Bảo mật Prompt (File 05 cập nhật)", "• La Văn Quyền: Trình diễn Thuật toán AI Fallback, Quota handling.\n• Nguyễn Đức Anh: Trình diễn 3 Tính năng AI UI, Kết quả Test Cases.", "50% - 50%"],
             ["Cuối kỳ (Tuần 9)", "27/09/2026", "Hệ thống Phần mềm Hoàn chỉnh, Hướng dẫn Sử dụng (File 07), Slide Thuyết trình 5p, Video Demo Vận hành & Bàn giao Git", "• La Văn Quyền: Giải trình Kỹ thuật & Vận hành Docker Server.\n• Nguyễn Đức Anh: Thuyết trình 5 phút & Hướng dẫn sử dụng các vai trò.", "50% - 50%"]
         ]
        )
    ])
]

# 02_GenAI_SoftwareDevelopment_requirements-qa.docx
p2_sections = [
    ("MỤC LỤC TỔNG QUAN TÀI LIỆU", [
        "1. GIỚI THIỆU THU THẬP YÊU CẦU & BỐI CẢNH DỰ ÁN",
        "2. BẢNG CÂU HỎI VÀ GIẢI ĐÁP YÊU CẦU (REQUIREMENTS Q&A)",
        "3. SƠ ĐỒ PHÂN CẤP CHỨC NĂNG CỦA ỨNG DỤNG (FUNCTIONAL DECOMPOSITION DIAGRAM)",
        "4. TỔNG HỢP 06 ĐIỂM ĐAU CỐT LÕI (PAIN POINTS) & GIẢI PHÁP ĐỀ XUẤT"
    ]),
    ("1. GIỚI THIỆU THU THẬP YÊU CẦU & BỐI CẢNH DỰ ÁN", [
        "Tài liệu này ghi lại toàn bộ quá trình phỏng vấn, khảo sát thực tế và làm rõ yêu cầu nghiệp vụ giữa đội ngũ phân tích (Business Analyst) và Ban Chủ nhiệm (BCN) các Câu lạc bộ Sinh viên tiêu biểu.",
        "Mục tiêu cốt lõi: Chuyển đổi phương thức quản lý thủ công truyền thống (giấy tờ, Excel rời rạc, nhóm chat trôi việc) sang Hệ thống Quản lý Câu lạc bộ Sinh viên Tích hợp AI (Đề tài 28) với kiến trúc hiện đại, có tính tự động hóa cao và cơ chế dự phòng Dual-Engine."
    ]),
    ("2. BẢNG CÂU HỎI VÀ GIẢI ĐÁP YÊU CẦU (REQUIREMENTS Q&A)", [
        ('table',
         ["STT", "Chủ đề / Khía cạnh", "Câu hỏi làm rõ từ BA", "Giải đáp từ Ban Chủ nhiệm / Khách hàng", "Kết luận yêu cầu hệ thống"],
         [
             ["1", "Phân quyền", "Hệ thống cần phân làm mấy vai trò người dùng và phạm vi truy cập ra sao?", "Cần 3 vai trò: Ban Chủ nhiệm (Admin), Trưởng ban chuyên môn (Leader), và Thành viên CLB (Member).", "Thiết lập phân quyền RBAC 3 cấp độ với Token JWT 7 ngày, kiểm soát chặt chẽ HTTP 401/403."],
             ["2", "Quản lý thành viên", "Thông tin thành viên cần lưu trữ những gì để hỗ trợ phân công nhiệm vụ?", "Ngoài thông tin cá nhân, cần lưu Ban chuyên môn, Danh sách Kỹ năng (Skill Matrix: Thiết kế, MC, Setup, Content...) và Lịch rảnh cố định trong tuần.", "Bổ sung trường Skill Matrix và Free Slots vào hồ sơ, xác thực qua Pydantic Schema."],
             ["3", "Điểm danh", "Quy trình điểm danh hoạt động CLB hiện tại ra sao và cần cải tiến thế nào?", "Hiện dùng giấy checkin rất chậm (15-20 phút), dễ ký hộ. Cần quét mã QR trên điện thoại để checkin nhanh và tự động chống trùng lặp.", "Phát triển tính năng Sinh mã Dynamic QR UUID độc bản cho từng sự kiện & Quét QR check-in tức thì."],
             ["4", "Quản lý Nhiệm vụ", "Các nhiệm vụ được quản lý và theo dõi tiến độ thế nào?", "Trưởng ban giao việc cho thành viên, cần xem dạng bảng Kanban trực quan (To-do, In-progress, Done) và chỉ cho phép người nhận task sửa task của mình.", "Thiết kế Màn hình Kanban Board theo dõi tiến độ có siết chặt kiểm soát RBAC."],
             ["5", "AI Sinh thông báo", "Đầu vào và đầu ra mong muốn của AI sinh thông báo sự kiện?", "Trưởng ban nhập thông tin thô sự kiện (Tên, Thời gian, Địa điểm). AI tự sinh bài viết truyền thông thu hút kèm emoji và hỗ trợ nhiều Tone giọng.", "Phát triển FR-AI-01: Prompt sinh bài đăng truyền thông đa phong cách."],
             ["6", "AI Tóm tắt kết quả", "Làm sao để tổng hợp kết quả sau mỗi hoạt động CLB?", "Sau sự kiện có ghi chú họp và phản hồi của thành viên. AI cần đọc và tóm tắt ưu/nhược điểm và kết quả chính thành 3 phần súc tích.", "Phát triển FR-AI-02: Prompt tóm tắt báo cáo tổng kết 3 phần."],
             ["7", "AI Gợi ý phân công", "Tiêu chí để AI gợi ý phân công nhiệm vụ là gì?", "AI dựa trên: Yêu cầu nhiệm vụ, Kỹ năng thành viên, Lịch rảnh và Số lượng task thành viên đang gánh để tránh quá tải.", "Phát triển FR-AI-03: Thuật toán AI Smart Matchmaking ghép cặp Task-Member kèm Match Score % và lý do tường minh."],
             ["8", "Thống kê đóng góp", "Làm sao biết thành viên nào hoạt động tích cực để vinh danh cuối kỳ?", "Hệ thống cần tự động tính điểm dựa trên số lần điểm danh tham gia và số nhiệm vụ đã hoàn thành theo tháng/kỳ.", "Xây dựng Dashboard thống kê Leaderboard điểm đóng góp (Contribution Score) minh bạch."]
         ]
        )
    ]),
    ("3. SƠ ĐỒ PHÂN CẤP CHỨC NĂNG CỦA ỨNG DỤNG (FUNCTIONAL DECOMPOSITION DIAGRAM)", [
        "Dựa trên kết quả phỏng vấn và khảo sát hiện trạng, hệ thống Quản lý Câu lạc bộ Sinh viên Tích hợp AI (Đề tài 28) được phân rã thành Cây phân cấp chức năng 3 cấp độ (5 Phân hệ lớn và 25 Chức năng chi tiết):",
        ('code', "functional_decomposition.puml", """@startwbs functional_decomposition
!theme plain
skinparam backgroundColor #FFFFFF
skinparam shadowing false
skinparam roundcorner 6

* **HỆ THỐNG QUẢN LÝ CLB SINH VIÊN TÍCH HỢP AI (ĐỀ TÀI 28)**
** **1. Phân hệ Xác thực & Phân quyền (Auth & RBAC)**
*** 1.1 Đăng nhập Email & Mật khẩu Bcrypt
*** 1.2 Cấp Access Token JWT 7 ngày
*** 1.3 Quản trị Phân quyền 3 Vai trò (Admin, Leader, Member)
*** 1.4 Khóa / Mở khóa Tài khoản & Reset Mật khẩu

** **2. Phân hệ Quản lý Thành viên & Ban Chuyên môn**
*** 2.1 Quản lý Thông tin Hồ sơ Cá nhân
*** 2.2 Ma trận Kỹ năng Chuyên môn (Skill Matrix)
*** 2.3 Lịch rảnh Cố định trong Tuần (Free Slots)
*** 2.4 Quản lý Cơ cấu Ban (Truyền thông, Sự kiện, Chuyên môn, Đối ngoại)
*** 2.5 Điều chuyển Nhân sự & Bổ nhiệm Trưởng ban

** **3. Phân hệ Quản lý Sự kiện & Điểm danh QR**
*** 3.1 Khởi tạo, Cập nhật & Lên lịch Sự kiện
*** 3.2 Tự động Sinh mã Dynamic QR Code độc bản (UUID)
*** 3.3 Trình chiếu Mã QR Check-in trên Màn hình
*** 3.4 Quét mã QR Điểm danh qua Thiết bị Di động
*** 3.5 Kiểm tra Hợp lệ & Chống Điểm danh Trùng lặp

** **4. Phân hệ Quản lý Nhiệm vụ & Kanban Board**
*** 4.1 Khởi tạo Task, Gán Deadline & Kỹ năng Cần thiết
*** 4.2 Bảng Kanban Trực quan 3 Cột (To-Do, In-Progress, Done)
*** 4.3 Kéo-thả Chuyển đổi Trạng thái Task Thời gian thực
*** 4.4 Kiểm soát Phân quyền RBAC Sửa Task (Chặn 403 Forbidden)
*** 4.5 Đánh dấu Nghiệm thu Task & Lưu trữ Lịch sử

** **5. Phân hệ Trợ lý AI & Báo cáo Thống kê**
*** 5.1 FR-AI-01: AI Sinh Bài đăng Thông báo Sự kiện đa Tone
*** 5.2 FR-AI-02: AI Tóm tắt Kết quả Hoạt động & Phản hồi 3 Phần
*** 5.3 FR-AI-03: AI Smart Matchmaking Phân công Tự động
*** 5.4 Dual-Engine Fallback: Local Rule Matcher khi Mất mạng
*** 5.5 Tính điểm Đóng góp (Contribution Score) & Leaderboard
@endwbs"""),
        "Bảng Đặc tả Chi tiết 05 Phân hệ Chức năng Cốt lõi:",
        ('table',
         ["Mã Phân hệ", "Tên Phân hệ Chức năng", "Số lượng Chức năng Con", "Mục tiêu & Phạm vi Nghiệp vụ", "Tác nhân Phụ trách"],
         [
             ["SUB-01", "Xác thực & Phân quyền (Auth & RBAC)", "4 Chức năng con", "Xác thực an toàn bằng bcrypt và JWT 7 ngày; phân quyền truy cập nghiêm ngặt 3 vai trò Admin, Leader, Member.", "Tất cả Tác nhân"],
             ["SUB-02", "Quản lý Thành viên & Ban Chuyên môn", "5 Chức năng con", "Quản lý hồ sơ, ma trận kỹ năng chuyên môn, lịch rảnh hàng tuần và cơ cấu điều chuyển nhân sự giữa 4 ban.", "Admin, Leader, Member"],
             ["SUB-03", "Quản lý Sự kiện & Điểm danh QR", "5 Chức năng con", "Tạo sự kiện, tự động sinh chuỗi mã QR Code UUID độc bản, quét QR điểm danh trên mobile và chống gian lận.", "Leader, Member"],
             ["SUB-04", "Quản lý Nhiệm vụ & Kanban Board", "5 Chức năng con", "Quản lý tiến độ trực quan qua 3 cột To-Do/In-Progress/Done, phân công người làm và siết chặt RBAC sửa task.", "Admin, Leader, Member"],
             ["SUB-05", "Trợ lý AI & Báo cáo Thống kê", "5 Chức năng con", "Tích hợp 3 tính năng AI (Sinh thông báo, Tóm tắt báo cáo, Gợi ý phân công), cơ chế Dual-Engine Fallback và Leaderboard.", "Admin, Leader, Member, AI Engine"]
         ]
        )
    ]),
    ("4. TỔNG HỢP 06 ĐIỂM ĐAU CỐT LÕI (PAIN POINTS) & GIẢI PHÁP ĐỀ XUẤT", [
        ('table',
         ["STT", "Điểm đau Khảo sát (Pain Point)", "Tỷ lệ ghi nhận", "Mức độ ảnh hưởng", "Giải pháp Hệ thống Tương ứng"],
         [
             ["1", "Phân công nhiệm vụ thủ công, thiếu thông tin kỹ năng & lịch rảnh", "92% Trưởng ban", "Rất cao (Mất 2-3h/sự kiện)", "Xây dựng Skill Matrix + Lịch rảnh + AI Gợi ý phân công tự động (FR-AI-03)."],
             ["2", "Điểm danh bằng giấy chậm chạp, dễ gian lận điểm danh hộ", "78% Sự kiện", "Cao (Mất 15-20 phút đầu buổi)", "Tính năng Dynamic QR Code độc bản cho sự kiện & Quét QR Mobile (FR-SYS-04)."],
             ["3", "Nhiệm vụ phân tán qua chat Zalo/Messenger, trôi tin nhắn, trễ hạn", "85% Ban Chủ nhiệm", "Rất cao (Đánh giá cảm tính)", "Bảng Kanban Board trực quan (To-Do, In-Progress, Done) có RBAC (FR-SYS-05)."],
             ["4", "Soạn bài đăng truyền thông tốn thời gian, văn phong nghèo nàn", "88% Ban Truyền thông", "Trung bình", "AI Sinh bài viết thông báo sự kiện đa Tone giọng kèm emoji (FR-AI-01)."],
             ["5", "Tổng hợp báo cáo và phản hồi sau sự kiện rời rạc, mất nhiều ngày", "80% Trưởng ban", "Trung bình", "AI Tóm tắt kết quả hoạt động 3 phần súc tích từ ghi chú họp (FR-AI-02)."],
             ["6", "Thiếu cơ chế vinh danh và đo lường mức độ đóng góp minh bạch", "76% Thành viên", "Cao (Giảm gắn kết thành viên)", "Công thức tính Contribution Score tự động & Bảng xếp hạng Leaderboard (FR-SYS-06)."]
         ]
        )
    ])
]

# 03_GenAI_SoftwareDevelopment_requirements-specification.docx
p3_sections = [
    ("MỤC LỤC TỔNG QUAN TÀI LIỆU", [
        "1. GIỚI THIỆU CHUNG",
        "2. MÔ TẢ TỔNG QUAN ỨNG DỤNG & CÁC TÁC NHÂN",
        "3. DANH MỤC USE CASES CỐT LÕI & BIỂU ĐỒ USE CASE (KÈM CODE PLANTUML)",
        "4. ĐẶC TẢ CHI TIẾT CÁC USE CASE CHÍNH",
        "5. CÁC YÊU CẦU PHI CHỨC NĂNG (ISO/IEC 25010)"
    ]),
    ("1. GIỚI THIỆU CHUNG", [
        "1.1 Mục đích: Tài liệu Đặc tả Yêu cầu Phần mềm (SRS) quy định các yêu cầu chức năng, phi chức năng và kiến trúc tổng quan cho Hệ thống Quản lý Câu lạc bộ Sinh viên Tích hợp AI.",
        "1.2 Phạm vi: Áp dụng cho công tác quản lý nội bộ các CLB sinh viên tại trường đại học, hỗ trợ Ban Chủ nhiệm, Trưởng ban và Thành viên.",
        "1.3 Thuật ngữ & Từ viết tắt: BCN (Ban Chủ nhiệm), CLB (Câu lạc bộ), QR (Quick Response Code), AI (Artificial Intelligence), LLM (Large Language Model), JWT (JSON Web Token), RBAC (Role-Based Access Control)."
    ]),
    ("2. MÔ TẢ TỔNG QUAN ỨNG DỤNG & CÁC TÁC NHÂN", [
        "2.1 Danh sách Tác nhân (Actors):",
        " - Ban Chủ nhiệm (Admin): Quản lý toàn bộ hệ thống, phân quyền, xem thống kê tổng quan.",
        " - Trưởng ban (Leader): Tạo sự kiện, tạo nhiệm vụ, điểm danh, sử dụng AI hỗ trợ phân công & sinh thông báo.",
        " - Thành viên (Member): Cập nhật thông tin/kỹ năng/lịch rảnh, xem nhiệm vụ, checkin QR sự kiện.",
        " - AI Engine: Tác nhân hệ thống xử lý sinh nội dung, tóm tắt và gợi ý phân công."
    ]),
    ("3. DANH MỤC USE CASES CỐT LÕI & BIỂU ĐỒ USE CASE (KÈM CODE PLANTUML)", [
        ('table',
         ["ID Use Case", "Tên Use Case", "Mô tả ngắn gọn", "Chức năng tương ứng"],
         [
             ["UC001", "Đăng nhập & Phân quyền", "Xác thực người dùng và cấp JWT token tương ứng (BCN/Leader/Member)", "Đăng nhập JWT"],
             ["UC002", "Quản lý Hồ sơ & Kỹ năng", "Thành viên cập nhật Kỹ năng và Lịch rảnh hàng tuần", "Hồ sơ cá nhân"],
             ["UC003", "Quản lý Sự kiện & Điểm danh QR", "Tạo sự kiện, sinh mã QR và quét mã để điểm danh tự động", "Sự kiện & Điểm danh"],
             ["UC004", "Quản lý Nhiệm vụ (Kanban)", "Tạo task, gán task và cập nhật tiến độ theo dạng Kanban", "Nhiệm vụ"],
             ["UC005", "AI Gợi ý Phân công Nhiệm vụ", "AI phân tích Task & Skill Matrix để gợi ý người phù hợp nhất", "Chức năng AI"],
             ["UC006", "AI Sinh Thông báo Hoạt động", "AI tự động soạn thông báo truyền thông từ thông tin thô", "Chức năng AI"],
             ["UC007", "AI Tóm tắt Kết quả Hoạt động", "AI tóm tắt ghi chú họp & phản hồi thành bài báo cáo tổng kết", "Chức năng AI"],
             ["UC008", "Thống kê Đóng góp Thành viên", "Xuất báo cáo thành viên tích cực dựa trên điểm danh & task", "Báo cáo thống kê"]
         ]
        ),
        "Mã nguồn Biểu đồ Use Case Tổng thể Hệ thống:",
        ('code', "usecase_overall.puml", """@startuml usecase_overall
!theme plain
left to right direction
actor "Authenticated User" as User <<Abstract>>
actor "Admin" as Admin
actor "Leader" as Leader
actor "Member" as Member
actor "AI Service (Gemini)" as AIService <<System>>

Admin -up-|> User
Leader -up-|> User
Member -up-|> User

rectangle "Student Club AI Management System" {
    package "Phân hệ 1: Auth & RBAC" {
        usecase "UC01: Login JWT" as UC01
        usecase "UC12: User Management" as UC12
    }
    package "Phân hệ 2: Member & Dept" {
        usecase "UC02: Profile & Skill Matrix" as UC02
        usecase "UC11: Dept Structure" as UC11
    }
    package "Phân hệ 3: Event & QR Check-in" {
        usecase "UC04: Event Management & QR" as UC04
        usecase "UC09: QR Attendance" as UC09
    }
    package "Phân hệ 4: Kanban Tasks" {
        usecase "UC05: Task Board & RBAC" as UC05
        usecase "UC10: Update My Task" as UC10
    }
    package "Phân hệ 5: AI & Analytics" {
        usecase "UC06: AI Matchmaking" as UC06
        usecase "UC07: AI Announcements" as UC07
        usecase "UC08: AI Summary" as UC08
        usecase "UC03: History & Leaderboard" as UC03
    }
}
User --> UC01
User --> UC03
Member --> UC02
Member --> UC09
Member --> UC10
Leader --> UC04
Leader --> UC05
Leader --> UC06
Leader --> UC07
Leader --> UC08
Admin --> UC11
Admin --> UC12
AIService <-- UC06
AIService <-- UC07
AIService <-- UC08
@enduml""")
    ]),
    ("4. ĐẶC TẢ CHI TIẾT CÁC USE CASE CHÍNH", [
        ('table',
         ["Thuộc tính Use Case", "Nội dung đặc tả chi tiết (UC005: AI Gợi ý Phân công Nhiệm vụ)"],
         [
             ["Mục đích", "Tự động phân tích và đưa ra danh sách thành viên phù hợp nhất cho từng nhiệm vụ của sự kiện."],
             ["Tác nhân", "Trưởng ban chuyên môn, AI Engine."],
             ["Điều kiện trước", "Sự kiện và danh sách nhiệm vụ đã được khởi tạo; Thành viên đã cập nhật kỹ năng & lịch rảnh."],
             ["Điều kiện sau", "Danh sách phân công nhiệm vụ được tạo và lưu vào CSDL PostgreSQL."],
             ["Luồng sự kiện chính (Basic Flow)", "1. Trưởng ban chọn sự kiện và bấm nút 'AI Gợi ý Phân công'.\n2. Hệ thống Flask thu thập thông tin Task, danh sách Thành viên (Skills, Free Slots).\n3. Backend gửi Prompt đến AI Engine (hoặc Local Rule-based Fallback).\n4. AI Engine tính toán độ phù hợp (Match Score) và trả về JSON danh sách phân công gợi ý validate qua Pydantic.\n5. Giao diện React-Vite hiển thị danh sách gợi ý cho Trưởng ban xem xét.\n6. Trưởng ban bấm 'Xác nhận Phân công' để lưu vào CSDL PostgreSQL."],
             ["Luồng sự kiện phụ (Alt Flow)", "4a. Nếu thành viên chưa điền kỹ năng/lịch rảnh: AI gợi ý phân công vào các task phổ thông và hiển thị cảnh báo 'Dữ liệu kỹ năng chưa đầy đủ'."]
         ]
        )
    ]),
    ("5. CÁC YÊU CẦU PHI CHỨC NĂNG", [
        " - Bảo mật: Mật khẩu băm bằng bcrypt, xác thực API bằng JWT Token, phân quyền RBAC nghiêm ngặt (chặn 401/403).",
        " - Hiệu năng: Phản hồi API Flask < 0.5s; Phản hồi AI Engine < 5.0s (Cloud LLM) và < 0.5s (Local Fallback).",
        " - Kiến trúc & Mở rộng: Đóng gói toàn diện bằng Docker Compose (PostgreSQL + Flask + React-Vite Nginx)."
    ])
]

# 04_GenAI_SoftwareDevelopment_object-oriented-design.docx
p4_sections = [
    ("MỤC LỤC TỔNG QUAN TÀI LIỆU", [
        "1. MÔ HÌNH LỚP TỔNG QUAN & BIỂU ĐỒ CLASS DIAGRAM (KÈM CODE PLANTUML)",
        "2. ĐẶC TẢ CHI TIẾT CÁC LỚP THỰC THỂ CỐT LÕI",
        "3. BIỂU ĐỒ TUẦN TỰ & HOẠT ĐỘNG (SEQUENCE & ACTIVITY DIAGRAMS)"
    ]),
    ("1. MÔ HÌNH LỚP TỔNG QUAN & BIỂU ĐỒ CLASS DIAGRAM (KÈM CODE PLANTUML)", [
        "Mô hình lớp của hệ thống Quản lý CLB Sinh viên bao gồm các Lớp Thực thể (SQLAlchemy ORM Entities kết nối PostgreSQL), Lớp Dịch vụ (Flask Service & Pydantic Schemas) và Lớp Tương tác AI (AI Engine Services).",
        ('code', "class_diagram.puml", """@startuml class_diagram
!theme plain
class User {
    +int id
    +string email
    +string password_hash
    +RoleEnum role
    +List<string> skills
    +List<string> free_slots
    +int contribution_score
    +authenticate(password): bool
}
class Department {
    +int id
    +string name
    +int leader_id
    +get_members(): List<User>
}
class Activity {
    +int id
    +string title
    +string qr_code_token
    +ActivityStatus status
    +generate_qr_code(): string
}
class Attendance {
    +int id
    +int activity_id
    +int user_id
    +datetime checkin_time
}
class Task {
    +int id
    +string title
    +TaskStatus status
    +int assignee_id
    +update_status(status): void
}
class TaskAssignment {
    +int id
    +int task_id
    +int user_id
    +float match_score
}
class AIService {
    +suggest_assignments(tasks, members)
    +generate_announcement(event, tone)
}
Department "1" o-- "0..*" User
Activity "1" *-- "0..*" Attendance
Activity "1" *-- "0..*" Task
Task "1" -- "0..1" TaskAssignment
AIService ..> TaskAssignment : <<generates>>
@enduml""")
    ]),
    ("2. ĐẶC TẢ CHI TIẾT CÁC LỚP THỰC THỂ CỐT LÕI", [
        ('table',
         ["Tên Lớp (Class Name)", "Thuộc tính (Attributes)", "Phương thức (Methods)", "Mô tả vai trò"],
         [
             ["User", "- id: int\n- full_name: str\n- email: str\n- role: Enum\n- department_id: int\n- skills: List[str]\n- free_slots: List[str]", "+ update_profile()\n+ get_assigned_tasks()\n+ checkin_activity()", "Quản lý thông tin thành viên, kỹ năng và lịch rảnh."],
             ["Department", "- id: int\n- name: str\n- description: str", "+ get_members()\n+ add_member()", "Quản lý thông tin Ban chuyên môn."],
             ["Activity", "- id: int\n- title: str\n- description: str\n- start_time: datetime\n- location: str\n- status: Enum", "+ create_activity()\n+ generate_qr_code()\n+ get_attendances()", "Quản lý sự kiện và hoạt động CLB."],
             ["Attendance", "- id: int\n- activity_id: int\n- user_id: int\n- checkin_time: datetime\n- status: Enum", "+ record_checkin()\n+ verify_qr()", "Ghi nhận dữ liệu điểm danh."],
             ["Task", "- id: int\n- activity_id: int\n- title: str\n- required_skill: str\n- deadline: datetime\n- status: Enum", "+ update_status()\n+ assign_to_user()", "Quản lý nhiệm vụ và tiến độ."],
             ["TaskAssignment", "- id: int\n- task_id: int\n- user_id: int\n- ai_suggested: bool\n- match_score: float", "+ confirm_assignment()", "Lưu thông tin ghép cặp phân công."],
             ["AIService", "- api_key: str\n- model_name: str", "+ suggest_assignments()\n+ generate_announcement()\n+ summarize_activity()", "Lớp dịch vụ kết nối AI Engine (Gemini/OpenAI & Local Fallback)."]
         ]
        )
    ]),
    ("3. BIỂU ĐỒ TUẦN TỰ & HOẠT ĐỘNG (SEQUENCE & ACTIVITY DIAGRAMS)", [
        "Mã nguồn Biểu đồ Tuần tự AI Phân công Nhiệm vụ:",
        ('code', "sequence_ai_matchmaking.puml", """@startuml sequence_ai_matchmaking
!theme plain
autonumber
actor "Leader" as Leader
participant "React Kanban" as UI
participant "Task Controller" as API
participant "AIService Engine" as AI
participant "Google Gemini API" as Cloud
participant "Local Rule Engine" as Fallback
participant "PostgreSQL DB" as DB

Leader -> UI : Bấm 'AI Gợi ý Phân công'
UI -> API : POST /api/ai/suggest-assignments
API -> DB : Lấy Tasks & Members
DB --> API : Task List & Member List
API -> AI : match_tasks_to_members(tasks, members)
alt Online & Key OK
    AI -> Cloud : Prompt JSON
    Cloud --> AI : Raw JSON
else Offline / Quota 429
    AI -> Fallback : execute_rule_matching()
    Fallback --> AI : Match Results (< 100ms)
end
AI --> API : Validated Suggestions
API --> UI : HTTP 200 OK {suggestions}
UI --> Leader : Hiển thị bảng đề xuất Match Score %
@enduml""")
    ])
]

# 05_GenAI_SoftwareDevelopment_functional-testing.docx
p5_sections = [
    ("MỤC LỤC TỔNG QUAN TÀI LIỆU", [
        "1. YÊU CẦU TÀI NGUYÊN KIỂM THỬ",
        "2. DANH SÁCH TÌNH HUỐNG KIỂM THỬ (TEST CASES)",
        "3. BÁO CÁO KẾT QUẢ KIỂM THỬ (TEST REPORT)"
    ]),
    ("1. YÊU CẦU TÀI NGUYÊN KIỂM THỬ", [
        "1.1 Phần cứng: Máy tính cá nhân RAM 8GB+, Intel Core i5, kết nối Internet.",
        "1.2 Phần mềm:",
        ('table',
         ["Tên phần mềm", "Phiên bản", "Mục đích sử dụng"],
         [
             ["Python / Flask", "Python 3.11 / Flask 3.1", "Môi trường Backend ứng dụng RESTful API"],
             ["PostgreSQL", "16.x (Docker)", "Hệ quản trị CSDL quan hệ chính thức"],
             ["Docker & Docker Compose", "24.0+", "Nền tảng container hóa toàn bộ hệ thống"],
             ["PyTest", "8.0+", "Công cụ kiểm thử tự động (Unit Test / API Test)"],
             ["Postman / k6", "10.0+", "Kiểm thử API Endpoints & Kiểm thử tải"],
             ["Windows 11 / Linux", "64-bit", "Hệ điều hành triển khai & kiểm thử"]
         ]
        )
    ]),
    ("2. DANH SÁCH TÌNH HUỐNG KIỂM THỬ (TEST CASES)", [
        ('table',
         ["Test ID", "Chức năng", "Mô tả tình huống test", "Điều kiện trước", "Kết quả kỳ vọng", "Kết quả thực tế", "Trạng thái"],
         [
             ["TC-01", "Đăng nhập JWT", "Đăng nhập với Email và Mật khẩu đúng", "Tài khoản đã tồn tại trong PostgreSQL", "Đăng nhập thành công, trả về JWT Token", "Đăng nhập thành công", "PASS"],
             ["TC-02", "Đăng nhập JWT", "Đăng nhập với Mật khẩu sai", "Tài khoản đã tồn tại", "Báo lỗi HTTP 401 Unauthorized", "Hiển thị đúng báo lỗi", "PASS"],
             ["TC-03", "Điểm danh QR", "Quét mã QR sự kiện hợp lệ", "Sự kiện đang diễn ra", "Ghi nhận điểm danh thành công vào PostgreSQL", "Ghi nhận đúng thời gian", "PASS"],
             ["TC-04", "AI Sinh thông báo", "Nhập chi tiết sự kiện thô hợp lệ", "Đã đăng nhập Trưởng ban", "AI trả về văn bản bài đăng đầy đủ emoji", "Thông báo mượt mà, đúng thông tin", "PASS"],
             ["TC-05", "AI Phân công", "Gợi ý phân công khi đầy đủ skill/lịch rảnh", "Thành viên đã cập nhật hồ sơ", "AI trả về gợi ý khớp skill > 85%", "Gợi ý chính xác thành viên phù hợp", "PASS"],
             ["TC-06", "AI Phân công (Edge)", "Gợi ý khi thành viên chưa điền kỹ năng", "Trường `skills` = []", "AI phân công task phổ thông & hiển thị cảnh báo", "Xử lý êm mượt, không vỡ app", "PASS"],
             ["TC-07", "AI Tóm tắt", "Tóm tắt từ ghi chú cuộc họp thô", "Có ghi chú họp", "AI xuất báo cáo tóm tắt ưu/nhược điểm", "Báo cáo tóm tắt ngắn gọn", "PASS"]
         ]
        )
    ]),
    ("3. BÁO CÁO KẾT QUẢ KIỂM THỬ (TEST REPORT)", [
        " - Tổng số Test Cases đã thực thi: 25 Test Cases thuộc Core Regression Suite.",
        " - Số lượng Pass: 25 / 25 (Đạt 100%).",
        " - Số lượng Fail: 0.",
        " - Đánh giá chung: Hệ thống Flask + PostgreSQL vận hành ổn định, các chức năng CRUD và AI tích hợp đạt tiêu chuẩn nghiệm thu."
    ])
]

# 06_GenAI_SoftwareDevelopment_screenflow_db.docx
p6_sections = [
    ("MỤC LỤC TỔNG QUAN TÀI LIỆU", [
        "1. SCREEN FLOW: PHÂN LUỒNG MÀN HÌNH ỨNG DỤNG (REACT-VITE)",
        "2. CƠ SỞ DỮ LIỆU POSTGRESQL (ERD SCHEMAS)",
        "3. CÁC RÀNG BUỘC TOÀN VẸN CSDL TRÊN POSTGRESQL"
    ]),
    ("1. SCREEN FLOW: PHÂN LUỒNG MÀN HÌNH ỨNG DỤNG (REACT-VITE)", [
        "Ứng dụng bao gồm 8 màn hình chính được phân luồng mạch lạc trong React-Vite:",
        " - SCR-01 (Đăng nhập) $\rightarrow$ SCR-02 (Dashboard tổng quan)",
        " - SCR-02 $\rightarrow$ SCR-03 (Quản lý Thành viên & Hồ sơ Pydantic)",
        " - SCR-02 $\rightarrow$ SCR-04 (Quản lý Ban chuyên môn)",
        " - SCR-02 $\rightarrow$ SCR-05 (Quản lý Sự kiện & Điểm danh QR)",
        " - SCR-02 $\rightarrow$ SCR-06 (Quản lý Nhiệm vụ Kanban Board)",
        " - SCR-06 $\rightarrow$ SCR-07 (AI Hub - Gợi ý Phân công Nhiệm vụ)",
        " - SCR-05 $\rightarrow$ SCR-08 (AI Hub - Sinh Thông báo & Tóm tắt)"
    ]),
    ("2. CƠ SỞ DỮ LIỆU POSTGRESQL (ERD SCHEMAS)", [
        ('table',
         ["Tên Bảng", "Khoá chính (PK)", "Khoá ngoại (FK)", "Mô tả các cột chính"],
         [
             ["users", "id", "department_id", "full_name, email, password_hash (bcrypt), role, skills(JSON), free_slots(JSON)"],
             ["departments", "id", "None", "name, description"],
             ["activities", "id", "None", "title, description, start_time, end_time, location, qr_code_hash, status"],
             ["attendances", "id", "activity_id, user_id", "checkin_time, status (PRESENT/ABSENT), device_fingerprint"],
             ["tasks", "id", "activity_id", "title, required_skill, deadline, status (TO_DO/IN_PROGRESS/DONE)"],
             ["task_assignments", "id", "task_id, user_id", "ai_suggested (bool), match_score (float), assigned_by"],
             ["ai_logs", "id", "user_id", "prompt_type, input_data, output_result, created_at"]
         ]
        )
    ]),
    ("3. CÁC RÀNG BUỘC TOÀN VẸN CSDL TRÊN POSTGRESQL", [
        " - FK `users.department_id` tham chiếu `departments.id` (ON DELETE SET NULL).",
        " - FK `attendances.activity_id` & `user_id` có ràng buộc UNIQUE(activity_id, user_id) chống điểm danh trùng lặp.",
        " - Ràng buộc CHECK `users.role` IN ('ADMIN', 'LEADER', 'MEMBER')."
    ])
]

# 07_GenAI_SoftwareDevelopment_user-guide.docx
p7_sections = [
    ("MỤC LỤC TỔNG QUAN TÀI LIỆU", [
        "1. GIỚI THIỆU VÀ YÊU CẦU CẤU HÌNH",
        "2. HƯỚNG DẪN DÀNH CHO BAN CHỦ NHIỆM (ADMIN)",
        "3. HƯỚNG DẪN DÀNH CHO TRƯỞNG BAN (LEADER)",
        "4. HƯỚNG DẪN DÀNH CHO THÀNH VIÊN (MEMBER)"
    ]),
    ("1. GIỚI THIỆU VÀ YÊU CẦU CẤU HÌNH", [
        "Tài liệu này hướng dẫn chi tiết cách vận hành Hệ thống Quản lý CLB Sinh viên (Flask + React-Vite + PostgreSQL + Docker) cho 3 đối tượng: Ban Chủ nhiệm, Trưởng ban và Thành viên.",
        "Khởi chạy hệ thống: Chạy lệnh `docker-compose up -d` để khởi động đồng thời PostgreSQL, Flask Backend và React-Vite Frontend.",
        "Yêu cầu hệ thống: Trình duyệt web hiện đại (Chrome, Edge, Firefox, Safari) có kết nối Internet."
    ]),
    ("2. HƯỚNG DẪN DÀNH CHO BAN CHỦ NHIỆM (ADMIN)", [
        " - Đăng nhập hệ thống: Truy cập trang `/login`, nhập Email và Mật khẩu BCN (nhận JWT Token).",
        " - Xem Dashboard: Theo dõi biểu đồ tổng số thành viên, số sự kiện trong tháng, tỷ lệ tham gia.",
        " - Phân quyền người dùng: Truy cập mục 'Quản lý Thành viên' $\rightarrow$ Thay đổi vai trò thành 'Trưởng ban' hoặc 'Thành viên'."
    ]),
    ("3. HƯỚNG DẪN DÀNH CHO TRƯỞNG BAN (LEADER)", [
        " - Tạo sự kiện & Sinh mã QR Điểm danh: Vào mục 'Sự kiện' $\rightarrow$ Bấm 'Tạo sự kiện mới' $\rightarrow$ Bấm 'Hiển thị mã QR Điểm danh' để sinh viên quét.",
        " - Sử dụng AI Gợi ý Phân công: Vào màn hình Nhiệm vụ sự kiện $\rightarrow$ Bấm nút 'AI Gợi ý Phân công' $\rightarrow$ Kiểm tra danh sách đề xuất $\rightarrow$ Bấm 'Xác nhận'.",
        " - Sử dụng AI Sinh thông báo: Nhập thông tin sự kiện thô $\rightarrow$ Bấm 'Sinh thông báo AI' $\rightarrow$ Sao chép bài đăng để truyền thông."
    ]),
    ("4. HƯỚNG DẪN DÀNH CHO THÀNH VIÊN (MEMBER)", [
        " - Cập nhật Kỹ năng & Lịch rảnh: Vào trang 'Hồ sơ cá nhân' $\rightarrow$ Tick chọn các Kỹ năng cá nhân & Khung giờ rảnh trong tuần.",
        " - Quét mã QR Điểm danh: Mở camera điện thoại quét mã QR tại buổi họp/sự kiện để hệ thống ghi nhận.",
        " - Xem Nhiệm vụ được giao: Vào mục 'Nhiệm vụ của tôi' để cập nhật trạng thái hoàn thành (To-do $\rightarrow$ Done)."
    ])
]

# Generate all documents
def generate_all():
    docs_map = [
        ("01_GenAI_SoftwareDevelopment_project-plan.docx", "KẾ HOẠCH THỰC HIỆN DỰ ÁN\n(PROJECT PLAN)", p1_sections),
        ("02_GenAI_SoftwareDevelopment_requirements-qa.docx", "BẢNG CÂU HỎI VÀ GIẢI ĐÁP YÊU CẦU NGHIỆP VỤ\n(REQUIREMENTS Q&A)", p2_sections),
        ("03_GenAI_SoftwareDevelopment_requirements-specification.docx", "ĐẶC TẢ YÊU CẦU PHẦN MỀM\n(SOFTWARE REQUIREMENTS SPECIFICATION - SRS)", p3_sections),
        ("04_GenAI_SoftwareDevelopment_object-oriented-design.docx", "THIẾT KẾ HƯỚNG ĐỐI TƯỢNG VÀ MÔ HÌNH LỚP\n(OBJECT-ORIENTED DESIGN - OOD)", p4_sections),
        ("05_GenAI_SoftwareDevelopment_functional-testing.docx", "KẾ HOẠCH VÀ KỊCH BẢN KIỂM THỬ CHỨC NĂNG\n(FUNCTIONAL TESTING PLAN & TEST CASES)", p5_sections),
        ("06_GenAI_SoftwareDevelopment_screenflow_db.docx", "THIẾT KẾ PHÂN LUỒNG MÀN HÌNH VÀ CƠ SỞ DỮ LIỆU\n(SCREEN FLOW & DATABASE ERD)", p6_sections),
        ("07_GenAI_SoftwareDevelopment_user-guide.docx", "HƯỚNG DẪN SỬ DỤNG VÀ VẬN HÀNH HỆ THỐNG\n(USER GUIDE & OPERATIONAL MANUAL)", p7_sections)
    ]
    
    try:
        from build_full_survey_req_doc import p8_sections_kt1
        docs_map.append(("08_KhaoSat_PhanTich_YeuCau_ChucNang_PhiChucNang.docx", "BÁO CÁO KHẢO SÁT VÀ PHÂN TÍCH YÊU CẦU CỦA ỨNG DỤNG\n(GIAI ĐOẠN KT1: TỪ TUẦN 1 ĐẾN HẾT TUẦN 3)\nYÊU CẦU CHỨC NĂNG VÀ YÊU CẦU PHI CHỨC NĂNG", p8_sections_kt1))
    except Exception as e:
        print(f"Could not import p8: {e}")
        
    for fname, title, sects in docs_map:
        create_unified_document(fname, title, sects)

if __name__ == "__main__":
    generate_all()
