import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

sys.stdout.reconfigure(encoding='utf-8')

docs_dir = r"D:\DTC245200328\Nam3\Ki1\UngDungAI\Student_Club_Management\docs"
images_dir = r"D:\DTC245200328\Nam3\Ki1\UngDungAI\Student_Club_Management\images"

# 1. Update 06_GenAI_SoftwareDevelopment_screenflow_db.docx
print("=== Updating 06_GenAI_SoftwareDevelopment_screenflow_db.docx ===")
fn06 = os.path.join(docs_dir, "06_GenAI_SoftwareDevelopment_screenflow_db.docx")
doc06 = docx.Document(fn06)

# Insert images into doc06
# Find section 1 for screenflow and section 2 for ERD
for i, p in enumerate(doc06.paragraphs):
    if "1. SCREEN FLOW: PHÂN LUỒNG MÀN HÌNH" in p.text:
        # Insert image after the list of screens
        target_p = None
        for j in range(i+1, len(doc06.paragraphs)):
            if "SCR-08" in doc06.paragraphs[j].text:
                target_p = doc06.paragraphs[j]
                break
        if target_p:
            img_p = target_p.insert_paragraph_before()
            img_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            img_p.paragraph_format.space_before = Pt(12)
            img_p.paragraph_format.space_after = Pt(4)
            r = img_p.add_run()
            sf_img = os.path.join(images_dir, "screenflow_diagram.png")
            if os.path.exists(sf_img):
                r.add_picture(sf_img, width=Inches(6.2))
                cap_p = target_p.insert_paragraph_before()
                cap_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                cap_p.paragraph_format.space_after = Pt(12)
                rcap = cap_p.add_run("Hình 1: Sơ đồ Phân luồng 8 Màn hình Ứng dụng React-Vite SPA (Screen Flow)")
                rcap.font.name = "Times New Roman"
                rcap.italic = True
                rcap.font.size = Pt(10.5)
                rcap.font.color.rgb = RGBColor(70, 70, 70)
                print("Embedded screenflow_diagram.png into Doc 06!")
        break

for i, p in enumerate(doc06.paragraphs):
    if "2. CƠ SỞ DỮ LIỆU POSTGRESQL (ERD SCHEMAS)" in p.text:
        img_p = doc06.paragraphs[i+1].insert_paragraph_before() if i+1 < len(doc06.paragraphs) else doc06.add_paragraph()
        img_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        img_p.paragraph_format.space_before = Pt(12)
        img_p.paragraph_format.space_after = Pt(4)
        r = img_p.add_run()
        erd_img = os.path.join(images_dir, "erd_database.png")
        if os.path.exists(erd_img):
            r.add_picture(erd_img, width=Inches(6.2))
            cap_p = img_p.insert_paragraph_before() # Wait, after img
            # Actually let's just add after img_p
            cap_p2 = doc06.paragraphs[i+2].insert_paragraph_before() if i+2 < len(doc06.paragraphs) else doc06.add_paragraph()
            cap_p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
            cap_p2.paragraph_format.space_after = Pt(12)
            rcap = cap_p2.add_run("Hình 2: Sơ đồ Thực thể - Mối quan hệ Cơ sở dữ liệu (PostgreSQL / SQLite ERD - Crow's Foot Notation)")
            rcap.font.name = "Times New Roman"
            rcap.italic = True
            rcap.font.size = Pt(10.5)
            rcap.font.color.rgb = RGBColor(70, 70, 70)
            print("Embedded erd_database.png into Doc 06!")
        break

doc06.save(fn06)
print("Saved Doc 06 successfully!")

# 2. Update 04_GenAI_SoftwareDevelopment_object-oriented-design.docx
print("=== Updating 04_GenAI_SoftwareDevelopment_object-oriented-design.docx ===")
fn04 = os.path.join(docs_dir, "04_GenAI_SoftwareDevelopment_object-oriented-design.docx")
doc04 = docx.Document(fn04)

for i, p in enumerate(doc04.paragraphs):
    if "1. MÔ HÌNH LỚP TỔNG QUAN" in p.text:
        target_p = doc04.paragraphs[i+1]
        img_p = target_p.insert_paragraph_before()
        img_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        img_p.paragraph_format.space_before = Pt(12)
        img_p.paragraph_format.space_after = Pt(4)
        r = img_p.add_run()
        cls_img = os.path.join(images_dir, "class_diagram.png")
        if os.path.exists(cls_img):
            r.add_picture(cls_img, width=Inches(6.2))
            cap_p = target_p.insert_paragraph_before()
            cap_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            cap_p.paragraph_format.space_after = Pt(12)
            rcap = cap_p.add_run("Hình 1: Biểu đồ Lớp Phân tích & Thực thể CSDL (UML Class Diagram / Domain Model)")
            rcap.font.name = "Times New Roman"
            rcap.italic = True
            rcap.font.size = Pt(10.5)
            rcap.font.color.rgb = RGBColor(70, 70, 70)
            print("Embedded class_diagram.png into Doc 04!")
        break

for i, p in enumerate(doc04.paragraphs):
    if "3. BIỂU ĐỒ TUẦN TỰ & HOẠT ĐỘNG" in p.text:
        target_p = doc04.paragraphs[i+1] if i+1 < len(doc04.paragraphs) else doc04.add_paragraph()
        img_p = target_p.insert_paragraph_before()
        img_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        img_p.paragraph_format.space_before = Pt(12)
        img_p.paragraph_format.space_after = Pt(4)
        r = img_p.add_run()
        seq_img = os.path.join(images_dir, "sequence_ai_matchmaking.png")
        if os.path.exists(seq_img):
            r.add_picture(seq_img, width=Inches(6.2))
            cap_p = target_p.insert_paragraph_before()
            cap_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            cap_p.paragraph_format.space_after = Pt(12)
            rcap = cap_p.add_run("Hình 2: Biểu đồ Tuần tự AI Gợi ý Phân công Nhiệm vụ với Dual-Engine Fallback")
            rcap.font.name = "Times New Roman"
            rcap.italic = True
            rcap.font.size = Pt(10.5)
            rcap.font.color.rgb = RGBColor(70, 70, 70)
            print("Embedded sequence_ai_matchmaking.png into Doc 04!")
        break

doc04.save(fn04)
print("Saved Doc 04 successfully!")

print("=== Done updating Doc 04 and Doc 06 ===")
