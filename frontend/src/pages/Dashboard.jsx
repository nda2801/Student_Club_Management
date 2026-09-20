import React, { useState, useEffect } from 'react';
import { Users, Building2, Calendar, CheckSquare, Sparkles, TrendingUp, ArrowRight, Clock, MapPin, CheckCircle, ChevronRight, AlertCircle } from 'lucide-react';
import { api } from '../api/client';
import { useToast } from '../context/ToastContext';

export default function Dashboard({ currentUser, onNavigate }) {
  const toast = useToast();
  const [stats, setStats] = useState(null);
  const [activities, setActivities] = useState([]);
  const [myTasks, setMyTasks] = useState([]);
  const [loading, setLoading] = useState(true);

  const getGreeting = () => {
    const hour = new Date().getHours();
    if (hour < 12) return 'Chào buổi sáng';
    if (hour < 18) return 'Chào buổi chiều';
    return 'Chào buổi tối';
  };

  const loadDashboardData = async () => {
    try {
      setLoading(true);
      const [statsData, actData, tasksData] = await Promise.all([
        api.getDashboardStats(),
        api.getActivities(),
        api.getTasks()
      ]);
      setStats(statsData);
      setActivities(actData || []);
      
      if (currentUser?.id) {
        const assigned = (tasksData || []).filter((t) => t.assigned_user_id === currentUser.id);
        setMyTasks(assigned);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadDashboardData();
  }, [currentUser?.id]);

  const handleQuickUpdateTaskStatus = async (taskId, newStatus, taskTitle) => {
    try {
      await api.updateTaskStatus(taskId, newStatus);
      const statusLabel = newStatus === 'DONE' ? 'Hoàn thành' : 'Đang thực hiện';
      toast.success(`Đã chuyển '${taskTitle}' sang '${statusLabel}'!`, 'Cập nhật tiến độ');
      loadDashboardData();
    } catch (err) {
      toast.error(err.message || 'Không thể cập nhật trạng thái', 'Lỗi');
    }
  };

  const statCards = [
    {
      title: 'Thành Viên CLB',
      value: stats?.total_members || 0,
      trend: '+12% tuần này',
      icon: Users,
      color: 'var(--primary)',
      bg: 'var(--tint-blue-bg)'
    },
    {
      title: 'Ban Chuyên Môn',
      value: stats?.total_departments || 0,
      trend: '4 ban chuyên môn',
      icon: Building2,
      color: 'var(--secondary)',
      bg: 'var(--tint-purple-bg)'
    },
    {
      title: 'Sự Kiện & Hoạt Động',
      value: stats?.total_activities || 0,
      trend: 'Mã QR động 4 lớp',
      icon: Calendar,
      color: 'var(--success)',
      bg: 'var(--tint-green-bg)'
    },
    {
      title: 'Nhiệm Vụ Đã Xong',
      value: `${stats?.completed_tasks || 0}/${stats?.total_tasks || 0}`,
      trend: 'Tiến độ đồng bộ Kanban',
      icon: CheckSquare,
      color: 'var(--accent)',
      bg: 'var(--tint-purple-bg)'
    },
  ];

  const upcomingActivities = activities.filter((a) => a.status === 'UPCOMING').slice(0, 2);

  return (
    <div className="animate-fade-in" style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-xl)' }}>
      {/* Header Banner */}
      <div className="dashboard-hero-banner">
        <div>
          <div className="dashboard-hero-badge">
            <Sparkles size={14} color="#ffd700" /> Hệ thống Tích hợp AI Agent (Nhóm 28)
          </div>
          <h2 className="dashboard-hero-title">
            {getGreeting()}, {currentUser?.full_name || 'Thành Viên'} 👋
          </h2>
          <p className="dashboard-hero-text">
            Tự động hóa vận hành câu lạc bộ với thuật toán AI đề xuất phân công, chống điểm danh hộ bằng mã QR động và giám sát tiến độ thời gian thực.
          </p>
        </div>
        <button
          onClick={() => onNavigate('aihub')}
          className="btn btn-ai"
          style={{ padding: '12px 22px', borderRadius: 'var(--rounded-md)', fontSize: '0.95rem', boxShadow: 'var(--shadow-ai)' }}
        >
          <Sparkles size={18} /> Khám Phá AI Hub <ArrowRight size={16} />
        </button>
      </div>

      {/* Stat Cards Grid with Trend Indicators */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 'var(--space-md)' }}>
        {statCards.map((card, idx) => {
          const Icon = card.icon;
          return (
            <div key={idx} className="club-card club-card-hover" style={{
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'space-between',
              gap: '12px'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)', fontWeight: 600 }}>{card.title}</span>
                <div style={{
                  width: '42px',
                  height: '42px',
                  borderRadius: 'var(--rounded-lg)',
                  background: card.bg,
                  color: card.color,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  border: '1px solid var(--border-color)'
                }}>
                  <Icon size={20} />
                </div>
              </div>

              <div>
                <div style={{ fontSize: '1.85rem', fontWeight: 800, color: 'var(--text-main)', letterSpacing: '-0.02em', lineHeight: 1 }}>
                  {loading ? '...' : card.value}
                </div>
                <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '6px', display: 'flex', alignItems: 'center', gap: '4px' }}>
                  <span style={{ color: card.color, fontWeight: 700 }}>●</span> {card.trend}
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Two Live Interactive Widgets Split */}
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 'var(--space-lg)' }}>
        {/* Widget 1: Upcoming Events */}
        <div className="club-card" style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px' }}>
              <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: 'var(--text-main)', display: 'flex', alignItems: 'center', gap: '8px' }}>
                <Calendar size={18} color="var(--primary)" /> Sự Kiện Sắp Diễn Ra
              </h3>
              <button
                onClick={() => onNavigate('activities')}
                style={{ background: 'transparent', border: 'none', color: 'var(--primary)', fontSize: '0.8rem', fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '2px' }}
              >
                Xem tất cả <ChevronRight size={14} />
              </button>
            </div>

            {upcomingActivities.length === 0 ? (
              <div style={{ padding: '24px 0', textAlign: 'center', color: 'var(--text-muted)', fontSize: '0.85rem' }}>
                Chưa có sự kiện nào sắp tới
              </div>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                {upcomingActivities.map((act) => (
                  <div key={act.id} style={{
                    padding: '12px 14px',
                    borderRadius: 'var(--rounded-md)',
                    background: 'var(--bg-card-secondary)',
                    border: '1px solid var(--border-color)',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center'
                  }}>
                    <div>
                      <div style={{ fontWeight: 700, fontSize: '0.9rem', color: 'var(--text-main)' }}>{act.title}</div>
                      <div style={{ fontSize: '0.78rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '10px', marginTop: '4px' }}>
                        <span style={{ display: 'flex', alignItems: 'center', gap: '3px' }}>
                          <Clock size={12} /> {new Date(act.start_time).toLocaleDateString('vi-VN')}
                        </span>
                        <span style={{ display: 'flex', alignItems: 'center', gap: '3px' }}>
                          <MapPin size={12} /> {act.location || 'Hội trường CLB'}
                        </span>
                      </div>
                    </div>

                    <button
                      onClick={() => onNavigate('activities')}
                      className="btn btn-primary"
                      style={{ padding: '6px 12px', fontSize: '0.75rem', borderRadius: 'var(--rounded-sm)' }}
                    >
                      Mã QR
                    </button>
                  </div>
                ))}
              </div>
            )}
          </div>

          <div style={{ marginTop: '16px', paddingTop: '12px', borderTop: '1px dashed var(--border-color)', fontSize: '0.75rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '6px' }}>
            <span style={{ width: '6px', height: '6px', borderRadius: '50%', background: 'var(--success)' }}></span>
            Mã QR độc bản chống điểm danh hộ bằng GPS & Khóa thiết bị
          </div>
        </div>

        {/* Widget 2: My Assigned Tasks */}
        <div className="club-card" style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px' }}>
              <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: 'var(--text-main)', display: 'flex', alignItems: 'center', gap: '8px' }}>
                <CheckSquare size={18} color="var(--success)" /> Nhiệm Vụ Của Bạn
              </h3>
              <button
                onClick={() => onNavigate('tasks')}
                style={{ background: 'transparent', border: 'none', color: 'var(--primary)', fontSize: '0.8rem', fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '2px' }}
              >
                Mở Nhiệm vụ <ChevronRight size={14} />
              </button>
            </div>

            {myTasks.length === 0 ? (
              <div style={{ padding: '24px 0', textAlign: 'center', color: 'var(--text-muted)', fontSize: '0.85rem' }}>
                🎉 Bạn chưa có nhiệm vụ nào tồn đọng!
              </div>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                {myTasks.slice(0, 3).map((task) => (
                  <div key={task.id} style={{
                    padding: '12px 14px',
                    borderRadius: 'var(--rounded-md)',
                    background: 'var(--bg-card-secondary)',
                    border: '1px solid var(--border-color)',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center'
                  }}>
                    <div style={{ paddingRight: '10px', flex: 1 }}>
                      <div style={{ fontWeight: 600, fontSize: '0.88rem', color: 'var(--text-main)' }}>{task.title}</div>
                      <div style={{ display: 'flex', gap: '6px', marginTop: '4px', alignItems: 'center' }}>
                        <span style={{
                          fontSize: '0.7rem',
                          padding: '1px 6px',
                          borderRadius: '4px',
                          fontWeight: 700,
                          background: task.status === 'DONE' ? 'var(--tint-green-bg)' : task.status === 'IN_PROGRESS' ? 'var(--tint-blue-bg)' : 'var(--bg-card)',
                          color: task.status === 'DONE' ? 'var(--tint-green-text)' : task.status === 'IN_PROGRESS' ? 'var(--tint-blue-text)' : 'var(--text-muted)',
                          border: '1px solid var(--border-color)'
                        }}>
                          {task.status === 'DONE' ? 'Đã Xong' : task.status === 'IN_PROGRESS' ? 'Đang Làm' : 'Cần Làm'}
                        </span>
                        {task.required_skill && (
                          <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>
                            • {task.required_skill}
                          </span>
                        )}
                      </div>
                    </div>

                    <div style={{ display: 'flex', gap: '6px' }}>
                      {task.status !== 'DONE' && (
                        <button
                          onClick={() => handleQuickUpdateTaskStatus(task.id, 'DONE', task.title)}
                          className="btn btn-primary"
                          style={{ padding: '5px 10px', fontSize: '0.75rem', borderRadius: 'var(--rounded-sm)' }}
                          title="Đánh dấu hoàn thành"
                        >
                          <CheckCircle size={13} /> Xong
                        </button>
                      )}
                      {task.status === 'TO_DO' && (
                        <button
                          onClick={() => handleQuickUpdateTaskStatus(task.id, 'IN_PROGRESS', task.title)}
                          className="btn btn-secondary"
                          style={{ padding: '5px 10px', fontSize: '0.75rem', borderRadius: 'var(--rounded-sm)' }}
                        >
                          Bắt đầu
                        </button>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>

          <div style={{ marginTop: '16px', paddingTop: '12px', borderTop: '1px dashed var(--border-color)', fontSize: '0.75rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '6px' }}>
            <span style={{ width: '6px', height: '6px', borderRadius: '50%', background: 'var(--primary)' }}></span>
            Cập nhật tức thì đồng bộ thời gian thực với Bảng Kanban
          </div>
        </div>
      </div>

      {/* Feature Quick Actions */}
      <div className="club-card">
        <h3 style={{ fontSize: '1.1rem', fontWeight: 700, color: 'var(--text-main)', marginBottom: 'var(--space-md)', display: 'flex', alignItems: 'center', gap: '8px' }}>
          <TrendingUp size={20} color="var(--primary)" /> Đơn Giản Hóa Quy Trình Với AI
        </h3>
        
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 'var(--space-md)' }}>
          <div
            onClick={() => onNavigate('aihub')}
            className="club-card-hover"
            style={{
              padding: 'var(--space-md)',
              borderRadius: 'var(--rounded-md)',
              background: 'var(--tint-purple-bg)',
              border: '1px solid var(--tint-purple-border)',
              cursor: 'pointer',
              transition: 'all 0.2s ease'
            }}
          >
            <div style={{ fontWeight: 700, color: 'var(--tint-purple-text)', marginBottom: '4px', display: 'flex', alignItems: 'center', gap: '6px' }}>
              <Sparkles size={16} /> 1. Gợi Ý Phân Công AI
            </div>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
              Khớp kỹ năng thành viên và lịch rảnh với yêu cầu công việc tự động.
            </p>
          </div>

          <div
            onClick={() => onNavigate('activities')}
            className="club-card-hover"
            style={{
              padding: 'var(--space-md)',
              borderRadius: 'var(--rounded-md)',
              background: 'var(--tint-green-bg)',
              border: '1px solid var(--tint-green-border)',
              cursor: 'pointer',
              transition: 'all 0.2s ease'
            }}
          >
            <div style={{ fontWeight: 700, color: 'var(--tint-green-text)', marginBottom: '4px', display: 'flex', alignItems: 'center', gap: '6px' }}>
              <Calendar size={16} /> 2. Điểm Danh Mã QR
            </div>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
              Sinh mã QR cho sự kiện và quét mã checkin tức thì trên thiết bị di động.
            </p>
          </div>

          <div
            onClick={() => onNavigate('tasks')}
            className="club-card-hover"
            style={{
              padding: 'var(--space-md)',
              borderRadius: 'var(--rounded-md)',
              background: 'var(--tint-blue-bg)',
              border: '1px solid var(--tint-blue-border)',
              cursor: 'pointer',
              transition: 'all 0.2s ease'
            }}
          >
            <div style={{ fontWeight: 700, color: 'var(--tint-blue-text)', marginBottom: '4px', display: 'flex', alignItems: 'center', gap: '6px' }}>
              <CheckSquare size={16} /> 3. Tiến Độ Nhiệm Vụ
            </div>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
              Theo dõi và cập nhật trạng thái nhiệm vụ trực quan theo thời gian thực.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
