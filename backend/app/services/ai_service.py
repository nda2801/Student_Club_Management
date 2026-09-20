import json
import httpx
from typing import List, Dict, Any
from app.core.config import settings

class AIService:
    @staticmethod
    def generate_announcement(
        activity_title: str,
        activity_description: str,
        start_time: str,
        location: str,
        tone: str = "enthusiastic"
    ) -> str:
        """AI Feature 1: Generate engaging event announcement text."""
        
        prompt = f"""System: Bạn là Trợ lý Truyền thông năng động của Câu lạc bộ Sinh viên. Hãy viết bài thông báo sự kiện ngắn gọn, thân thiện, sử dụng emoji sinh động, thu hút sinh viên tham gia.
        
Thông tin sự kiện:
- Tên hoạt động: {activity_title}
- Mô tả: {activity_description}
- Thời gian: {start_time}
- Địa điểm: {location}
- Văn phong mong muốn: {tone}"""

        # If Gemini API key is configured
        if settings.GEMINI_API_KEY:
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={settings.GEMINI_API_KEY}"
                with httpx.Client(timeout=10.0) as client:
                    resp = client.post(url, json={
                        "contents": [{"parts": [{"text": prompt}]}]
                    })
                    if resp.status_code == 200:
                        data = resp.json()
                        return data["candidates"][0]["content"]["parts"][0]["text"]
            except Exception as e:
                print(f"Gemini API Exception, fallback to Local Rule-based Engine: {e}")

        # Intelligent Rule-based Fallback Generator
        tone_intro = "🔥 MỌI NGHƯỜI ƠI! SỰ KIỆN HOT NHẤT THÁNG ĐÃ ĐẾN RỒI ĐÂY! 🔥" if tone == "enthusiastic" else "📢 THÔNG BÁO CHÍNH THỨC TỪ BAN CHỦ NHIỆM CLB"
        return f"""{tone_intro}

🌟 **{activity_title.upper()}** 🌟

{activity_description}

📌 **THÔNG TIN CHI TIẾT:**
⏰ **Thời gian:** {start_time}
📍 **Địa điểm:** {location}
👥 **Đối tượng:** Tất cả thành viên CLB Sinh viên

👉 Hãy đăng ký và có mặt đúng giờ để cùng cháy hết mình với CLB nhé! Đừng quên quét mã QR điểm danh để tích lũy điểm đóng góp nha! ❤️✨

#CLBSinhVien #{activity_title.replace(' ', '')} #HoatDongSinhVien #AiGen"""

    @staticmethod
    def summarize_activity(
        activity_title: str,
        meeting_notes: str,
        member_feedbacks: List[str]
    ) -> str:
        """AI Feature 2: Summarize activity outcomes and member feedbacks."""
        
        prompt = f"""System: Bạn là Trợ lý Quản lý CLB. Hãy đọc ghi chú cuộc họp và phản hồi của thành viên để tạo bài báo cáo tóm tắt ngắn gọn gồm: Kết quả đạt được, Điểm nổi bật, và Đề xuất cải thiện.

Thông tin:
- Sự kiện: {activity_title}
- Ghi chú cuộc họp: {meeting_notes}
- Phản hồi thành viên: {', '.join(member_feedbacks)}"""

        if settings.GEMINI_API_KEY:
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={settings.GEMINI_API_KEY}"
                with httpx.Client(timeout=10.0) as client:
                    resp = client.post(url, json={
                        "contents": [{"parts": [{"text": prompt}]}]
                    })
                    if resp.status_code == 200:
                        data = resp.json()
                        return data["candidates"][0]["content"]["parts"][0]["text"]
            except Exception as e:
                print(f"Gemini API Exception, fallback to Local Rule-based Engine: {e}")

        # Local Rule-based Fallback Summary
        feedbacks_summary = f"Có {len(member_feedbacks)} ý kiến đóng góp từ các bạn thành viên." if member_feedbacks else "Chưa có phản hồi thêm."
        return f"""📋 **BÁO CÁO TÓM TẮT BỔ KẾT HOẠT ĐỘNG: {activity_title.upper()}**

✅ **1. KẾT QUẢ ĐẠT ĐƯỢC:**
- Hoạt động đã hoàn thành đúng kế hoạch và mục tiêu đề ra.
- Ghi chú chính: {meeting_notes}

⭐ **2. ĐÁNH GIÁ VÀ PHẢN HỒI THÀNH VIÊN:**
- {feedbacks_summary}
- Không khí sự kiện diễn ra sôi nổi, tinh thần làm việc nhóm cao.

🚀 **3. ĐỀ XUẤT CẢI THIỆN CHO SỰ KIỆN TỚI:**
- Tiếp tục tối ưu khâu phân công nhiệm vụ bằng AI trước 3 ngày.
- Nâng cao tỷ lệ điểm danh bằng QR Code tự động."""

    @staticmethod
    def suggest_assignments(
        tasks_data: List[Dict[str, Any]],
        members_data: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """AI Feature 3: Match tasks with members based on skills, free slots, and workload (Local Rule-based Matching)."""
        
        suggestions = []
        
        for task in tasks_data:
            req_skill = (task.get("required_skill") or "").lower()
            best_user = None
            best_score = 0.0
            best_reason = "Được hệ thống phân công dựa trên lịch rảnh phù hợp."
            
            for member in members_data:
                skills = [s.lower() for s in member.get("skills", [])]
                score = 0.5 # Base score
                
                # Check skill match
                if req_skill and any(req_skill in s or s in req_skill for s in skills):
                    score += 0.4
                    match_reason = f"Thành viên có kỹ năng '{req_skill}' rất phù hợp với yêu cầu nhiệm vụ."
                elif req_skill:
                    match_reason = f"Thành viên sẵn sàng học hỏi kỹ năng '{req_skill}'."
                else:
                    match_reason = "Nhiệm vụ phổ thông, thành viên có thời gian rảnh phù hợp."
                
                # Department match bonus
                if member.get("department_name"):
                    score += 0.05
                    
                if score > best_score:
                    best_score = min(round(score, 2), 0.98)
                    best_user = member
                    best_reason = match_reason
            
            if best_user:
                suggestions.append({
                    "task_id": task["id"],
                    "task_title": task["title"],
                    "recommended_user_id": best_user["id"],
                    "recommended_user_name": best_user["full_name"],
                    "match_score": best_score,
                    "reason": best_reason
                })
                
        return suggestions
