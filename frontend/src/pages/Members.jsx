import React, { useState, useEffect } from 'react';
import { Search, Building2, Clock } from 'lucide-react';
import { api } from '../api/client';

export default function Members() {
  const [members, setMembers] = useState([]);
  const [departments, setDepartments] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedDept, setSelectedDept] = useState('ALL');
  const [selectedSkill, setSelectedSkill] = useState('ALL');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadData() {
      try {
        const [mList, dList] = await Promise.all([
          api.getMembers(),
          api.getDepartments()
        ]);
        setMembers(mList);
        setDepartments(dList);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    }
    loadData();
  }, []);

  const popularSkills = ['Photoshop', 'Canva', 'Lập trình', 'MC dẫn chương trình', 'Setup âm thanh', 'Video Editing'];

  const filteredMembers = members.filter((m) => {
    const matchName = m.full_name.toLowerCase().includes(searchTerm.toLowerCase()) || m.email.toLowerCase().includes(searchTerm.toLowerCase());
    const matchDept = selectedDept === 'ALL' || m.department_id === parseInt(selectedDept);
    const matchSkill = selectedSkill === 'ALL' || (m.skills && m.skills.some((s) => s.toLowerCase().includes(selectedSkill.toLowerCase())));
    return matchName && matchDept && matchSkill;
  });

  return (
    <div className="animate-fade-in" style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-lg)' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h2 style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--text-main)', letterSpacing: '-0.02em' }}>
            Danh Sách Thành Viên & Ban Chuyên Môn
          </h2>
          <p style={{ fontSize: '0.875rem', color: 'var(--text-muted)', marginTop: '2px' }}>
            Quản lý hồ sơ nhân sự, Ma trận Kỹ năng (Skill Matrix) và Lịch rảnh trong tuần
          </p>
        </div>
      </div>

      {/* Filter Bar */}
      <div className="club-card" style={{
        padding: '14px 18px',
        display: 'flex',
        flexDirection: 'column',
        gap: '12px'
      }}>
        <div style={{ display: 'flex', gap: 'var(--space-sm)', alignItems: 'center' }}>
          <div style={{ position: 'relative', flex: 1 }}>
            <Search size={18} style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
            <input
              type="text"
              placeholder="Tìm theo họ tên hoặc email..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              style={{
                width: '100%',
                padding: '10px 14px 10px 38px',
                fontSize: '0.875rem'
              }}
            />
          </div>

          <select
            value={selectedDept}
            onChange={(e) => setSelectedDept(e.target.value)}
            style={{
              padding: '10px 14px',
              fontSize: '0.875rem',
              minWidth: '220px'
            }}
          >
            <option value="ALL">Tất cả Ban chuyên môn ({members.length})</option>
            {departments.map((d) => (
              <option key={d.id} value={d.id}>{d.name} ({d.member_count})</option>
            ))}
          </select>
        </div>

        {/* Skill Matrix Filter Pills */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap', paddingTop: '4px', borderTop: '1px dashed var(--border-color)' }}>
          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.02em' }}>
            Lọc Kỹ Năng:
          </span>
          <button
            onClick={() => setSelectedSkill('ALL')}
            style={{
              padding: '4px 10px',
              borderRadius: 'var(--rounded-full)',
              border: selectedSkill === 'ALL' ? '1px solid var(--primary)' : '1px solid var(--border-color)',
              background: selectedSkill === 'ALL' ? 'var(--tint-blue-bg)' : 'transparent',
              color: selectedSkill === 'ALL' ? 'var(--primary)' : 'var(--text-secondary)',
              fontSize: '0.75rem',
              fontWeight: selectedSkill === 'ALL' ? 700 : 500,
              cursor: 'pointer'
            }}
          >
            Tất cả
          </button>
          {popularSkills.map((skill) => (
            <button
              key={skill}
              onClick={() => setSelectedSkill(skill === selectedSkill ? 'ALL' : skill)}
              style={{
                padding: '4px 10px',
                borderRadius: 'var(--rounded-full)',
                border: selectedSkill === skill ? '1px solid var(--accent)' : '1px solid var(--border-color)',
                background: selectedSkill === skill ? 'var(--tint-purple-bg)' : 'transparent',
                color: selectedSkill === skill ? 'var(--accent)' : 'var(--text-secondary)',
                fontSize: '0.75rem',
                fontWeight: selectedSkill === skill ? 700 : 500,
                cursor: 'pointer'
              }}
            >
              {skill}
            </button>
          ))}
        </div>
      </div>

      {/* Members Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: 'var(--space-md)' }}>
        {filteredMembers.map((member) => (
          <div key={member.id} className="club-card club-card-hover" style={{
            display: 'flex',
            flexDirection: 'column',
            gap: 'var(--space-sm)'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
              <div style={{ display: 'flex', gap: 'var(--space-sm)', alignItems: 'center' }}>
                <div style={{
                  width: '46px',
                  height: '46px',
                  borderRadius: 'var(--rounded-full)',
                  background: 'linear-gradient(135deg, #3b82f6, #6366f1)',
                  color: 'white',
                  fontWeight: 700,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontSize: '1.1rem',
                  boxShadow: '0 4px 10px rgba(59, 130, 246, 0.3)'
                }}>
                  {member.full_name.charAt(0)}
                </div>
                <div>
                  <h4 style={{ fontSize: '1rem', fontWeight: 700, color: 'var(--text-main)' }}>{member.full_name}</h4>
                  <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>{member.email}</div>
                </div>
              </div>

              <span className={`badge badge-${member.role.toLowerCase()}`}>
                {member.role === 'ADMIN' ? 'Ban Chủ Nhiệm' : member.role === 'LEADER' ? 'Trưởng Ban' : 'Thành Viên'}
              </span>
            </div>

            <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', display: 'flex', alignItems: 'center', gap: '6px' }}>
              <Building2 size={16} color="var(--secondary)" />
              <strong>Ban:</strong> {member.department_name}
            </div>

            {/* Skills Matrix */}
            <div>
              <div style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '6px', letterSpacing: '0.02em' }}>
                🎯 Kỹ năng (Skill Matrix):
              </div>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px' }}>
                {member.skills && member.skills.length > 0 ? (
                  member.skills.map((skill, idx) => (
                    <span key={idx} style={{
                      fontSize: '0.75rem',
                      background: 'var(--tint-blue-bg)',
                      color: 'var(--tint-blue-text)',
                      padding: '4px 9px',
                      borderRadius: 'var(--rounded-sm)',
                      border: '1px solid var(--tint-blue-border)',
                      fontWeight: 600
                    }}>
                      {skill}
                    </span>
                  ))
                ) : (
                  <span style={{ fontSize: '0.75rem', color: 'var(--text-light)', fontStyle: 'italic' }}>Chưa cập nhật</span>
                )}
              </div>
            </div>

            {/* Free Slots */}
            <div>
              <div style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', marginBottom: '6px', display: 'flex', alignItems: 'center', gap: '4px', letterSpacing: '0.02em' }}>
                <Clock size={12} /> Lịch rảnh trong tuần:
              </div>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px' }}>
                {member.free_slots && member.free_slots.length > 0 ? (
                  member.free_slots.map((slot, idx) => (
                    <span key={idx} style={{
                      fontSize: '0.75rem',
                      background: 'var(--tint-green-bg)',
                      color: 'var(--tint-green-text)',
                      padding: '4px 9px',
                      borderRadius: 'var(--rounded-sm)',
                      border: '1px solid var(--tint-green-border)',
                      fontWeight: 600
                    }}>
                      {slot}
                    </span>
                  ))
                ) : (
                  <span style={{ fontSize: '0.75rem', color: 'var(--text-light)', fontStyle: 'italic' }}>Chưa cập nhật</span>
                )}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
