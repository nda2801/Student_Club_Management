import React from 'react';
import { LayoutDashboard, Users, Calendar, CheckSquare, Sparkles, Award } from 'lucide-react';

export default function Sidebar({ activeTab, setActiveTab }) {
  const sections = [
    {
      title: 'TỔNG QUAN',
      items: [
        { id: 'dashboard', label: 'Bàn Làm Việc', icon: LayoutDashboard },
      ]
    },
    {
      title: 'HOẠT ĐỘNG CLB',
      items: [
        { id: 'members', label: 'Thành viên & Ban', icon: Users },
        { id: 'activities', label: 'Sự kiện & Điểm danh', icon: Calendar },
        { id: 'tasks', label: 'Nhiệm vụ', icon: CheckSquare },
      ]
    },
    {
      title: 'TRÍ TUỆ NHÂN TẠO',
      items: [
        { id: 'aihub', label: 'Trợ lý AI Hub', icon: Sparkles, isAi: true, badge: 'AGENT' },
        { id: 'leaderboard', label: 'Bảng Xếp Hạng', icon: Award },
      ]
    }
  ];

  return (
    <aside style={{
      width: '250px',
      background: 'var(--bg-sidebar)',
      borderRight: '1px solid var(--border-color)',
      display: 'flex',
      flexDirection: 'column',
      padding: '20px 14px',
      flexShrink: 0,
      minHeight: 'calc(100vh - 64px)',
      transition: 'background-color 0.25s ease, border-color 0.25s ease'
    }}>
      <nav style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
        {sections.map((sec, idx) => (
          <div key={idx}>
            <div style={{
              fontSize: '0.7rem',
              fontWeight: 800,
              color: 'var(--text-light)',
              textTransform: 'uppercase',
              padding: '0 12px 8px',
              letterSpacing: '0.06em'
            }}>
              {sec.title}
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
              {sec.items.map((item) => {
                const Icon = item.icon;
                const isActive = activeTab === item.id;

                return (
                  <button
                    key={item.id}
                    onClick={() => setActiveTab(item.id)}
                    className={`sidebar-nav-btn ${isActive ? 'active' : ''} ${item.isAi ? 'ai-active' : ''}`}
                  >
                    <Icon
                      size={18}
                      style={{
                        color: isActive
                          ? '#ffffff'
                          : item.isAi
                            ? 'var(--accent)'
                            : 'var(--text-muted)'
                      }}
                    />
                    <span style={{ flex: 1 }}>{item.label}</span>
                    {item.badge && !isActive && (
                      <span className="badge badge-ai" style={{ fontSize: '0.65rem', padding: '2px 7px' }}>
                        {item.badge}
                      </span>
                    )}
                  </button>
                );
              })}
            </div>
          </div>
        ))}
      </nav>

      {/* Footer Info Box */}
      <div style={{
        marginTop: 'auto',
        padding: '16px 14px',
        background: 'var(--bg-card-secondary)',
        borderRadius: 'var(--rounded-lg)',
        border: '1px solid var(--border-color)',
        transition: 'background-color 0.25s ease, border-color 0.25s ease'
      }}>
        <div style={{
          fontSize: '0.82rem',
          fontWeight: 700,
          color: 'var(--text-main)',
          marginBottom: '4px',
          display: 'flex',
          alignItems: 'center',
          gap: '6px'
        }}>
          <Sparkles size={15} color="var(--accent)" /> Nhóm 28 • AI Agent
        </div>
        <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', lineHeight: 1.4 }}>
          Nhóm 28: La Văn Quyền & Nguyễn Đức Anh
        </div>
      </div>
    </aside>
  );
}
