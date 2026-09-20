import React, { useState, useEffect } from 'react';
import { Plus, Sparkles, ShieldAlert } from 'lucide-react';
import { api } from '../api/client';
import KanbanBoard from '../components/KanbanBoard';
import { useToast } from '../context/ToastContext';

export default function Tasks({ currentUser, onNavigateToAiHub }) {
  const toast = useToast();
  const [tasks, setTasks] = useState([]);
  const [members, setMembers] = useState([]);
  const [activities, setActivities] = useState([]);
  const [selectedActivityId, setSelectedActivityId] = useState('');
  const [showCreateModal, setShowCreateModal] = useState(false);

  // Form states
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [requiredSkill, setRequiredSkill] = useState('');
  const [activityId, setActivityId] = useState('');

  const isAdminOrLeader = currentUser?.role === 'ADMIN' || currentUser?.role === 'LEADER';

  const loadData = async () => {
    try {
      const [tList, mList, aList] = await Promise.all([
        api.getTasks(selectedActivityId ? parseInt(selectedActivityId) : null),
        api.getMembers(),
        api.getActivities()
      ]);
      setTasks(tList || []);
      setMembers(mList || []);
      setActivities(aList || []);
      if (aList?.length > 0 && !activityId) {
        setActivityId(aList[0].id);
      }
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    loadData();
  }, [selectedActivityId]);

  const handleCreateTask = async (e) => {
    e.preventDefault();
    if (!isAdminOrLeader) {
      toast.warning('Chỉ Ban chủ nhiệm và Trưởng ban mới có quyền tạo nhiệm vụ!', 'Quyền hạn');
      return;
    }
    try {
      await api.createTask({
        activity_id: parseInt(activityId),
        title,
        description,
        required_skill: requiredSkill,
        status: 'TO_DO'
      });
      toast.success(`Đã thêm nhiệm vụ '${title}' vào hàng đợi Kanban!`, 'Tạo task thành công');
      setShowCreateModal(false);
      setTitle('');
      setDescription('');
      setRequiredSkill('');
      loadData();
    } catch (err) {
      toast.error(err.message || 'Tạo nhiệm vụ thất bại', 'Lỗi tạo task');
    }
  };

  return (
    <div className="animate-fade-in" style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-lg)' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h2 style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--text-main)', letterSpacing: '-0.02em' }}>
            Nhiệm Vụ
          </h2>
          <p style={{ fontSize: '0.875rem', color: 'var(--text-muted)', marginTop: '2px' }}>
            {isAdminOrLeader
              ? 'Quản lý, phân công và theo dõi tiến độ công việc toàn bộ CLB'
              : 'Xem nhiệm vụ của bạn và cập nhật tiến độ công việc được giao'}
          </p>
        </div>

        <div style={{ display: 'flex', gap: 'var(--space-xs)' }}>
          {isAdminOrLeader && (
            <>
              <button
                onClick={() => onNavigateToAiHub('suggest')}
                className="btn btn-ai"
              >
                <Sparkles size={16} /> Gợi Ý Phân Công AI
              </button>

              <button
                onClick={() => setShowCreateModal(true)}
                className="btn btn-primary"
              >
                <Plus size={18} /> Thêm Task Mới
              </button>
            </>
          )}
        </div>
      </div>

      {!isAdminOrLeader && (
        <div style={{
          background: 'var(--tint-blue-bg)',
          border: '1px solid var(--tint-blue-border)',
          borderRadius: 'var(--rounded-md)',
          padding: '10px 14px',
          fontSize: '0.85rem',
          color: 'var(--tint-blue-text)',
          display: 'flex',
          alignItems: 'center',
          gap: '8px'
        }}>
          <ShieldAlert size={16} /> Bạn đang xem với vai trò <strong>Thành Viên</strong>. Bạn chỉ có quyền chuyển trạng thái nhiệm vụ được phân công cho chính mình.
        </div>
      )}

      {/* Filter by Activity */}
      <div className="club-card" style={{
        padding: '12px 18px',
        display: 'flex',
        alignItems: 'center',
        gap: 'var(--space-sm)'
      }}>
        <span style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-secondary)' }}>Lọc theo sự kiện:</span>
        <select
          value={selectedActivityId}
          onChange={(e) => setSelectedActivityId(e.target.value)}
          style={{
            padding: '8px 12px',
            fontSize: '0.85rem',
            flex: 1
          }}
        >
          <option value="">Tất cả sự kiện ({activities.length})</option>
          {activities.map((a) => (
            <option key={a.id} value={a.id}>{a.title}</option>
          ))}
        </select>
      </div>

      {/* Kanban Board Component */}
      <KanbanBoard tasks={tasks} members={members} currentUser={currentUser} onTaskUpdated={loadData} />

      {/* Create Task Modal */}
      {showCreateModal && (
        <div style={{ position: 'fixed', inset: 0, background: 'var(--bg-overlay)', backdropFilter: 'blur(6px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 100 }}>
          <div className="club-card" style={{ maxWidth: '480px', width: '100%', padding: '24px', boxShadow: 'var(--shadow-lg)' }}>
            <h3 style={{ fontSize: '1.2rem', fontWeight: 700, color: 'var(--text-main)', marginBottom: '16px' }}>Thêm Nhiệm Vụ Mới</h3>
            <form onSubmit={handleCreateTask} style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              <div>
                <label style={{ fontSize: '0.8rem', fontWeight: 600, color: 'var(--text-secondary)', marginBottom: '4px', display: 'block' }}>Sự kiện thuộc về</label>
                <select
                  value={activityId}
                  onChange={(e) => setActivityId(e.target.value)}
                  style={{ width: '100%', padding: '10px 14px' }}
                >
                  {activities.map((a) => (
                    <option key={a.id} value={a.id}>{a.title}</option>
                  ))}
                </select>
              </div>

              <input
                type="text"
                placeholder="Tên nhiệm vụ"
                required
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                style={{ width: '100%', padding: '10px 14px' }}
              />

              <textarea
                placeholder="Mô tả công việc"
                rows={3}
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                style={{ width: '100%', padding: '10px 14px' }}
              />

              <input
                type="text"
                placeholder="Kỹ năng yêu cầu (vd: Thiết kế Photoshop, Setup âm thanh)"
                value={requiredSkill}
                onChange={(e) => setRequiredSkill(e.target.value)}
                style={{ width: '100%', padding: '10px 14px' }}
              />

              <div style={{ display: 'flex', gap: '8px', justifyContent: 'flex-end', marginTop: '12px' }}>
                <button type="button" onClick={() => setShowCreateModal(false)} className="btn btn-secondary">Hủy</button>
                <button type="submit" className="btn btn-primary">Lưu Nhiệm Vụ</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
