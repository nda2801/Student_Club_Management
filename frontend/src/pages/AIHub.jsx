import React, { useState, useEffect } from 'react';
import { Sparkles, MessageSquare, FileText, UserCheck, Copy, Check, Wand2, RefreshCw } from 'lucide-react';
import { api } from '../api/client';
import { useToast } from '../context/ToastContext';

export default function AIHub({ initialTab = 'suggest' }) {
  const toast = useToast();
  const [activeTab, setActiveTab] = useState(initialTab);
  const [loading, setLoading] = useState(false);
  const [copied, setCopied] = useState(false);

  // Tab 1: AI Announcement
  const [annTitle, setAnnTitle] = useState('Chào tân sinh viên & Workshop AI 2026');
  const [annDesc, setAnnDesc] = useState('Sự kiện chào mừng sinh viên khóa mới kết hợp chia sẻ ứng dụng AI trong học tập và làm việc.');
  const [annTime, setAnnTime] = useState('18:00 - Thứ Bảy, Ngày 15/08/2026');
  const [annLoc, setAnnLoc] = useState('Hội trường A1 - Trường Đại học');
  const [annTone, setAnnTone] = useState('enthusiastic');
  const [annResult, setAnnResult] = useState('');

  // Tab 2: AI Summary
  const [sumTitle, setSumTitle] = useState('Cuộc thi Hackathon CLB Sinh viên 2026');
  const [sumNotes, setSumNotes] = useState('Có 15 đội tham gia. Các đội hoàn thành đúng hạn 12 sản phẩm. Khâu âm thanh hội trường gặp sự cố nhỏ lúc mở màn nhưng đã khắc phục.');
  const [sumFeedbacks, setSumFeedbacks] = useState('Sự kiện rất bổ ích, Mong muốn CLB tổ chức thêm buổi hướng dẫn Prompting, Thời gian thi 24h hơi gấp nhưng rất vui.');
  const [sumResult, setSumResult] = useState('');

  // Tab 3: AI Assignment
  const [activities, setActivities] = useState([]);
  const [selectedActId, setSelectedActId] = useState('');
  const [aiSuggestions, setAiSuggestions] = useState([]);

  useEffect(() => {
    async function loadActs() {
      try {
        const data = await api.getActivities();
        setActivities(data || []);
        if (data?.length > 0) setSelectedActId(data[0].id);
      } catch (err) {
        console.error(err);
      }
    }
    loadActs();
  }, []);

  const handleGenerateAnnouncement = async (e) => {
    e.preventDefault();
    try {
      setLoading(true);
      const res = await api.generateAnnouncement({
        activity_title: annTitle,
        activity_description: annDesc,
        start_time: annTime,
        location: annLoc,
        tone: annTone
      });
      setAnnResult(res.result);
      toast.success('AI đã hoàn thành bản thảo thông báo truyền thông!', 'Sinh nội dung AI');
    } catch (err) {
      toast.error(err.message || 'Lỗi khi sinh thông báo', 'Lỗi AI Agent');
    } finally {
      setLoading(false);
    }
  };

  const handleSummarize = async (e) => {
    e.preventDefault();
    try {
      setLoading(true);
      const res = await api.summarizeActivity({
        activity_title: sumTitle,
        meeting_notes: sumNotes,
        member_feedbacks: sumFeedbacks.split(',').map((s) => s.trim())
      });
      setSumResult(res.result);
      toast.success('Đã tổng hợp báo cáo và rút ra bài học kinh nghiệm!', 'Tóm tắt sự kiện');
    } catch (err) {
      toast.error(err.message || 'Lỗi khi tóm tắt', 'Lỗi AI Agent');
    } finally {
      setLoading(false);
    }
  };

  const handleSuggestAssignments = async () => {
    if (!selectedActId) return;
    try {
      setLoading(true);
      const tasks = await api.getTasks(parseInt(selectedActId));
      if (!tasks || tasks.length === 0) {
        toast.warning('Sự kiện này chưa có nhiệm vụ nào. Hãy vào Kanban để tạo task trước!', 'Chưa có task');
        setLoading(false);
        return;
      }

      const res = await api.suggestAssignments({
        activity_id: parseInt(selectedActId),
        task_ids: tasks.map((t) => t.id)
      });
      setAiSuggestions(res.suggestions || []);
      toast.success(`Đã phân tích ${res.suggestions?.length || 0} nhiệm vụ khớp với Skill Matrix!`, 'Phân tích AI');
    } catch (err) {
      toast.error(err.message || 'Lỗi gợi ý phân công', 'Lỗi AI Agent');
    } finally {
      setLoading(false);
    }
  };

  const handleApplyAssignment = async (sugg) => {
    try {
      await api.assignTask({
        task_id: sugg.task_id,
        user_id: sugg.recommended_user_id,
        ai_suggested: true,
        match_score: sugg.match_score
      });
      toast.success(`Đã duyệt phân công '${sugg.task_title}' cho ${sugg.recommended_user_name}!`, 'Phân công thành công');
    } catch (err) {
      toast.error(err.message || 'Duyệt thất bại', 'Lỗi');
    }
  };

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
    setCopied(true);
    toast.info('Đã sao chép nội dung vào khay nhớ tạm (Clipboard)!', 'Đã copy');
    setTimeout(() => setCopied(false), 2000);
  };

  const toneOptions = [
    { id: 'enthusiastic', label: 'Hào hứng 🔥' },
    { id: 'formal', label: 'Trang trọng 🏛️' },
    { id: 'friendly', label: 'Gần gũi 💬' },
    { id: 'urgent', label: 'Khẩn cấp ⚡' }
  ];

  return (
    <div className="animate-fade-in" style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-lg)' }}>
      <div>
        <h2 style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--text-main)', display: 'flex', alignItems: 'center', gap: '8px', letterSpacing: '-0.02em' }}>
          <Sparkles color="var(--accent)" /> Trợ Lý AI Agent (AI Hub)
        </h2>
        <p style={{ fontSize: '0.875rem', color: 'var(--text-muted)', marginTop: '2px' }}>
          Tự động hóa sinh bài viết truyền thông, khớp Skill Matrix phân công nhiệm vụ và tổng kết hoạt động sau sự kiện
        </p>
      </div>

      {/* Tabs Switcher */}
      <div style={{ display: 'flex', gap: 'var(--space-xs)', borderBottom: '1px solid var(--border-color)', paddingBottom: '12px' }}>
        <button
          onClick={() => setActiveTab('suggest')}
          className={`btn ${activeTab === 'suggest' ? 'btn-ai' : 'btn-secondary'}`}
        >
          <UserCheck size={16} /> 1. Gợi Ý Phân Công AI
        </button>
        <button
          onClick={() => setActiveTab('announcement')}
          className={`btn ${activeTab === 'announcement' ? 'btn-ai' : 'btn-secondary'}`}
        >
          <MessageSquare size={16} /> 2. Sinh Thông Báo AI
        </button>
        <button
          onClick={() => setActiveTab('summary')}
          className={`btn ${activeTab === 'summary' ? 'btn-ai' : 'btn-secondary'}`}
        >
          <FileText size={16} /> 3. Tóm Tắt Hoạt Động AI
        </button>
      </div>

      {/* TAB 1: AI Suggest Assignments */}
      {activeTab === 'suggest' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
          <div className="club-card">
            <h3 style={{ fontSize: '1.1rem', fontWeight: 700, marginBottom: '12px', color: 'var(--text-main)' }}>
              🎯 AI Phân Tích Skill Matrix & Lịch Rảnh Để Gợi Ý Phân Công
            </h3>
            <div style={{ display: 'flex', gap: '12px', alignItems: 'center' }}>
              <select
                value={selectedActId}
                onChange={(e) => setSelectedActId(e.target.value)}
                style={{
                  flex: 1,
                  padding: '10px 14px',
                  fontSize: '0.9rem'
                }}
              >
                {activities.map((a) => (
                  <option key={a.id} value={a.id}>{a.title}</option>
                ))}
              </select>
              <button
                onClick={handleSuggestAssignments}
                disabled={loading}
                className="btn btn-ai"
                style={{ padding: '10px 20px' }}
              >
                {loading ? 'AI Đang Phân Tích...' : 'Chạy AI Phân Công'}
              </button>
            </div>
          </div>

          {/* AI Suggestion Cards Result */}
          {aiSuggestions.length > 0 && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              <h4 style={{ fontSize: '1rem', fontWeight: 700, color: 'var(--text-secondary)' }}>Kết Quả Gợi Ý Từ AI Agent:</h4>
              {aiSuggestions.map((sugg, idx) => (
                <div key={idx} className="club-card club-card-hover animate-fade-in" style={{
                  padding: '16px 20px',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center'
                }}>
                  <div>
                    <div style={{ fontSize: '0.95rem', fontWeight: 700, color: 'var(--text-main)' }}>
                      Nhiệm vụ: {sugg.task_title}
                    </div>
                    <div style={{ fontSize: '0.875rem', color: 'var(--primary)', fontWeight: 600, marginTop: '2px' }}>
                      👉 Khuyên giao cho: <strong>{sugg.recommended_user_name}</strong>
                    </div>
                    <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginTop: '4px' }}>
                      💡 Lý do AI: {sugg.reason}
                    </div>
                  </div>

                  <div style={{ textAlign: 'right', display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: '8px' }}>
                    <span className="badge badge-ai" style={{ fontSize: '0.75rem', padding: '4px 10px' }}>
                      Độ khớp: {Math.round(sugg.match_score * 100)}%
                    </span>
                    <button
                      onClick={() => handleApplyAssignment(sugg)}
                      className="btn btn-primary"
                      style={{ fontSize: '0.8rem', padding: '6px 14px' }}
                    >
                      Duyệt Phân Công
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* TAB 2: AI Generate Announcement */}
      {activeTab === 'announcement' && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 'var(--space-md)' }}>
          <form onSubmit={handleGenerateAnnouncement} className="club-card" style={{
            display: 'flex',
            flexDirection: 'column',
            gap: '12px'
          }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: 700, color: 'var(--text-main)' }}>Nhập Thông Tin Sự Kiện Thô</h3>
            <input
              type="text"
              placeholder="Tên sự kiện"
              required
              value={annTitle}
              onChange={(e) => setAnnTitle(e.target.value)}
              style={{ width: '100%', padding: '10px 14px' }}
            />
            <textarea
              placeholder="Mô tả tóm tắt"
              rows={3}
              value={annDesc}
              onChange={(e) => setAnnDesc(e.target.value)}
              style={{ width: '100%', padding: '10px 14px' }}
            />
            <input
              type="text"
              placeholder="Thời gian"
              value={annTime}
              onChange={(e) => setAnnTime(e.target.value)}
              style={{ width: '100%', padding: '10px 14px' }}
            />
            <input
              type="text"
              placeholder="Địa điểm"
              value={annLoc}
              onChange={(e) => setAnnLoc(e.target.value)}
              style={{ width: '100%', padding: '10px 14px' }}
            />

            <div>
              <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: 'var(--text-secondary)', marginBottom: '6px' }}>
                Chọn Văn Phong Thông Báo:
              </label>
              <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
                {toneOptions.map((tone) => (
                  <button
                    key={tone.id}
                    type="button"
                    onClick={() => setAnnTone(tone.id)}
                    style={{
                      padding: '6px 12px',
                      borderRadius: 'var(--rounded-full)',
                      border: annTone === tone.id ? '1px solid var(--accent)' : '1px solid var(--border-color)',
                      background: annTone === tone.id ? 'var(--tint-purple-bg)' : 'var(--bg-card)',
                      color: annTone === tone.id ? 'var(--tint-purple-text)' : 'var(--text-secondary)',
                      fontWeight: annTone === tone.id ? 700 : 500,
                      fontSize: '0.8rem',
                      cursor: 'pointer',
                      transition: 'all 0.15s ease'
                    }}
                  >
                    {tone.label}
                  </button>
                ))}
              </div>
            </div>

            <button type="submit" disabled={loading} className="btn btn-ai" style={{ padding: '12px', marginTop: '8px' }}>
              {loading ? 'AI Đang Soạn Bài...' : '✨ Sinh Bài Đăng AI Ngay'}
            </button>
          </form>

          {/* Result Output Card */}
          <div className="club-card" style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px' }}>
                <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: 'var(--text-main)', display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <Sparkles size={18} color="var(--accent)" /> Bài Viết Truyền Thông Đã Sinh
                </h3>
                {annResult && (
                  <button
                    onClick={() => copyToClipboard(annResult)}
                    className="btn btn-secondary"
                    style={{ padding: '6px 12px', fontSize: '0.75rem' }}
                  >
                    {copied ? <Check size={14} color="var(--success)" /> : <Copy size={14} />} {copied ? 'Đã chép' : 'Sao chép'}
                  </button>
                )}
              </div>

              {loading ? (
                <div style={{ padding: '40px 20px', textAlign: 'center', color: 'var(--text-muted)' }}>
                  <Wand2 size={32} className="animate-spin" color="var(--accent)" style={{ margin: '0 auto 12px' }} />
                  <p style={{ fontWeight: 600, color: 'var(--text-main)' }}>AI đang phân tích và soạn bài đăng hấp dẫn...</p>
                  <p style={{ fontSize: '0.8rem', marginTop: '4px' }}>Đang tối ưu cấu trúc bài đăng, icon và CTA tham gia</p>
                </div>
              ) : annResult ? (
                <div style={{
                  background: 'var(--bg-card-secondary)',
                  padding: '16px',
                  borderRadius: 'var(--rounded-md)',
                  border: '1px solid var(--border-color)',
                  whiteSpace: 'pre-wrap',
                  fontSize: '0.88rem',
                  lineHeight: 1.6,
                  color: 'var(--text-main)',
                  maxHeight: '420px',
                  overflowY: 'auto'
                }}>
                  {annResult}
                </div>
              ) : (
                <div style={{ padding: '40px 20px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '0.85rem' }}>
                  Điền thông tin sự kiện bên trái và nhấn <strong>'Sinh Bài Đăng AI'</strong> để nhận bài viết hoàn chỉnh.
                </div>
              )}
            </div>

            {annResult && (
              <div style={{ marginTop: '16px', fontSize: '0.75rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '6px' }}>
                <span style={{ color: 'var(--success)', fontWeight: 700 }}>✓</span> Đã định dạng sẵn CTA, hashtag và biểu tượng cảm xúc sẵn sàng đăng Fanpage.
              </div>
            )}
          </div>
        </div>
      )}

      {/* TAB 3: AI Summarize Activity */}
      {activeTab === 'summary' && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 'var(--space-md)' }}>
          <form onSubmit={handleSummarize} className="club-card" style={{
            display: 'flex',
            flexDirection: 'column',
            gap: '12px'
          }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: 700, color: 'var(--text-main)' }}>Thông Tin Sau Sự Kiện</h3>
            <input
              type="text"
              placeholder="Tên sự kiện đã diễn ra"
              required
              value={sumTitle}
              onChange={(e) => setSumTitle(e.target.value)}
              style={{ width: '100%', padding: '10px 14px' }}
            />
            <textarea
              placeholder="Ghi chú cuộc họp rút kinh nghiệm"
              rows={4}
              value={sumNotes}
              onChange={(e) => setSumNotes(e.target.value)}
              style={{ width: '100%', padding: '10px 14px' }}
            />
            <textarea
              placeholder="Ý kiến phản hồi của các thành viên (ngăn cách bằng dấu phẩy)"
              rows={3}
              value={sumFeedbacks}
              onChange={(e) => setSumFeedbacks(e.target.value)}
              style={{ width: '100%', padding: '10px 14px' }}
            />

            <button type="submit" disabled={loading} className="btn btn-ai" style={{ padding: '12px', marginTop: '8px' }}>
              {loading ? 'AI Đang Tổng Hợp...' : '📊 Tóm Tắt & Rút Kinh Nghiệm AI'}
            </button>
          </form>

          {/* Summary Output Card */}
          <div className="club-card" style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px' }}>
                <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: 'var(--text-main)', display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <FileText size={18} color="var(--primary)" /> Báo Cáo Tổng Kết AI
                </h3>
                {sumResult && (
                  <button
                    onClick={() => copyToClipboard(sumResult)}
                    className="btn btn-secondary"
                    style={{ padding: '6px 12px', fontSize: '0.75rem' }}
                  >
                    {copied ? <Check size={14} color="var(--success)" /> : <Copy size={14} />} {copied ? 'Đã chép' : 'Sao chép'}
                  </button>
                )}
              </div>

              {loading ? (
                <div style={{ padding: '40px 20px', textAlign: 'center', color: 'var(--text-muted)' }}>
                  <RefreshCw size={32} className="animate-spin" color="var(--primary)" style={{ margin: '0 auto 12px' }} />
                  <p style={{ fontWeight: 600, color: 'var(--text-main)' }}>AI đang phân tích phản hồi và đúc kết bài học...</p>
                </div>
              ) : sumResult ? (
                <div style={{
                  background: 'var(--bg-card-secondary)',
                  padding: '16px',
                  borderRadius: 'var(--rounded-md)',
                  border: '1px solid var(--border-color)',
                  whiteSpace: 'pre-wrap',
                  fontSize: '0.88rem',
                  lineHeight: 1.6,
                  color: 'var(--text-main)',
                  maxHeight: '420px',
                  overflowY: 'auto'
                }}>
                  {sumResult}
                </div>
              ) : (
                <div style={{ padding: '40px 20px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '0.85rem' }}>
                  Nhập ghi chú cuộc họp và phản hồi bên trái để AI tự động trích xuất các điểm mạnh, thiếu sót và đề xuất hành động.
                </div>
              )}
            </div>

            {sumResult && (
              <div style={{ marginTop: '16px', fontSize: '0.75rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '6px' }}>
                <span style={{ color: 'var(--primary)', fontWeight: 700 }}>●</span> Dữ liệu được cấu trúc theo phương pháp Retrospective tiêu chuẩn.
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
