import React from 'react';
import { LogOut, User as UserIcon, Sparkles, Shield, Compass, CircleDot } from 'lucide-react';
import { removeAuthToken } from '../api/client';
import ThemeToggle from './ThemeToggle';

export default function Navbar({ user, onLogout }) {
  const getRoleBadge = (role) => {
    if (role === 'ADMIN') return <span className="badge badge-admin"><Shield size={12} /> Ban Chủ Nhiệm</span>;
    if (role === 'LEADER') return <span className="badge badge-leader"><Compass size={12} /> Trưởng Ban</span>;
    return <span className="badge badge-member"><UserIcon size={12} /> Thành Viên</span>;
  };

  return (
    <header style={{
      height: '66px',
      background: 'var(--bg-header)',
      borderBottom: '1px solid var(--border-color)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      padding: '0 28px',
      position: 'sticky',
      top: 0,
      zIndex: 40,
      backdropFilter: 'blur(16px)',
      WebkitBackdropFilter: 'blur(16px)',
      transition: 'background-color 0.25s ease, border-color 0.25s ease'
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
        <div style={{
          width: '40px',
          height: '40px',
          borderRadius: 'var(--rounded-md)',
          background: 'linear-gradient(135deg, #2563eb, #8b5cf6)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: 'white',
          fontWeight: 'bold',
          boxShadow: '0 4px 14px rgba(37, 99, 235, 0.35)'
        }}>
          <Sparkles size={22} />
        </div>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <h1 style={{ fontSize: '1.15rem', fontWeight: 800, color: 'var(--text-main)', lineHeight: 1.2, letterSpacing: '-0.02em' }}>
              CLB Sinh Viên AI
            </h1>
            <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', fontSize: '0.7rem', color: 'var(--success)', background: 'var(--tint-green-bg)', padding: '2px 8px', borderRadius: 'var(--rounded-full)', fontWeight: 600 }}>
              <CircleDot size={10} /> Online
            </span>
          </div>
          <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Hệ thống tích hợp AI Agent (Nhóm 28)</span>
        </div>
      </div>

      <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
        <ThemeToggle />

        {user && (
          <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
            <div style={{ textAlign: 'right' }}>
              <div style={{ fontSize: '0.9rem', fontWeight: 700, color: 'var(--text-main)' }}>
                {user.full_name}
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px', justifyContent: 'flex-end', marginTop: '3px' }}>
                {getRoleBadge(user.role)}
                <span style={{ fontSize: '0.75rem', color: 'var(--text-secondary)', background: 'var(--bg-card-secondary)', border: '1px solid var(--border-color)', padding: '2px 8px', borderRadius: 'var(--rounded-xs)', fontWeight: 500 }}>
                  {user.department_name}
                </span>
              </div>
            </div>
            <button
              onClick={() => {
                removeAuthToken();
                onLogout();
              }}
              style={{
                background: 'var(--danger-light)',
                color: 'var(--danger)',
                border: '1px solid rgba(239, 68, 68, 0.25)',
                padding: '8px 14px',
                borderRadius: 'var(--rounded-md)',
                display: 'flex',
                alignItems: 'center',
                gap: '6px',
                fontSize: '0.85rem',
                fontWeight: 600,
                cursor: 'pointer'
              }}
              title="Đăng xuất"
            >
              <LogOut size={16} /> Đăng xuất
            </button>
          </div>
        )}
      </div>
    </header>
  );
}
