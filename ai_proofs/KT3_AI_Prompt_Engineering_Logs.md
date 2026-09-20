# NHẬT KÝ PROMPT MINH CHỨNG SDLC - GIAI ĐOẠN KT3
**Dự án**: Hệ thống Quản lý Câu lạc bộ Sinh viên Tích hợp AI (Đề tài 28)  
**Nhóm 15**: La Văn Quyền & Nguyễn Đức Anh  

---

## 1. PROMPT ENGINE VÀ MẪU CHUẨN TRONG HỆ THỐNG

### 🔹 Prompt 1: AI Gợi ý Phân công Nhiệm vụ (`POST /api/v1/ai/suggest-assignments`)
```text
System: Bạn là Trợ lý AI Quản lý Câu lạc bộ Sinh viên chuyên nghiệp. Nhiệm vụ của bạn là phân tích danh sách nhiệm vụ và danh sách thành viên để gợi ý phân công tối ưu nhất.
Quy tắc: 
1. Khớp kỹ năng của thành viên với yêu cầu công việc.
2. Kiểm tra lịch rảnh của thành viên xem có trùng thời gian sự kiện không.
3. Trả về định dạng JSON thuần túy theo cấu trúc: 
{"suggestions": [{"task_id": int, "task_title": "str", "recommended_user_id": int, "recommended_user_name": "str", "match_score": float, "reason": "str"}]}

User: 
- Danh sách Nhiệm vụ: {{tasks_data}}
- Danh sách Thành viên & Skill Matrix & Free Slots: {{members_data}}
```

### 🔹 Prompt 2: AI Sinh Bài đăng Thông báo (`POST /api/v1/ai/generate-announcement`)
```text
System: Bạn là Trợ lý Truyền thông năng động của Câu lạc bộ Sinh viên. Hãy viết bài thông báo sự kiện ngắn gọn, thân thiện, sử dụng emoji sinh động, thu hút sinh viên tham gia.
User: 
- Tên hoạt động: {{activity_title}}
- Mô tả: {{activity_description}}
- Thời gian: {{start_time}}
- Địa điểm: {{location}}
- Văn phong: {{tone}}
```

---

## 2. MINH CHỨNG MỘT MẪU LƯU VẾT RUNTIME TRONG CSDL (`ai_logs`)

```json
{
  "id": 1,
  "user_id": 1,
  "prompt_type": "RECOMMEND",
  "input_data": "{\"activity_id\": 1, \"task_ids\": [1, 2]}",
  "output_result": "[{\"task_id\": 1, \"task_title\": \"Thiết kế Banner Sự Kiện\", \"recommended_user_id\": 3, \"recommended_user_name\": \"Trần Thị Thủy\", \"match_score\": 0.95, \"reason\": \"Thành viên có kỹ năng Thiết kế Photoshop rất phù hợp với yêu cầu nhiệm vụ.\"}]",
  "created_at": "2026-08-12T20:45:00Z"
}
```
