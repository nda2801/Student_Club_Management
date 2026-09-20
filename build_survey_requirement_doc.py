import os
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

docs_dir = r"D:\DTC245200328\Nam3\Ki1\UngDungAI\Student_Club_Management\docs"
file_name = "08_KhaoSat_PhanTich_YeuCau_ChucNang_PhiChucNang.docx"

doc = docx.Document()

# Title
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_title = p_title.add_run("BÁO CÁO KHẢO SÁT VÀ PHÂN TÍCH YÊU CẦU PHẦN MỀM\n(YÊU CẦU CHỨC NĂNG VÀ PHI CHỨC NĂNG)")
r_title.bold = True
r_title.font.size = Pt(16)
r_title.font.color.rgb = RGBColor(0, 51, 102)

# Subtitle / Header
p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_sub = p_sub.add_run("Đề tài 28: Hệ thống Quản lý Câu lạc bộ Sinh viên Tích hợp AI\nNhóm 15: La Văn Quyền (Trưởng nhóm) & Nguyễn Đức Anh (Thành viên)")
r_sub.font.size = Pt(11)
r_sub.italic = True
doc.add_paragraph()

sections = [
    ("CHƯƠNG 1: TỔNG QUAN KHẢO SÁT HIỆN TRẠNG (CURRENT STATE SURVEY)", [
        "1.1 Đối tượng khảo sát:",
        "Khảo sát được thực hiện trên 120 sinh viên thuộc 4 Ban chuyên môn (Ban Truyền thông, Ban Sự kiện, Ban Chuyên môn, Ban Đối ngoại) và 6 thành viên Ban Chủ nhiệm CLB.",
        "1.2 Phương pháp khảo sát:",
        " - Phỏng vấn sâu (Deep Interview) đối với Chủ nhiệm và các Trưởng ban.",
        " - Khảo sát trực tuyến qua mẫu Google Form đối với thành viên CLB.",
        " - Quan sát trực tiếp quy trình chuẩn bị sự kiện, phân công công việc và điểm danh họp hàng tuần.",
        "1.3 Thống kê kết quả khảo sát thực trạng:",
        ('table',
         ["STT", "Vấn đề / Điểm đau (Pain Point)", "Tỷ lệ ghi nhận", "Mức độ ảnh hưởng", "Giải pháp yêu cầu hệ thống"],
         [
             ["1", "Phân công nhiệm vụ thủ công qua tin nhắn, không nắm rõ lịch rảnh & kỹ năng thành viên", "92% Trưởng ban", "Rất cao (Lãng phí 2-3h/sự kiện)", "Tính năng AI Gợi ý phân công tự động khớp Skill & Free Slots."],
             ["2", "Điểm danh bằng giấy / Google Form bị chậm, dễ sót hoặc gian lận điểm danh hộ", "78% Sự kiện", "Cao (Mất thời gian đầu buổi)", "Điểm danh mã QR Code tự động trên thiết bị di động."],
             ["3", "Ban chủ nhiệm khó theo dõi tiến độ nhiệm vụ và đánh giá mức độ đóng góp thành viên", "85% Ban Chủ nhiệm", "Rất cao (Đánh giá cảm tính)", "Bảng Kanban Board trực quan & Bảng xếp hạng Contribution Score."],
             ["4", "Viết bài thông báo truyền thông sự kiện tốn thời gian, văn phong chưa thu hút", "88% Ban Truyền thông", "Trung bình", "Tính năng AI Sinh bài đăng truyền thông sinh động với nhiều tone giọng."],
             ["5", "Tổng hợp tóm tắt kết quả cuộc họp và phản hồi thành viên bị rời rạc", "80% Trưởng ban", "Trung bình", "Tính năng AI Tóm tắt kết quả hoạt động tự động từ ghi chú."]
         ]
        )
    ]),
    ("CHƯƠNG 2: PHÂN TÍCH YÊU CẦU CHỨC NĂNG (FUNCTIONAL REQUIREMENTS - FR)", [
        "Yêu cầu chức năng mô tả các hành vi, dịch vụ và thao tác mà hệ thống phải thực hiện cho từng nhóm tác nhân.",
        "2.1 Danh mục Yêu cầu Chức năng Quản lý (FR-SYS):",
        ('table',
         ["Mã Yêu cầu", "Tên Chức năng", "Mô tả Chi tiết Yêu cầu Chức năng", "Phân quyền Tác nhân"],
         [
             ["FR-SYS-01", "Đăng nhập & Phân quyền", "Xác thực tài khoản Email/Password, cấp token JWT, phân quyền 3 vai trò (Admin, Leader, Member).", "Tất cả Tác nhân"],
             ["FR-SYS-02", "Quản lý Hồ sơ & Skill Matrix", "Cập nhật Kỹ năng cá nhân (Photoshop, Setup, Content...) và Lịch rảnh hàng tuần.", "Thành viên / Admin"],
             ["FR-SYS-03", "Quản lý Ban chuyên môn", "Tạo ban mới, thêm/sửa thành viên vào các Ban (Truyền thông, Sự kiện, Chuyên môn...).", "Ban Chủ nhiệm (Admin)"],
             ["FR-SYS-04", "Quản lý Sự kiện & Điểm danh QR", "Tạo sự kiện mới, tự động sinh mã QR Code độc bản. Quét QR để điểm danh và ghi nhận thời gian.", "Trưởng ban / Thành viên"],
             ["FR-SYS-05", "Quản lý Nhiệm vụ & Kanban Board", "Tạo task, theo dõi tiến độ 3 cột (To-Do, In-Progress, Done). Siết chặt phân quyền: Admin/Leader phân công & đổi status mọi task; Member chỉ được đổi status task của mình.", "Admin / Leader / Member"],
             ["FR-SYS-06", "Thống kê & Bảng xếp hạng", "Tính điểm đóng góp (Contribution Score = Điểm danh*10 + Task hoàn thành*20) và hiển thị Leaderboard TOP đóng góp.", "Tất cả Tác nhân"]
         ]
        ),
        "2.2 Danh mục Yêu cầu Chức năng Tích hợp AI (FR-AI):",
        ('table',
         ["Mã Yêu cầu", "Tên Chức năng AI", "Mô tả Chi tiết Yêu cầu Chức năng AI", "Đầu vào / Đầu ra"],
         [
             ["FR-AI-01", "AI Sinh Bài đăng Thông báo", "AI phân tích thông tin thô sự kiện để tự động soạn văn bản truyền thông sinh động với emoji.", "Input: Tên, Mô tả, Thời gian, Địa điểm, Tone giọng.\nOutput: Văn bản truyền thông hoàn chỉnh."],
             ["FR-AI-02", "AI Tóm tắt Kết quả Hoạt động", "AI đọc ghi chú cuộc họp và phản hồi của thành viên để tổng hợp báo cáo tóm tắt ưu/nhược điểm.", "Input: Ghi chú họp, danh sách phản hồi.\nOutput: Báo cáo tóm tắt 3 phần."],
             ["FR-AI-03", "AI Gợi ý Phân công Nhiệm vụ", "AI phân tích danh sách Task và Skill Matrix + Lịch rảnh của thành viên để tính Match Score (%) và gợi ý phân công.", "Input: Task list, Member skills, Free slots.\nOutput: Danh sách gợi ý ghép cặp + Lý do."]
         ]
        )
    ]),
    ("CHƯƠNG 3: PHÂN TÍCH YÊU CẦU PHI CHỨC NĂNG (NON-FUNCTIONAL REQUIREMENTS - NFR)", [
        "Yêu cầu phi chức năng quy định các tiêu chuẩn chất lượng, ràng buộc kỹ thuật và tiêu chí vận hành của hệ thống.",
        ('table',
         ["Nhóm Yêu cầu", "Mã NFR", "Tiêu chí & Chỉ số Chi tiết", "Phương án Kỹ thuật Đảm bảo"],
         [
             ["Hiệu năng (Performance)", "NFR-PERF-01", "Thời gian phản hồi API thông thường < 500ms; Thời gian phản hồi AI Engine < 2.5s. Hỗ trợ 200+ truy cập đồng thời.", "Sử dụng FastAPI Async I/O kết hợp SQLite/Index tối ưu truy vấn."],
             ["Bảo mật (Security)", "NFR-SEC-01", "Mã hóa mật khẩu SHA-256 + Salt. Xác thực API bằng JWT Token 7 ngày. Phân quyền RBAC nghiêm ngặt tại Backend (HTTP 403 Forbidden nếu vi phạm).", "Module `security.py` & Middleware CORS, Sanitization lọc dữ liệu trước khi gửi Prompt AI."],
             ["Độ tin cậy (Reliability)", "NFR-REL-01", "Tỷ lệ hoạt động liên tục (Uptime) >= 99.5%. Hệ thống không bị treo khi vắng kết nối Internet hoặc hết Quota API Key ngoài.", "Cấu hình chế độ Dual-AI Engine: Tự động chuyển đổi sang Local AI Fallback Engine khi mất mạng."],
             ["Giao diện & Trải nghiệm (Usability)", "NFR-USA-01", "Giao diện chuẩn Responsive tương thích Mobile & Desktop. Màu sắc HSL hiện đại, font Plus Jakarta Sans, thao tác không quá 3 click.", "Thiết kế React Tailwind/Vanilla CSS Component system + Nút đăng nhập Nhanh Demo."],
             ["Bảo trì & Mở rộng (Scalability)", "NFR-MNT-01", "Mã nguồn phân tầng rõ ràng (Controller - Service - Model - Schema). Dễ dàng nâng cấp CSDL lên PostgreSQL.", "Đ tuân thủ nguyên lý Clean Architecture & RESTful API conventions."]
         ]
        )
    ]),
    ("CHƯƠNG 4: PHÂN LOẠI ƯU TIÊN YÊU CẦU THEO PHƯƠNG PHÁP MoSCoW", [
        ('table',
         ["Mức độ Ưu tiên", "Danh sách Yêu cầu Chức năng & Phi chức năng Tương ứng", "Ghi chú Khả thi"],
         [
             ["Must Have (Bắt buộc phải có)", "FR-SYS-01 (Auth JWT), FR-SYS-02 (Member/Skill), FR-SYS-04 (QR Checkin), FR-SYS-05 (Kanban Task & RBAC), FR-AI-03 (AI Phân công), NFR-SEC-01 (Bảo mật RBAC).", "Đã hoàn thành 100% trong phiên bản v1.0."],
             ["Should Have (Nên có)", "FR-AI-01 (AI Sinh thông báo), FR-AI-02 (AI Tóm tắt), FR-SYS-06 (Bảng xếp hạng đóng góp), NFR-REL-01 (Local AI Fallback Engine).", "Đã hoàn thành 100% trong phiên bản v1.0."],
             ["Could Have (Có thể bổ sung)", "Tích hợp gửi thông báo qua Zalo OA / Telegram Bot, Export báo cáo Excel.", "Định hướng phát triển phiên bản v2.0."],
             ["Won't Have (Chưa làm đợt này)", "Thanh toán lệ phí CLB qua cổng VNPay/Momo trực tuyến.", "Không thuộc phạm vi Đề tài 28."]
         ]
        )
    ])
]

for sec_heading, sec_items in sections:
    if sec_heading:
        p_h = doc.add_paragraph()
        r_h = p_h.add_run(sec_heading)
        r_h.bold = True
        r_h.font.size = Pt(13)
        r_h.font.color.rgb = RGBColor(0, 102, 153)
        p_h.paragraph_format.space_before = Pt(10)
        p_h.paragraph_format.space_after = Pt(4)
    
    for item in sec_items:
        if isinstance(item, str):
            p_text = doc.add_paragraph(item)
            p_text.paragraph_format.space_after = Pt(4)
            p_text.paragraph_format.line_spacing = 1.15
        elif isinstance(item, tuple) and item[0] == 'table':
            headers, rows = item[1], item[2]
            table = doc.add_table(rows=1, cols=len(headers))
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
            table.style = 'Table Grid'
            hdr_cells = table.rows[0].cells
            for idx, heading in enumerate(headers):
                hdr_cells[idx].text = heading
                for p in hdr_cells[idx].paragraphs:
                    for r in p.runs:
                        r.bold = True
                        r.font.size = Pt(9.5)
            for row_data in rows:
                row_cells = table.add_row().cells
                for idx, cell_value in enumerate(row_data):
                    row_cells[idx].text = str(cell_value)
                    for p in row_cells[idx].paragraphs:
                        for r in p.runs:
                            r.font.size = Pt(9.0)
            doc.add_paragraph()

file_path = os.path.join(docs_dir, file_name)
doc.save(file_path)
print(f"SUCCESSFULLY GENERATED: {file_name}")
