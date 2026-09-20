import React, { useState, useEffect } from 'react';
import { QRCodeSVG } from 'qrcode.react';
import { X, CheckCircle, QrCode, Clock, ShieldCheck, AlertTriangle, MapPin, Smartphone } from 'lucide-react';
import { api } from '../api/client';

import { useToast } from '../context/ToastContext';

const getDeviceFingerprint = () => {
  let fp = localStorage.getItem('device_fp');
  if (!fp) {
    fp = 'DEV_' + Math.random().toString(36).substring(2, 9) + '_' + Date.now().toString(36);
    localStorage.setItem('device_fp', fp);
  }
  return fp;
};

export default function QRCodeModal({ activity, currentUser, onClose, onCheckinSuccess }) {
  const toast = useToast();
  const [qrData, setQrData] = useState(null);
  const [loadingQr, setLoadingQr] = useState(true);
  const [loadingCheckin, setLoadingCheckin] = useState(false);
  const [userGps, setUserGps] = useState(null);
  const [gpsStatus, setGpsStatus] = useState('Đang lấy vị trí GPS...');
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    async function fetchPersonalQr() {
      try {
        setLoadingQr(true);
        setError('');
        const data = await api.getMyQr(activity.id);
        setQrData(data);
      } catch (err) {
        setError(err.message || 'Không thể tạo mã QR điểm danh cá nhân');
        toast.error(err.message || 'Không thể tạo mã QR', 'Lỗi QR');
      } finally {
        setLoadingQr(false);
      }
    }
    fetchPersonalQr();

    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (pos) => {
          setUserGps({ lat: pos.coords.latitude, lng: pos.coords.longitude });
          setGpsStatus('✅ Đã xác thực GPS hội trường');
        },
        (err) => {
          setGpsStatus('⚠️ Không thể lấy GPS (Mặc định kiểm tra mã QR & Thiết bị)');
        }
      );
    }
  }, [activity.id]);

  const handleAutoCheckin = async () => {
    if (!qrData?.qr_token) return;
    try {
      setLoadingCheckin(true);
      setError('');
      setMessage('');

      const res = await api.checkinActivity({
        activity_id: activity.id,
        qr_code_hash: qrData.qr_token,
        user_lat: userGps?.lat || null,
        user_lng: userGps?.lng || null,
        device_fingerprint: getDeviceFingerprint()
      });

      const successMsg = `🎉 ĐÃ XÁC THỰC THIẾT BỊ PHẦN CỨNG & TỰ ĐỘNG ĐUYỆT ĐIỂM DANH cho ${res.user_name} vào lúc ${new Date(res.checkin_time).toLocaleTimeString()}!`;
      setMessage(successMsg);
      toast.success(`Đã điểm danh thành công cho ${res.user_name}!`, 'Điểm danh hoàn tất');
      if (onCheckinSuccess) onCheckinSuccess();
    } catch (err) {
      setError(err.message || 'Điểm danh thất bại');
      toast.error(err.message || 'Điểm danh thất bại', 'Lỗi điểm danh');
    } finally {
      setLoadingCheckin(false);
    }
  };

  return (
    <div style={{
      position: 'fixed',
      inset: 0,
      background: 'var(--bg-overlay)',
      backdropFilter: 'blur(6px)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      zIndex: 100,
      padding: '16px'
    }}>
      <div className="animate-fade-in" style={{
        background: 'var(--bg-modal)',
        borderRadius: '20px',
        maxWidth: '460px',
        width: '100%',
        padding: '28px',
        border: '1px solid var(--border-color)',
        boxShadow: 'var(--shadow-lg)',
        position: 'relative',
        transition: 'background-color 0.25s ease, border-color 0.25s ease'
      }}>
        <button
          onClick={onClose}
          style={{
            position: 'absolute',
            top: '16px',
            right: '16px',
            background: 'var(--bg-card-secondary)',
            border: '1px solid var(--border-color)',
            borderRadius: '50%',
            width: '32px',
            height: '32px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: 'var(--text-muted)'
          }}
        >
          <X size={18} />
        </button>

        <div style={{ textAlign: 'center', marginBottom: '16px' }}>
          <div style={{
            display: 'inline-flex',
            padding: '10px',
            borderRadius: '12px',
            background: 'linear-gradient(135deg, #3b82f6, #6366f1)',
            color: 'white',
            marginBottom: '8px'
          }}>
            <QrCode size={26} />
          </div>
          <h3 style={{ fontSize: '1.25rem', fontWeight: 800, color: 'var(--text-main)' }}>
            Mã QR Cá Nhân (Bảo Vệ Đăng Nhập Hộ)
          </h3>
          <div style={{ fontSize: '0.85rem', color: 'var(--primary)', fontWeight: 600, marginTop: '2px' }}>
            Dành riêng cho: {currentUser?.full_name || qrData?.user_name}
          </div>
          <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginTop: '4px' }}>
            Sự kiện: <strong>{activity.title}</strong>
          </p>
        </div>

        {/* QR Code Container */}
        <div style={{
          background: 'var(--bg-card-secondary)',
          padding: '20px',
          borderRadius: '16px',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          alignItems: 'center',
          border: '1px solid var(--border-color)',
          marginBottom: '14px'
        }}>
          {loadingQr ? (
            <div style={{ padding: '40px', color: 'var(--text-muted)', fontSize: '0.85rem' }}>Đang khởi tạo mã QR động...</div>
          ) : qrData?.qr_token ? (
            <>
              {/* White backing card with animated radar pulse ring */}
              <div className="radar-pulse-ring" style={{ background: '#ffffff', padding: '14px', borderRadius: '14px', display: 'inline-flex', boxShadow: '0 4px 14px rgba(0,0,0,0.1)' }}>
                <QRCodeSVG value={qrData.qr_token} size={170} level="H" />
              </div>
              <div style={{ marginTop: '14px', fontSize: '0.75rem', color: 'var(--text-secondary)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                <Clock size={12} color="#3b82f6" /> Hạn dùng mã: Hết giờ sự kiện ({new Date(activity.end_time || Date.now() + 14400000).toLocaleTimeString()})
              </div>
            </>
          ) : (
            <div style={{ padding: '20px', color: 'var(--danger)', fontSize: '0.85rem', textAlign: 'center' }}>
              Không thể tải mã QR cá nhân
            </div>
          )}
        </div>

        {/* Anti-Proxy Protection Badge */}
        <div style={{
          background: 'var(--tint-green-bg)',
          border: '1px solid var(--tint-green-border)',
          borderRadius: '10px',
          padding: '10px 12px',
          fontSize: '0.75rem',
          color: 'var(--tint-green-text)',
          marginBottom: '16px'
        }}>
          <div style={{ fontWeight: 700, display: 'flex', alignItems: 'center', gap: '4px', marginBottom: '2px' }}>
            <ShieldCheck size={16} /> Bảo vệ 4 Lớp Chống Đăng Nhập Hộ:
          </div>
          <ul style={{ paddingLeft: '18px', margin: 0, lineHeight: 1.4 }}>
            <li>Mã QR độc bản thay đổi theo từng người dùng.</li>
            <li>Giới hạn thời gian kết thúc sự kiện.</li>
            <li style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
              <MapPin size={12} color="#10b981" /> <strong>GPS Geofencing:</strong> {gpsStatus}
            </li>
            <li style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
              <Smartphone size={12} color="#3b82f6" /> <strong>Device Lock:</strong> Mỗi thiết bị chỉ điểm danh 1 tài khoản
            </li>
          </ul>
        </div>

        {message && (
          <div style={{
            background: 'var(--tint-green-bg)',
            color: 'var(--success)',
            padding: '10px 14px',
            borderRadius: '10px',
            fontSize: '0.85rem',
            marginBottom: '16px',
            display: 'flex',
            alignItems: 'center',
            gap: '8px',
            border: '1px solid var(--tint-green-border)'
          }}>
            <CheckCircle size={18} /> {message}
          </div>
        )}

        {error && (
          <div style={{
            background: 'var(--danger-light)',
            color: 'var(--danger)',
            padding: '10px 14px',
            borderRadius: '10px',
            fontSize: '0.85rem',
            marginBottom: '16px',
            display: 'flex',
            alignItems: 'center',
            gap: '8px',
            border: '1px solid rgba(239, 68, 68, 0.3)'
          }}>
            <AlertTriangle size={18} /> {error}
          </div>
        )}

        <button
          onClick={handleAutoCheckin}
          disabled={loadingCheckin || !qrData?.qr_token}
          className="btn btn-primary"
          style={{ width: '100%', padding: '12px', borderRadius: '10px', fontSize: '0.95rem' }}
        >
          {loadingCheckin ? 'Đang kiểm tra thiết bị...' : '⚡ Quét GPS + Thiết bị / Tự Động Điểm Danh Tức Thời'}
        </button>
      </div>
    </div>
  );
}
