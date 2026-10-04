# -*- coding: utf-8 -*-
"""
Update Doc 02 and Doc 03 to ensure full consistency:
- Replace use case images in Doc 03 with the newly rendered ones (all extend, no AI in Phân hệ 5).
- Update text and table packages in Doc 02 and Doc 03.
- Sync to CacGiaiDoanThucHien.
"""

import os
import sys
import shutil
import zipfile
import docx

sys.stdout.reconfigure(encoding='utf-8')

DOCS_DIR = r"docs"
IMAGES_DIR = r"images"
CG_DIR = r"CacGiaiDoanThucHien"
KT1_DIR = os.path.join(CG_DIR, "GiaiDoan_KT1_KhaoSat_YeuCau_ThietKe_Tuan1_Tuan3")

# 1. UPDATE DOC 03
print(">>> CẬP NHẬT DOC 03: SRS...")
d3_path = os.path.join(DOCS_DIR, "03_GenAI_SoftwareDevelopment_requirements-specification.docx")
d3 = docx.Document(d3_path)

# Update P37 & P39
p37 = d3.paragraphs[37]
print("Old Doc 03 P37:", p37.text)
p37.text = "7.5 Phân hệ 5: Báo cáo Thống kê:"
print("New Doc 03 P37:", p37.text)

p39 = d3.paragraphs[39]
print("Old Doc 03 P39:", p39.text)
p39.text = "Hình 4.3.5: Use Case Phân hệ Báo cáo Thống kê (UC03, UC06, UC07, UC08)"
print("New Doc 03 P39:", p39.text)

# Update Table 3
t3 = d3.tables[3]
for r_idx in [3, 6, 7, 8]:
    t3.rows[r_idx].cells[2].text = "Báo cáo Thống kê"

t3.rows[6].cells[1].text = "Gợi ý Phân công Nhiệm vụ Thông minh"
t3.rows[7].cells[1].text = "Sinh Bài đăng Thông báo Sự kiện"
t3.rows[8].cells[1].text = "Tóm tắt Kết quả Hoạt động & Phản hồi"

temp_d3 = os.path.join(DOCS_DIR, "_temp_d3.docx")
d3.save(temp_d3)

# Replace images in Doc 03
d3_media_map = {
    'word/media/image2.png': os.path.join(IMAGES_DIR, 'usecase_overall.png'),
    'word/media/image3.png': os.path.join(IMAGES_DIR, 'usecase_sub1_auth.png'),
    'word/media/image4.png': os.path.join(IMAGES_DIR, 'usecase_sub2_member.png'),
    'word/media/image5.png': os.path.join(IMAGES_DIR, 'usecase_sub3_event.png'),
    'word/media/image6.png': os.path.join(IMAGES_DIR, 'usecase_sub4_task.png'),
    'word/media/image7.png': os.path.join(IMAGES_DIR, 'usecase_sub5_ai.png')
}

out_d3_zip = os.path.join(DOCS_DIR, "_out_d3.docx")
with zipfile.ZipFile(temp_d3, 'r') as zin:
    with zipfile.ZipFile(out_d3_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.filename in d3_media_map:
                src_f = d3_media_map[item.filename]
                print(f"  -> Doc 03 thay thế {item.filename} bằng {src_f}")
                with open(src_f, 'rb') as f:
                    zout.writestr(item, f.read())
            else:
                zout.writestr(item, zin.read(item.filename))

shutil.copyfile(out_d3_zip, d3_path)
shutil.copyfile(d3_path, os.path.join(CG_DIR, "03_GenAI_SoftwareDevelopment_requirements-specification.docx"))
shutil.copyfile(d3_path, os.path.join(KT1_DIR, "03_GenAI_SoftwareDevelopment_requirements-specification.docx"))

if os.path.exists(temp_d3):
    os.remove(temp_d3)
if os.path.exists(out_d3_zip):
    os.remove(out_d3_zip)
print("  ✓ Đã cập nhật xong Doc 03!")

# 2. UPDATE DOC 02
print("\n>>> CẬP NHẬT DOC 02: REQUIREMENTS Q&A...")
d2_path = os.path.join(DOCS_DIR, "02_GenAI_SoftwareDevelopment_requirements-qa.docx")
d2 = docx.Document(d2_path)
t3_d2 = d2.tables[3]
# Row 5 in Table 3 of Doc 02: SUB-05
cell = t3_d2.rows[5].cells[1]
print("Old Doc 02 T3R5:", cell.text)
if "Trợ lý AI & Báo cáo Thống kê" in cell.text:
    cell.text = "Báo cáo Thống kê"
    print("New Doc 02 T3R5:", cell.text)
d2.save(d2_path)
shutil.copyfile(d2_path, os.path.join(CG_DIR, "02_GenAI_SoftwareDevelopment_requirements-qa.docx"))
shutil.copyfile(d2_path, os.path.join(KT1_DIR, "02_GenAI_SoftwareDevelopment_requirements-qa.docx"))
print("  ✓ Đã cập nhật xong Doc 02!")

print("\n>>> TẤT CẢ TÀI LIỆU ĐÃ ĐƯỢC ĐỒNG BỘ 100%!")
