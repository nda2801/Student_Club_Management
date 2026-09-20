# GIAI ĐOẠN KT3: TÍCH HỢP TRÍ TUỆ NHÂN TẠO & KIỂM THỬ TOÀN DIỆN
## PHẠM VI: TỪ TUẦN 7 ĐẾN HẾT TUẦN 8 (07/09/2026 – 20/09/2026)

---

### 1. Mục tiêu Giai đoạn KT3
1. Tích hợp 03 tính năng AI then chốt theo kiến trúc **Dual-Engine (Cloud LLM + Local Fallback)**:
   - **FR-AI-01 (AI Sinh bài đăng thông báo):** Phân tích ngữ cảnh sự kiện, cho phép chọn Tone giọng (*Hào hứng, Trang trọng, Thân thiện*) và tự động thêm emoji sinh động.
   - **FR-AI-02 (AI Tóm tắt kết quả hoạt động):** Đọc ghi chú họp và danh sách phản hồi để xuất báo cáo 3 phần súc tích (*Ưu điểm, Tồn tại, Đề xuất cải tiến*).
   - **FR-AI-03 (AI Smart Matchmaking):** So khớp độ tương đồng kỹ năng giữa Task với Skill Matrix, kiểm tra slot rảnh và cân bằng tải công việc để xuất danh sách ghép cặp kèm Match Score (%) và lý do rõ ràng.
2. Cài đặt **Local Rule-based Fallback Engine** bằng thuật toán Heuristic trong bộ nhớ, đảm bảo hệ thống tự chuyển sang Fallback trong $< 100$ms khi mất mạng hoặc hết quota API.
3. Thiết kế **Hệ thống Phòng thủ Prompt Injection 5 tầng** và ép kiểu JSON đầu ra qua Pydantic Validation.
4. Thực hiện kiểm thử toàn diện:
   - Automated Core Regression Suite (25+ test cases).
   - Load testing 200 concurrent users với Locust / k6.
   - Đo lường thời gian phản hồi API (P95 $\le$ 500ms).

---

### 2. Kế hoạch Phân công Công việc KT3 (Nhóm 15)
- **La Văn Quyền (Lead Dev / Architect):**
  - Tích hợp Google Gemini API SDK / OpenAI API Client.
  - Viết thuật toán Local Rule-based Fallback Matcher Engine.
  - Xây dựng mô-đun lưu vết Prompt & Response vào bảng `ai_logs`.
- **Nguyễn Đức Anh (BA / UX / QA):**
  - Thiết kế và tinh chỉnh System Prompt, User Prompt cho từng tính năng AI.
  - Chạy bộ kịch bản kiểm thử Adversarial Prompt Injection và kiểm thử chịu tải 200 VUs.
