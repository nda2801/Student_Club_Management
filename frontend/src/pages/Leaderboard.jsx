import React, { useState, useEffect } from 'react';
import { Trophy, Crown, Medal, Award, Flame, CheckCircle2, Calendar } from 'lucide-react';
import { api } from '../api/client';

export default function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadData() {
      try {
        setLoading(true);
        const data = await api.getLeaderboard();
        setLeaderboard(data || []);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    }
    loadData();
  }, []);

  const top1 = leaderboard[0];
  const top2 = leaderboard[1];
  const top3 = leaderboard[2];
  const maxScore = Math.max(...leaderboard.map((m) => m.contribution_score || 0), 1);

  const getRankBadge = (idx) => {
    if (idx === 0) return <span style={{ background: 'var(--tint-amber-bg)', color: 'var(--tint-amber-text)', border: '1px solid var(--tint-amber-border)', padding: '4px 10px', borderRadius: 'var(--rounded-full)', fontWeight: 800, fontSize: '0.8rem' }}>🥇 HẠNG 1</span>;
    if (idx === 1) return <span style={{ background: 'var(--tint-blue-bg)', color: 'var(--tint-blue-text)', border: '1px solid var(--tint-blue-border)', padding: '4px 10px', borderRadius: 'var(--rounded-full)', fontWeight: 800, fontSize: '0.8rem' }}>🥈 HẠNG 2</span>;
    if (idx === 2) return <span style={{ background: 'var(--tint-purple-bg)', color: 'var(--tint-purple-text)', border: '1px solid var(--tint-purple-border)', padding: '4px 10px', borderRadius: 'var(--rounded-full)', fontWeight: 800, fontSize: '0.8rem' }}>🥉 HẠNG 3</span>;
    return <span style={{ color: 'var(--text-muted)', fontWeight: 700, fontSize: '0.9rem' }}>#{idx + 1}</span>;
  };

  return (
    <div className="animate-fade-in" style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-xl)' }}>
      <div>
        <h2 style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--text-main)', display: 'flex', alignItems: 'center', gap: '8px', letterSpacing: '-0.02em' }}>
          <Trophy color="var(--warning)" size={24} /> Bảng Xếp Hạng Đóng Góp Thành Viên
        </h2>
        <p style={{ fontSize: '0.875rem', color: 'var(--text-muted)', marginTop: '2px' }}>
          Tôn vinh và xếp hạng đóng góp cá nhân dựa trên lượt tham gia sự kiện và khối lượng hoàn thành nhiệm vụ
        </p>
      </div>

      {/* TOP 3 PODIUM DISPLAY */}
      {leaderboard.length >= 3 && (
        <div className="podium-container">
          {/* Rank 2: Silver */}
          <div className="podium-card podium-rank-2">
            <div style={{
              width: '56px',
              height: '56px',
              borderRadius: 'var(--rounded-full)',
              background: 'linear-gradient(135deg, #94a3b8, #64748b)',
              color: '#ffffff',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: '1.3rem',
              fontWeight: 800,
              boxShadow: '0 4px 12px rgba(100, 116, 139, 0.3)',
              marginBottom: '12px'
            }}>
              {top2.full_name?.charAt(0)}
            </div>

            <div style={{ background: 'var(--tint-blue-bg)', color: 'var(--tint-blue-text)', border: '1px solid var(--tint-blue-border)', padding: '2px 10px', borderRadius: 'var(--rounded-full)', fontSize: '0.75rem', fontWeight: 800, marginBottom: '8px' }}>
              🥈 HẠNG 2
            </div>

            <div style={{ fontSize: '1.05rem', fontWeight: 800, color: 'var(--text-main)' }}>
              {top2.full_name}
            </div>
            <div style={{ fontSize: '0.78rem', color: 'var(--text-muted)', marginTop: '2px' }}>
              {top2.department_name}
            </div>

            <div style={{ marginTop: '14px', fontSize: '1.35rem', fontWeight: 800, color: 'var(--primary)' }}>
              {top2.contribution_score} <span style={{ fontSize: '0.8rem', fontWeight: 600 }}>điểm</span>
            </div>

            <div style={{ display: 'flex', gap: '8px', marginTop: '10px', fontSize: '0.72rem', color: 'var(--text-muted)' }}>
              <span>{top2.attendance_count} điểm danh</span> • <span>{top2.task_completed_count} task</span>
            </div>
          </div>

          {/* Rank 1: Gold (Center & Elevated) */}
          <div className="podium-card podium-rank-1">
            <div style={{ position: 'relative', marginBottom: '12px' }}>
              <Crown size={28} color="#f59e0b" style={{ position: 'absolute', top: '-22px', left: '50%', transform: 'translateX(-50%)', filter: 'drop-shadow(0 2px 6px rgba(245, 158, 11, 0.5))' }} />
              <div style={{
                width: '68px',
                height: '68px',
                borderRadius: 'var(--rounded-full)',
                background: 'linear-gradient(135deg, #f59e0b, #d97706)',
                color: '#ffffff',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '1.6rem',
                fontWeight: 800,
                boxShadow: '0 6px 16px rgba(245, 158, 11, 0.4)',
                border: '2px solid #ffffff'
              }}>
                {top1.full_name?.charAt(0)}
              </div>
            </div>

            <div style={{ background: 'var(--tint-amber-bg)', color: 'var(--tint-amber-text)', border: '1px solid var(--tint-amber-border)', padding: '3px 12px', borderRadius: 'var(--rounded-full)', fontSize: '0.8rem', fontWeight: 800, marginBottom: '8px' }}>
              🥇 QUÁN QUÂN
            </div>

            <div style={{ fontSize: '1.2rem', fontWeight: 800, color: 'var(--text-main)' }}>
              {top1.full_name}
            </div>
            <div style={{ fontSize: '0.82rem', color: 'var(--text-muted)', marginTop: '2px' }}>
              {top1.department_name}
            </div>

            <div style={{ marginTop: '14px', fontSize: '1.65rem', fontWeight: 800, color: '#d97706' }}>
              {top1.contribution_score} <span style={{ fontSize: '0.85rem', fontWeight: 600 }}>điểm</span>
            </div>

            <div style={{ display: 'flex', gap: '8px', marginTop: '10px', fontSize: '0.75rem', color: 'var(--text-muted)' }}>
              <span>{top1.attendance_count} điểm danh</span> • <span>{top1.task_completed_count} task</span>
            </div>
          </div>

          {/* Rank 3: Bronze */}
          <div className="podium-card podium-rank-3">
            <div style={{
              width: '52px',
              height: '52px',
              borderRadius: 'var(--rounded-full)',
              background: 'linear-gradient(135deg, #b45309, #78350f)',
              color: '#ffffff',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: '1.2rem',
              fontWeight: 800,
              boxShadow: '0 4px 12px rgba(180, 83, 9, 0.3)',
              marginBottom: '12px'
            }}>
              {top3.full_name?.charAt(0)}
            </div>

            <div style={{ background: 'var(--tint-purple-bg)', color: 'var(--tint-purple-text)', border: '1px solid var(--tint-purple-border)', padding: '2px 10px', borderRadius: 'var(--rounded-full)', fontSize: '0.75rem', fontWeight: 800, marginBottom: '8px' }}>
              🥉 HẠNG 3
            </div>

            <div style={{ fontSize: '1rem', fontWeight: 800, color: 'var(--text-main)' }}>
              {top3.full_name}
            </div>
            <div style={{ fontSize: '0.78rem', color: 'var(--text-muted)', marginTop: '2px' }}>
              {top3.department_name}
            </div>

            <div style={{ marginTop: '14px', fontSize: '1.35rem', fontWeight: 800, color: 'var(--accent)' }}>
              {top3.contribution_score} <span style={{ fontSize: '0.8rem', fontWeight: 600 }}>điểm</span>
            </div>

            <div style={{ display: 'flex', gap: '8px', marginTop: '10px', fontSize: '0.72rem', color: 'var(--text-muted)' }}>
              <span>{top3.attendance_count} điểm danh</span> • <span>{top3.task_completed_count} task</span>
            </div>
          </div>
        </div>
      )}

      {/* Leaderboard Table Card */}
      <div className="club-card" style={{ padding: 0, overflow: 'hidden' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
          <thead>
            <tr style={{ background: 'var(--bg-card-secondary)', borderBottom: '1px solid var(--border-color)', fontSize: '0.8rem', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.02em' }}>
              <th style={{ padding: '14px 20px' }}>Thứ Hạng</th>
              <th style={{ padding: '14px 20px' }}>Họ Và Tên</th>
              <th style={{ padding: '14px 20px' }}>Ban Chuyên Môn</th>
              <th style={{ padding: '14px 20px', textAlign: 'center' }}>Điểm Danh</th>
              <th style={{ padding: '14px 20px', textAlign: 'center' }}>Nhiệm Vụ Đã Xong</th>
              <th style={{ padding: '14px 20px', textAlign: 'right' }}>Mức Độ Đóng Góp</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.map((item, idx) => {
              const percentage = Math.round((item.contribution_score / maxScore) * 100);

              return (
                <tr key={item.user_id} style={{
                  borderBottom: '1px solid var(--border-color)',
                  background: idx === 0 ? 'var(--tint-amber-bg)' : idx === 1 ? 'var(--tint-blue-bg)' : idx === 2 ? 'var(--tint-purple-bg)' : 'transparent',
                  transition: 'background-color 0.15s ease'
                }}>
                  <td style={{ padding: '16px 20px' }}>
                    {getRankBadge(idx)}
                  </td>
                  <td style={{ padding: '16px 20px', fontWeight: 700, color: 'var(--text-main)' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span>{item.full_name}</span>
                      {item.role === 'ADMIN' && <span className="badge badge-admin">BCN</span>}
                      {item.role === 'LEADER' && <span className="badge badge-leader">Trưởng Ban</span>}
                    </div>
                  </td>
                  <td style={{ padding: '16px 20px', color: 'var(--text-secondary)', fontSize: '0.88rem' }}>
                    {item.department_name}
                  </td>
                  <td style={{ padding: '16px 20px', textAlign: 'center', fontWeight: 600, color: 'var(--primary)' }}>
                    {item.attendance_count} buổi
                  </td>
                  <td style={{ padding: '16px 20px', textAlign: 'center', fontWeight: 600, color: 'var(--success)' }}>
                    {item.task_completed_count} task
                  </td>
                  <td style={{ padding: '16px 20px', textAlign: 'right' }}>
                    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: '4px' }}>
                      <div style={{ fontWeight: 800, color: 'var(--accent)', fontSize: '1.05rem' }}>
                        {item.contribution_score} điểm
                      </div>
                      <div style={{ width: '120px', height: '5px', background: 'var(--border-color)', borderRadius: 'var(--rounded-full)', overflow: 'hidden' }}>
                        <div style={{
                          width: `${percentage}%`,
                          height: '100%',
                          background: idx === 0 ? '#f59e0b' : 'var(--accent)',
                          borderRadius: 'var(--rounded-full)'
                        }} />
                      </div>
                    </div>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}
