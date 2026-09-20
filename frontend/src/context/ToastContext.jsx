import React, { createContext, useContext, useState, useCallback } from 'react';

const ToastContext = createContext(null);

export function ToastProvider({ children }) {
  const [toasts, setToasts] = useState([]);

  const removeToast = useCallback((id) => {
    setToasts((prev) => prev.filter((t) => t.id !== id));
  }, []);

  const addToast = useCallback((message, type = 'info', title = '', duration = 3500) => {
    const id = Date.now().toString(36) + Math.random().toString(36).substring(2, 6);
    const newToast = { id, message, type, title };

    setToasts((prev) => [...prev.slice(-4), newToast]); // Keep maximum 5 toasts

    if (duration > 0) {
      setTimeout(() => {
        removeToast(id);
      }, duration);
    }
    return id;
  }, [removeToast]);

  const toast = {
    success: (msg, title = 'Thành công') => addToast(msg, 'success', title),
    error: (msg, title = 'Có lỗi xảy ra') => addToast(msg, 'error', title, 5000),
    info: (msg, title = 'Thông báo') => addToast(msg, 'info', title),
    warning: (msg, title = 'Cảnh báo') => addToast(msg, 'warning', title, 4000),
  };

  return (
    <ToastContext.Provider value={{ toasts, removeToast, addToast, toast }}>
      {children}
    </ToastContext.Provider>
  );
}

export function useToast() {
  const context = useContext(ToastContext);
  if (!context) {
    throw new Error('useToast must be used within a ToastProvider');
  }
  return context.toast;
}

export function useToastContext() {
  const context = useContext(ToastContext);
  if (!context) {
    throw new Error('useToastContext must be used within a ToastProvider');
  }
  return context;
}
