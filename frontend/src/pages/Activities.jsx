import React, { useState, useEffect } from 'react';
import { Plus, QrCode, MapPin, Clock, Users } from 'lucide-react';
import { api } from '../api/client';
import QRCodeModal from '../components/QRCodeModal';

import { useToast } from '../context/ToastContext';

export default function Activities({ currentUser }) {
  const toast = useToast();
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedActivity, setSelectedActivity] = useState(null);
  const [showCreateModal, setShowCreateModal] = useState(false);

  // Form states
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [startTime, setStartTime] = useState('');
  const [endTime, setEndTime] = useState('');
  const [location, setLocation] = useState('');

  const loadActivities = async () => {
    try {
      setLoading(true);
      const data = await api.getActivities();
      setActivities(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadActivities();
  }, []);

  const handleCreateActivity = async (e) => {
    e.preventDefault();
    try {
      const startDt = startTime ? new Date(startTime).toISOString() : new Date().toISOString();
      const endDt = endTime ? new Date(endTime).toISOString() : new Date(Date.now() + 14400000).toISOString();

      await api.createActivity({
        title,
        description,
        start_time: startDt,
        end_time: endDt,
        location,
        status: 'UPCOMING'
      });
      toast.success(`Đã tạo sự kiện '${title}' thành công!`, 'Tạo sự kiện');
      setShowCreateModal(false);
      setTitle('');
      setDescription('');
      setLocation('');
      setStartTime('');
      setEndTime('');
      loadActivities();
    } catch (err) {
      toast.error(err.message || 'Không thể tạo sự kiện', 'Lỗi tạo sự kiện');
    }
  };

  return (
    <div className="animate-fade-in" style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-lg)' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h2 style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--text-main)', letterSpacing: '-0.02em' }}>
            Sự Kiện & Mã QR Điểm Danh Động
          </h2>
          <p style={{ fontSize: '0.875rem', color: 'var(--text-muted)', marginTop: '2px' }}>
            Mã QR cá nhân độc bản thay đổi tự động, giới hạn thời gian và xác thực thiết bị
          </p>
        </div>

        {currentUser?.role !== 'MEMBER' && (
          <button
            onClick={() => setShowCreateModal(true)}
            className="btn btn-primary"
          >
            <Plus size={18} /> Tạo Sự Kiện Mới
          </button>
        )}
      </div>

      {/* Activity Cards List */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: 'var(--space-md)' }}>
        {activities.map((act) => (
          <div key={act.id} className="club-card club-card-hover" style={{
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'space-between',
            gap: 'var(--space-sm)'
          }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '8px' }}>
                <span style={{
                  fontSize: '0.75rem',
                  fontWeight: 700,
                  padding: '3px 10px',
                  borderRadius: 'var(--rounded-full)',
                  background: act.status === 'UPCOMING' ? 'var(--tint-blue-bg)' : 'var(--tint-green-bg)',
                  color: act.status === 'UPCOMING' ? 'var(--tint-blue-text)' : 'var(--tint-green-text)',
                  border: `1px solid ${act.status === 'UPCOMING' ? 'var(--tint-blue-border)' : 'var(--tint-green-border)'}`
                }}>
                  {act.status === 'UPCOMING' ? 'Sắp diễn ra' : 'Đã hoàn thành'}
                </span>
                <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                  <Users size={14} /> {act.attendance_count} đã điểm danh
                </span>
              </div>

              <h3 style={{ fontSize: '1.1rem', fontWeight: 700, color: 'var(--text-main)', marginBottom: '6px' }}>
                {act.title}
              </h3>
              <p style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginBottom: '12px', lineHeight: 1.5 }}>
                {act.description}
              </p>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <Clock size={14} color="var(--primary)" /> 
                  Bắt đầu: {new Date(act.start_time).toLocaleString()}
                </div>
                {act.end_time && (
                  <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <Clock size={14} color="var(--accent)" /> 
                    Kết thúc (Hết hạn QR): {new Date(act.end_time).toLocaleString()}
                  </div>
                )}
                <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <MapPin size={14} color="var(--danger)" /> {act.location || 'Chưa cập nhật'}
                </div>
              </div>
            </div>

            <div style={{ paddingTop: '12px', borderTop: '1px solid var(--border-color)', display: 'flex', justifyContent: 'flex-end' }}>
              <button
                onClick={() => setSelectedActivity(act)}
                className="btn btn-ai"
                style={{ fontSize: '0.85rem', padding: '8px 14px' }}
              >
                <QrCode size={16} /> Lấy Mã QR Cá Nhân & Điểm Danh
              </button>
            </div>
          </div>
        ))}
      </div>

      {/* QR Code Modal */}
      {selectedActivity && (
        <QRCodeModal
          activity={selectedActivity}
          currentUser={currentUser}
          onClose={() => setSelectedActivity(null)}
          onCheckinSuccess={loadActivities}
        />
      )}

      {/* Create Activity Modal */}
      {showCreateModal && (
        <div style={{ position: 'fixed', inset: 0, background: 'var(--bg-overlay)', backdropFilter: 'blur(6px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 100 }}>
          <div className="club-card" style={{ maxWidth: '480px', width: '100%', padding: '24px', boxShadow: 'var(--shadow-lg)' }}>
            <h3 style={{ fontSize: '1.2rem', fontWeight: 700, color: 'var(--text-main)', marginBottom: '16px' }}>Tạo Sự Kiện CLB Mới</h3>
            <form onSubmit={handleCreateActivity} style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              <input
                type="text"
                placeholder="Tên sự kiện / Hoạt động"
                required
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                style={{ width: '100%', padding: '10px 14px' }}
              />
              <textarea
                placeholder="Mô tả sự kiện"
                rows={3}
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                style={{ width: '100%', padding: '10px 14px' }}
              />
              <div>
                <label style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', marginBottom: '4px', display: 'block', fontWeight: 600 }}>Thời gian bắt đầu</label>
                <input
                  type="datetime-local"
                  required
                  value={startTime}
                  onChange={(e) => setStartTime(e.target.value)}
                  style={{ width: '100%', padding: '10px 14px' }}
                />
              </div>
              <div>
                <label style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', marginBottom: '4px', display: 'block', fontWeight: 600 }}>Thời gian kết thúc (Mã QR hết hạn sau giờ này)</label>
                <input
                  type="datetime-local"
                  required
                  value={endTime}
                  onChange={(e) => setEndTime(e.target.value)}
                  style={{ width: '100%', padding: '10px 14px' }}
                />
              </div>
              <input
                type="text"
                placeholder="Địa điểm tổ chức (vd: Hội trường A1)"
                value={location}
                onChange={(e) => setLocation(e.target.value)}
                style={{ width: '100%', padding: '10px 14px' }}
              />
              <div style={{ display: 'flex', gap: '8px', justifyContent: 'flex-end', marginTop: '12px' }}>
                <button type="button" onClick={() => setShowCreateModal(false)} className="btn btn-secondary">Hủy</button>
                <button type="submit" className="btn btn-primary">Lưu Sự Kiện</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
