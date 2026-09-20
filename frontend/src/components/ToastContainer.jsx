import React from 'react';
import { CheckCircle2, AlertCircle, AlertTriangle, Info, X } from 'lucide-react';
import { useToastContext } from '../context/ToastContext';

export default function ToastContainer() {
  const { toasts, removeToast } = useToastContext();

  if (toasts.length === 0) return null;

  const getToastIcon = (type) => {
    switch (type) {
      case 'success':
        return <CheckCircle2 size={20} color="var(--success)" />;
      case 'error':
        return <AlertCircle size={20} color="var(--danger)" />;
      case 'warning':
        return <AlertTriangle size={20} color="var(--warning)" />;
      case 'info':
      default:
        return <Info size={20} color="var(--primary)" />;
    }
  };

  const getToastBorderColor = (type) => {
    switch (type) {
      case 'success':
        return 'var(--tint-green-border)';
      case 'error':
        return 'rgba(239, 68, 68, 0.4)';
      case 'warning':
        return 'var(--tint-amber-border)';
      case 'info':
      default:
        return 'var(--tint-blue-border)';
    }
  };

  return (
    <div style={{
      position: 'fixed',
      bottom: '24px',
      right: '24px',
      zIndex: 9999,
      display: 'flex',
      flexDirection: 'column',
      gap: '10px',
      maxWidth: '400px',
      width: '100%',
      pointerEvents: 'none'
    }}>
      {toasts.map((t) => (
        <div
          key={t.id}
          className="toast-card-animate"
          style={{
            pointerEvents: 'auto',
            background: 'var(--bg-modal)',
            borderRadius: 'var(--rounded-lg)',
            padding: '14px 16px',
            boxShadow: 'var(--shadow-lg)',
            border: `1px solid ${getToastBorderColor(t.type)}`,
            display: 'flex',
            alignItems: 'flex-start',
            gap: '12px',
            position: 'relative',
            overflow: 'hidden'
          }}
        >
          <div style={{ flexShrink: 0, marginTop: '2px' }}>
            {getToastIcon(t.type)}
          </div>

          <div style={{ flex: 1, paddingRight: '18px' }}>
            {t.title && (
              <div style={{
                fontSize: '0.875rem',
                fontWeight: 700,
                color: 'var(--text-main)',
                marginBottom: '2px'
              }}>
                {t.title}
              </div>
            )}
            <div style={{
              fontSize: '0.825rem',
              color: 'var(--text-secondary)',
              lineHeight: 1.4
            }}>
              {t.message}
            </div>
          </div>

          <button
            onClick={() => removeToast(t.id)}
            style={{
              position: 'absolute',
              top: '10px',
              right: '10px',
              background: 'transparent',
              border: 'none',
              color: 'var(--text-muted)',
              cursor: 'pointer',
              padding: '2px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center'
            }}
          >
            <X size={15} />
          </button>
        </div>
      ))}
    </div>
  );
}
