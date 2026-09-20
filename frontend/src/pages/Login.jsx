import React, { useState } from 'react';
import { Sparkles, Shield, Compass, User, Lock, Mail, Eye, EyeOff, CheckCircle2, Cpu, QrCode, Award } from 'lucide-react';
import { api } from '../api/client';
import ThemeToggle from '../components/ThemeToggle';
import { useTheme } from '../context/ThemeContext';

export default function Login({ onLoginSuccess }) {
  const { isDark } = useTheme();
  const [email, setEmail] = useState('admin@club.edu.vn');
  const [password, setPassword] = useState('admin123');
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      setLoading(true);
      setError('');
      const data = await api.login(email, password);
      onLoginSuccess(data.user);
    } catch (err) {
      setError(err.message || 'Đăng nhập thất bại. Vui lòng kiểm tra Email/Mật khẩu.');
    } finally {
      setLoading(false);
    }
  };

  const handleQuickLogin = (presetEmail, presetPass) => {
    setEmail(presetEmail);
    setPassword(presetPass);
    setError('');
  };

  return (
    <div style={{
      minHeight: '100vh',
      background: isDark
        ? 'linear-gradient(135deg, #090d16 0%, #0f172a 40%, #171538 75%, #0b0f19 100%)'
        : 'linear-gradient(135deg, #eff6ff 0%, #f8fafc 40%, #ede9fe 75%, #f1f5f9 100%)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '24px',
      position: 'relative',
      overflow: 'hidden',
      transition: 'background 0.3s ease'
    }}>
      {/* Ambient Glowing Light Orbs */}
      <div className="ambient-light-blob animate-float" style={{
        top: '-10%',
        left: '-5%',
        width: '500px',
        height: '500px',
        background: 'radial-gradient(circle, rgba(59, 130, 246, 0.25) 0%, transparent 70%)'
      }} />
      <div className="ambient-light-blob animate-float" style={{
        bottom: '-10%',
        right: '-5%',
        width: '550px',
        height: '550px',
        background: 'radial-gradient(circle, rgba(139, 92, 246, 0.22) 0%, transparent 70%)',
        animationDelay: '-4s'
      }} />

      {/* Floating Theme Toggle in Header */}
      <div style={{ position: 'fixed', top: '24px', right: '28px', zIndex: 50 }}>
        <ThemeToggle />
      </div>

      {/* Main Container - Split Layout on Desktop */}
      <div className="animate-fade-in" style={{
        display: 'grid',
        gridTemplateColumns: '1fr 1fr',
        maxWidth: '1080px',
        width: '100%',
        borderRadius: '24px',
        background: isDark ? 'rgba(20, 29, 46, 0.75)' : 'rgba(255, 255, 255, 0.95)',
        backdropFilter: 'blur(24px)',
        WebkitBackdropFilter: 'blur(24px)',
        border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid var(--border-color)',
        boxShadow: isDark
          ? '0 25px 50px -12px rgba(0, 0, 0, 0.6), 0 0 40px rgba(99, 102, 241, 0.15)'
          : '0 20px 40px -12px rgba(15, 23, 42, 0.12), 0 0 30px rgba(99, 102, 241, 0.08)',
        overflow: 'hidden',
        zIndex: 1,
        transition: 'background 0.3s ease, border-color 0.3s ease'
      }}>
        {/* Left Column: Brand & AI Capabilities Showcase */}
        <div style={{
          padding: '44px 40px',
          background: isDark
            ? 'linear-gradient(180deg, rgba(37, 99, 235, 0.08) 0%, rgba(139, 92, 246, 0.04) 100%)'
            : 'linear-gradient(180deg, rgba(239, 246, 255, 0.7) 0%, rgba(245, 243, 255, 0.4) 100%)',
          borderRight: isDark ? '1px solid rgba(255, 255, 255, 0.08)' : '1px solid var(--border-color)',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between',
          transition: 'background 0.3s ease, border-color 0.3s ease'
        }}>
          <div>
            {/* Logo Emblem */}
            <div style={{ display: 'inline-flex', alignItems: 'center', gap: '10px', background: 'rgba(59, 130, 246, 0.15)', border: '1px solid rgba(59, 130, 246, 0.3)', padding: '6px 14px', borderRadius: '999px', marginBottom: '24px' }}>
              <Sparkles size={16} color="#60a5fa" />
              <span style={{ fontSize: '0.8rem', fontWeight: 700, color: isDark ? '#93c5fd' : '#2563eb', letterSpacing: '0.04em' }}>
                NHÓM 28 • HỆ THỐNG TÍCH HỢP AI AGENT
              </span>
            </div>

            <h1 style={{ fontSize: '2.1rem', fontWeight: 800, color: isDark ? '#ffffff' : 'var(--text-main)', lineHeight: 1.25, letterSpacing: '-0.025em', marginBottom: '14px' }}>
              Hệ Thống Quản Lý <br />
              <span className="gradient-text-ai">CLB Sinh Viên Tích Hợp AI Agent</span>
            </h1>

            <p style={{ fontSize: '0.95rem', color: isDark ? '#94a3b8' : 'var(--text-secondary)', lineHeight: 1.6, marginBottom: '32px' }}>
              Giải pháp số hóa toàn diện vận hành câu lạc bộ sinh viên trường đại học với thuật toán AI đề xuất phân công, chống điểm danh hộ và theo dõi tiến độ thời gian thực.
            </p>

            {/* Feature Highlights Grid */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '12px', color: isDark ? '#e2e8f0' : 'var(--text-main)', fontSize: '0.9rem' }}>
                <div style={{ width: '34px', height: '34px', borderRadius: '10px', background: 'rgba(59, 130, 246, 0.2)', border: '1px solid rgba(59, 130, 246, 0.4)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#60a5fa', flexShrink: 0 }}>
                  <Cpu size={18} />
                </div>
                <div>
                  <strong style={{ color: isDark ? '#ffffff' : 'var(--text-main)' }}>Gợi ý phân công AI:</strong> Tự động khớp Skill Matrix & Lịch rảnh thành viên.
                </div>
              </div>

              <div style={{ display: 'flex', alignItems: 'center', gap: '12px', color: isDark ? '#e2e8f0' : 'var(--text-main)', fontSize: '0.9rem' }}>
                <div style={{ width: '34px', height: '34px', borderRadius: '10px', background: 'rgba(16, 185, 129, 0.2)', border: '1px solid rgba(16, 185, 129, 0.4)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#10b981', flexShrink: 0 }}>
                  <QrCode size={18} />
                </div>
                <div>
                  <strong style={{ color: isDark ? '#ffffff' : 'var(--text-main)' }}>Mã QR bảo mật 4 lớp:</strong> GPS geofencing & khóa thiết bị phần cứng.
                </div>
              </div>

              <div style={{ display: 'flex', alignItems: 'center', gap: '12px', color: isDark ? '#e2e8f0' : 'var(--text-main)', fontSize: '0.9rem' }}>
                <div style={{ width: '34px', height: '34px', borderRadius: '10px', background: 'rgba(245, 158, 11, 0.2)', border: '1px solid rgba(245, 158, 11, 0.4)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#f59e0b', flexShrink: 0 }}>
                  <Award size={18} />
                </div>
                <div>
                  <strong style={{ color: isDark ? '#ffffff' : 'var(--text-main)' }}>Bảng xếp hạng đóng góp:</strong> Vinh danh cá nhân tích cực tự động.
                </div>
              </div>
            </div>
          </div>

          {/* Footer Team Info */}
          <div style={{ marginTop: '36px', paddingTop: '20px', borderTop: isDark ? '1px solid rgba(255, 255, 255, 0.08)' : '1px solid var(--border-color)', display: 'flex', alignItems: 'center', gap: '12px' }}>
            <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: '#10b981', boxShadow: '0 0 8px #10b981' }} />
            <div style={{ fontSize: '0.8rem', color: isDark ? '#94a3b8' : 'var(--text-muted)' }}>
              <strong>Nhóm 28:</strong> La Văn Quyền & Nguyễn Đức Anh
            </div>
          </div>
        </div>

        {/* Right Column: Interactive Login Form */}
        <div style={{
          padding: '40px',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          background: isDark ? 'rgba(15, 23, 42, 0.75)' : '#ffffff',
          transition: 'background 0.3s ease'
        }}>
          <div style={{ marginBottom: '24px' }}>
            <h2 style={{ fontSize: '1.4rem', fontWeight: 800, color: isDark ? '#ffffff' : 'var(--text-main)', letterSpacing: '-0.02em' }}>
              Đăng Nhập Hệ Thống
            </h2>
            <p style={{ fontSize: '0.85rem', color: isDark ? '#94a3b8' : 'var(--text-muted)', marginTop: '4px' }}>
              Nhập tài khoản được cấp hoặc chọn nhanh tài khoản trải nghiệm bên dưới
            </p>
          </div>

          {error && (
            <div style={{
              background: 'rgba(239, 68, 68, 0.15)',
              color: isDark ? '#f87171' : '#dc2626',
              padding: '12px 16px',
              borderRadius: '10px',
              fontSize: '0.85rem',
              marginBottom: '20px',
              border: '1px solid rgba(239, 68, 68, 0.3)',
              display: 'flex',
              alignItems: 'center',
              gap: '8px'
            }}>
              <span>⚠️</span> {error}
            </div>
          )}

          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <div>
              <label style={{ display: 'block', fontSize: '0.85rem', fontWeight: 600, color: isDark ? '#cbd5e1' : 'var(--text-secondary)', marginBottom: '6px' }}>
                Email Đăng Nhập
              </label>
              <div style={{ position: 'relative' }}>
                <Mail size={18} style={{ position: 'absolute', left: '14px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
                <input
                  type="email"
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="vd: admin@club.edu.vn"
                  style={{
                    width: '100%',
                    padding: '12px 14px 12px 42px',
                    borderRadius: '10px',
                    border: isDark ? '1px solid #334155' : '1px solid var(--border-input)',
                    background: isDark ? '#1e293b' : 'var(--bg-input)',
                    color: isDark ? '#ffffff' : 'var(--text-main)',
                    fontSize: '0.9rem'
                  }}
                />
              </div>
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '0.85rem', fontWeight: 600, color: isDark ? '#cbd5e1' : 'var(--text-secondary)', marginBottom: '6px' }}>
                Mật Khẩu
              </label>
              <div style={{ position: 'relative' }}>
                <Lock size={18} style={{ position: 'absolute', left: '14px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
                <input
                  type={showPassword ? 'text' : 'password'}
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="••••••••"
                  style={{
                    width: '100%',
                    padding: '12px 44px 12px 42px',
                    borderRadius: '10px',
                    border: isDark ? '1px solid #334155' : '1px solid var(--border-input)',
                    background: isDark ? '#1e293b' : 'var(--bg-input)',
                    color: isDark ? '#ffffff' : 'var(--text-main)',
                    fontSize: '0.9rem'
                  }}
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  style={{
                    position: 'absolute',
                    right: '12px',
                    top: '50%',
                    transform: 'translateY(-50%)',
                    background: 'transparent',
                    border: 'none',
                    color: 'var(--text-muted)',
                    cursor: 'pointer',
                    padding: '4px'
                  }}
                  title={showPassword ? 'Ẩn mật khẩu' : 'Xem mật khẩu'}
                >
                  {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
                </button>
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="btn btn-primary"
              style={{
                width: '100%',
                padding: '13px',
                borderRadius: '10px',
                marginTop: '6px',
                fontSize: '0.95rem',
                fontWeight: 700,
                boxShadow: '0 4px 16px rgba(37, 99, 235, 0.4)'
              }}
            >
              {loading ? 'Đang xác thực tài khoản...' : 'Đăng Nhập Vào Hệ Thống'}
            </button>
          </form>

          {/* Quick Demo Login Presets */}
          <div style={{ marginTop: '24px', paddingTop: '20px', borderTop: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid var(--border-color)' }}>
            <div style={{ fontSize: '0.75rem', fontWeight: 700, color: isDark ? '#94a3b8' : 'var(--text-muted)', marginBottom: '12px', textAlign: 'center', textTransform: 'uppercase', letterSpacing: '0.04em' }}>
              ⚡ CHỌN NHANH TÀI KHOẢN TRẢI NGHIỆM
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <button
                type="button"
                onClick={() => handleQuickLogin('admin@club.edu.vn', 'admin123')}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  padding: '10px 14px',
                  borderRadius: '10px',
                  background: isDark ? 'rgba(239, 68, 68, 0.12)' : 'rgba(239, 68, 68, 0.08)',
                  border: isDark ? '1px solid rgba(239, 68, 68, 0.35)' : '1px solid rgba(239, 68, 68, 0.25)',
                  color: isDark ? '#f87171' : '#dc2626',
                  fontSize: '0.82rem',
                  fontWeight: 600,
                  cursor: 'pointer',
                  transition: 'all 0.2s ease'
                }}
              >
                <span style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <Shield size={16} /> Ban Chủ Nhiệm (La Văn Quyền)
                </span>
                <span style={{ fontSize: '0.75rem', opacity: 0.85, background: isDark ? 'rgba(0,0,0,0.2)' : 'rgba(255,255,255,0.8)', padding: '2px 8px', borderRadius: '4px' }}>admin@club.edu.vn</span>
              </button>

              <button
                type="button"
                onClick={() => handleQuickLogin('leader@club.edu.vn', 'leader123')}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  padding: '10px 14px',
                  borderRadius: '10px',
                  background: isDark ? 'rgba(59, 130, 246, 0.12)' : 'rgba(59, 130, 246, 0.08)',
                  border: isDark ? '1px solid rgba(59, 130, 246, 0.35)' : '1px solid rgba(59, 130, 246, 0.25)',
                  color: isDark ? '#60a5fa' : '#2563eb',
                  fontSize: '0.82rem',
                  fontWeight: 600,
                  cursor: 'pointer',
                  transition: 'all 0.2s ease'
                }}
              >
                <span style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <Compass size={16} /> Trưởng Ban (Nguyễn Đức Anh)
                </span>
                <span style={{ fontSize: '0.75rem', opacity: 0.85, background: isDark ? 'rgba(0,0,0,0.2)' : 'rgba(255,255,255,0.8)', padding: '2px 8px', borderRadius: '4px' }}>leader@club.edu.vn</span>
              </button>

              <button
                type="button"
                onClick={() => handleQuickLogin('member@club.edu.vn', 'member123')}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  padding: '10px 14px',
                  borderRadius: '10px',
                  background: isDark ? 'rgba(16, 185, 129, 0.12)' : 'rgba(16, 185, 129, 0.08)',
                  border: isDark ? '1px solid rgba(16, 185, 129, 0.35)' : '1px solid rgba(16, 185, 129, 0.25)',
                  color: isDark ? '#34d399' : '#059669',
                  fontSize: '0.82rem',
                  fontWeight: 600,
                  cursor: 'pointer',
                  transition: 'all 0.2s ease'
                }}
              >
                <span style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <User size={16} /> Thành Viên (Trần Phương Anh)
                </span>
                <span style={{ fontSize: '0.75rem', opacity: 0.85, background: isDark ? 'rgba(0,0,0,0.2)' : 'rgba(255,255,255,0.8)', padding: '2px 8px', borderRadius: '4px' }}>member@club.edu.vn</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
