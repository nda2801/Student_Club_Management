import React from 'react';
import { Sun, Moon } from 'lucide-react';
import { useTheme } from '../context/ThemeContext';

export default function ThemeToggle({ className = '', style = {} }) {
  const { isDark, toggleTheme } = useTheme();

  return (
    <button
      type="button"
      onClick={toggleTheme}
      className={`theme-toggle-btn ${className}`}
      title={isDark ? 'Chuyển sang Chế độ Sáng' : 'Chuyển sang Chế độ Tối'}
      aria-label={isDark ? 'Chuyển sang Chế độ Sáng' : 'Chuyển sang Chế độ Tối'}
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: '8px',
        padding: '8px 12px',
        borderRadius: '10px',
        border: '1px solid var(--border-color)',
        background: isDark ? 'rgba(255, 255, 255, 0.08)' : 'var(--bg-card-secondary)',
        color: 'var(--text-main)',
        cursor: 'pointer',
        fontWeight: 600,
        fontSize: '0.85rem',
        transition: 'all 0.25s cubic-bezier(0.16, 1, 0.3, 1)',
        boxShadow: isDark ? '0 0 12px rgba(139, 92, 246, 0.2)' : 'var(--shadow-sm)',
        ...style
      }}
    >
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        width: '20px',
        height: '20px',
        position: 'relative'
      }}>
        {isDark ? (
          <Sun
            size={18}
            style={{
              color: '#f59e0b',
              transition: 'transform 0.3s ease, filter 0.3s ease',
              filter: 'drop-shadow(0 0 6px rgba(245, 158, 11, 0.6))'
            }}
          />
        ) : (
          <Moon
            size={18}
            style={{
              color: '#6366f1',
              transition: 'transform 0.3s ease, filter 0.3s ease',
              filter: 'drop-shadow(0 0 4px rgba(99, 102, 241, 0.4))'
            }}
          />
        )}
      </div>
      <span className="theme-toggle-label" style={{ fontSize: '0.82rem', userSelect: 'none' }}>
        {isDark ? 'Giao diện Tối' : 'Giao diện Sáng'}
      </span>
    </button>
  );
}
