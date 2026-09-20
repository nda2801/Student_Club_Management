import React, { useState } from 'react';
import { UserCheck, Sparkles, Lock, Search, Filter, CheckCircle, ArrowRight, User } from 'lucide-react';
import { api } from '../api/client';
import { useToast } from '../context/ToastContext';

export default function KanbanBoard({ tasks, members, currentUser, onTaskUpdated }) {
  const toast = useToast();
  const [searchQuery, setSearchQuery] = useState('');
  const [filterMyTasks, setFilterMyTasks] = useState(false);

  const columns = [
    { id: 'TO_DO', title: 'Cần Làm (To Do)', color: 'var(--text-muted)', bg: 'var(--tint-blue-bg)' },
    { id: 'IN_PROGRESS', title: 'Đang Thực Hiện', color: 'var(--primary)', bg: 'var(--tint-blue-bg)' },
    { id: 'DONE', title: 'Hoàn Thành', color: 'var(--success)', bg: 'var(--tint-green-bg)' }
  ];

  const isAdminOrLeader = currentUser?.role === 'ADMIN' || currentUser?.role === 'LEADER';

  const handleStatusChange = async (taskId, newStatus, taskTitle) => {
    try {
      await api.updateTaskStatus(taskId, newStatus);
      const statusLabel = newStatus === 'DONE' ? 'Hoàn Thành' : newStatus === 'IN_PROGRESS' ? 'Đang Thực Hiện' : 'Cần Làm';
      toast.success(`Đã chuyển '${taskTitle}' sang '${statusLabel}'!`, 'Tiến độ Kanban');
      if (onTaskUpdated) onTaskUpdated();
    } catch (err) {
      toast.error(err.message || 'Không thể cập nhật trạng thái', 'Lỗi cập nhật');
    }
  };

  const handleAssignMember = async (taskId, userId, taskTitle) => {
    if (!isAdminOrLeader) {
      toast.warning('Chỉ Ban chủ nhiệm và Trưởng ban mới có quyền phân công nhiệm vụ!', 'Quyền hạn');
      return;
    }
    try {
      await api.assignTask({
        task_id: taskId,
        user_id: parseInt(userId),
        ai_suggested: false,
        match_score: 1.0
      });
      const member = members.find((m) => m.id === parseInt(userId));
      toast.success(`Đã giao '${taskTitle}' cho ${member?.full_name || 'thành viên'}!`, 'Phân công nhiệm vụ');
      if (onTaskUpdated) onTaskUpdated();
    } catch (err) {
      toast.error(err.message || 'Phân công thất bại', 'Lỗi phân công');
    }
  };

  const filteredTasks = tasks.filter((task) => {
    const q = searchQuery.toLowerCase();
    const matchesQuery = !searchQuery || 
      task.title?.toLowerCase().includes(q) || 
      task.description?.toLowerCase().includes(q) || 
      task.required_skill?.toLowerCase().includes(q) ||
      task.assigned_user_name?.toLowerCase().includes(q);

    const matchesMyFilter = !filterMyTasks || task.assigned_user_id === currentUser?.id;
    return matchesQuery && matchesMyFilter;
  });

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)', width: '100%' }}>
      {/* Search & Filter Subbar */}
      <div className="club-card" style={{
        padding: '10px 16px',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        gap: 'var(--space-sm)'
      }}>
        <div style={{ position: 'relative', flex: 1, maxWidth: '380px' }}>
          <Search size={16} style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
          <input
            type="text"
            placeholder="Tìm theo tên task, kỹ năng, hoặc thành viên..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            style={{
              width: '100%',
              padding: '8px 12px 8px 36px',
              fontSize: '0.85rem'
            }}
          />
        </div>

        <div style={{ display: 'flex', gap: '8px' }}>
          <button
            onClick={() => setFilterMyTasks(!filterMyTasks)}
            className={`btn ${filterMyTasks ? 'btn-primary' : 'btn-secondary'}`}
            style={{ padding: '7px 14px', fontSize: '0.8rem' }}
          >
            <User size={14} /> {filterMyTasks ? 'Đang lọc task của tôi' : 'Chỉ task của tôi'}
          </button>
        </div>
      </div>

      {/* 3 Kanban Columns Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 'var(--space-md)', width: '100%' }}>
        {columns.map((col) => {
          const colTasks = filteredTasks.filter((t) => t.status === col.id);

          return (
            <div key={col.id} className="club-card" style={{
              padding: '16px',
              display: 'flex',
              flexDirection: 'column',
              gap: 'var(--space-sm)',
              minHeight: '440px'
            }}>
              <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                paddingBottom: '12px',
                borderBottom: '1px solid var(--border-subtle)'
              }}>
                <h4 style={{ fontSize: '0.95rem', fontWeight: 700, color: col.color, display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <span style={{ width: '8px', height: '8px', borderRadius: 'var(--rounded-full)', background: col.color }}></span>
                  {col.title}
                </h4>
                <span style={{
                  background: 'var(--bg-card-secondary)',
                  color: col.color,
                  border: '1px solid var(--border-color)',
                  padding: '2px 8px',
                  borderRadius: 'var(--rounded-full)',
                  fontSize: '0.75rem',
                  fontWeight: 700
                }}>
                  {colTasks.length}
                </span>
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-sm)', flex: 1 }}>
                {colTasks.map((task) => {
                  const isAssignedToMe = task.assigned_user_id === currentUser?.id;
                  const canChangeStatus = isAdminOrLeader || isAssignedToMe;

                  return (
                    <div key={task.id} className="animate-fade-in" style={{
                      background: 'var(--bg-card-secondary)',
                      borderRadius: 'var(--rounded-md)',
                      padding: '14px',
                      border: isAssignedToMe ? '2px solid var(--primary)' : '1px solid var(--border-color)',
                      boxShadow: 'var(--shadow-sm)',
                      position: 'relative',
                      transition: 'all 0.2s ease'
                    }}>
                      {isAssignedToMe && (
                        <div style={{
                          position: 'absolute',
                          top: '-10px',
                          right: '10px',
                          background: 'var(--primary)',
                          color: 'white',
                          fontSize: '0.65rem',
                          fontWeight: 700,
                          padding: '2px 8px',
                          borderRadius: 'var(--rounded-full)',
                          boxShadow: '0 2px 6px rgba(37,99,235,0.35)'
                        }}>
                          Nhiệm Vụ Của Bạn
                        </div>
                      )}

                      <div style={{ fontSize: '0.9rem', fontWeight: 700, color: 'var(--text-main)', marginBottom: '4px', paddingRight: isAssignedToMe ? '70px' : '0' }}>
                        {task.title}
                      </div>
                      {task.description && (
                        <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginBottom: '8px', lineHeight: 1.4 }}>
                          {task.description}
                        </div>
                      )}

                      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px', marginBottom: '10px' }}>
                        {task.required_skill && (
                          <span style={{
                            fontSize: '0.7rem',
                            background: 'var(--tint-blue-bg)',
                            color: 'var(--tint-blue-text)',
                            border: '1px solid var(--tint-blue-border)',
                            padding: '2px 8px',
                            borderRadius: 'var(--rounded-xs)',
                            fontWeight: 600
                          }}>
                            Skill: {task.required_skill}
                          </span>
                        )}
                        {task.ai_suggested && (
                          <span className="badge badge-ai" style={{ fontSize: '0.65rem' }}>
                            <Sparkles size={10} /> AI Gợi ý ({Math.round((task.match_score || 1) * 100)}%)
                          </span>
                        )}
                      </div>

                      {/* Member Assignment Section */}
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginTop: '8px', paddingTop: '8px', borderTop: '1px dashed var(--border-color)' }}>
                        <div style={{
                          width: '24px',
                          height: '24px',
                          borderRadius: '50%',
                          background: task.assigned_user_name ? 'linear-gradient(135deg, #3b82f6, #6366f1)' : 'var(--border-color)',
                          color: '#ffffff',
                          fontSize: '0.7rem',
                          fontWeight: 700,
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          flexShrink: 0
                        }}>
                          {task.assigned_user_name ? task.assigned_user_name.charAt(0) : '?'}
                        </div>

                        {isAdminOrLeader ? (
                          <select
                            value={task.assigned_user_id || ''}
                            onChange={(e) => handleAssignMember(task.id, e.target.value, task.title)}
                            style={{
                              fontSize: '0.75rem',
                              padding: '5px 8px',
                              borderRadius: 'var(--rounded-sm)',
                              border: '1px solid var(--border-input)',
                              background: 'var(--bg-input)',
                              flex: 1,
                              color: task.assigned_user_id ? 'var(--text-main)' : 'var(--text-muted)'
                            }}
                          >
                            <option value="">-- Chọn thành viên --</option>
                            {members.map((m) => (
                              <option key={m.id} value={m.id}>
                                {m.full_name} ({m.department_name})
                              </option>
                            ))}
                          </select>
                        ) : (
                          <div style={{ fontSize: '0.75rem', color: task.assigned_user_name ? 'var(--text-main)' : 'var(--text-muted)', fontWeight: task.assigned_user_name ? 600 : 400 }}>
                            {task.assigned_user_name ? (
                              <span>Đã giao: <strong>{task.assigned_user_name}</strong></span>
                            ) : (
                              <span style={{ fontStyle: 'italic' }}>Chưa phân công</span>
                            )}
                          </div>
                        )}
                      </div>

                      {/* Status Change Buttons */}
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '10px' }}>
                        {!canChangeStatus && (
                          <span style={{ fontSize: '0.7rem', color: 'var(--text-light)', display: 'flex', alignItems: 'center', gap: '4px', fontStyle: 'italic' }}>
                            <Lock size={12} /> Chỉ đọc
                          </span>
                        )}

                        {canChangeStatus && (
                          <div style={{ display: 'flex', gap: '4px', marginLeft: 'auto' }}>
                            {col.id !== 'TO_DO' && (
                              <button
                                onClick={() => handleStatusChange(task.id, 'TO_DO', task.title)}
                                style={{
                                  fontSize: '0.7rem',
                                  padding: '4px 8px',
                                  background: 'var(--bg-card)',
                                  border: '1px solid var(--border-color)',
                                  borderRadius: 'var(--rounded-xs)',
                                  color: 'var(--text-secondary)',
                                  fontWeight: 500,
                                  cursor: 'pointer'
                                }}
                              >
                                ← To Do
                              </button>
                            )}
                            {col.id !== 'IN_PROGRESS' && (
                              <button
                                onClick={() => handleStatusChange(task.id, 'IN_PROGRESS', task.title)}
                                style={{
                                  fontSize: '0.7rem',
                                  padding: '4px 8px',
                                  background: 'var(--tint-blue-bg)',
                                  border: '1px solid var(--tint-blue-border)',
                                  borderRadius: 'var(--rounded-xs)',
                                  color: 'var(--tint-blue-text)',
                                  fontWeight: 600,
                                  cursor: 'pointer'
                                }}
                              >
                                ⚡ Tiến hành
                              </button>
                            )}
                            {col.id !== 'DONE' && (
                              <button
                                onClick={() => handleStatusChange(task.id, 'DONE', task.title)}
                                style={{
                                  fontSize: '0.7rem',
                                  padding: '4px 8px',
                                  background: 'var(--tint-green-bg)',
                                  border: '1px solid var(--tint-green-border)',
                                  borderRadius: 'var(--rounded-xs)',
                                  color: 'var(--tint-green-text)',
                                  fontWeight: 700,
                                  cursor: 'pointer'
                                }}
                              >
                                ✓ Hoàn thành
                              </button>
                            )}
                          </div>
                        )}
                      </div>
                    </div>
                  );
                })}

                {colTasks.length === 0 && (
                  <div style={{ textAlign: 'center', padding: '32px 0', color: 'var(--text-muted)', fontSize: '0.85rem', fontStyle: 'italic' }}>
                    Chưa có nhiệm vụ
                  </div>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
