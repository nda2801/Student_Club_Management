// API Base URL - Configured for Flask Backend
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || (
  window.location.port === '5173' || window.location.port === '3000' 
    ? 'http://localhost:5000/api/v1' 
    : '/api/v1'
);

export const getAuthToken = () => localStorage.getItem('token');
export const setAuthToken = (token) => localStorage.setItem('token', token);
export const removeAuthToken = () => {
  localStorage.removeItem('token');
  localStorage.removeItem('user');
};
export const getStoredUser = () => {
  const user = localStorage.getItem('user');
  return user ? JSON.parse(user) : null;
};
export const setStoredUser = (user) => localStorage.setItem('user', JSON.stringify(user));

async function request(endpoint, options = {}) {
  const token = getAuthToken();
  const headers = {
    'Content-Type': 'application/json',
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
    ...options.headers,
  };

  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    ...options,
    headers,
  });

  if (response.status === 401) {
    removeAuthToken();
    window.location.reload();
    throw new Error('Hết phiên đăng nhập');
  }

  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.detail || 'Có lỗi xảy ra');
  }
  return data;
}

export const api = {
  // Auth
  login: async (username, password) => {
    const response = await fetch(`${API_BASE_URL}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password }),
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || 'Đăng nhập thất bại');
    setAuthToken(data.access_token);
    setStoredUser(data.user);
    return data;
  },
  getMe: () => request('/auth/me'),

  // Members & Depts
  getMembers: () => request('/members'),
  updateMember: (id, data) => request(`/members/${id}`, { method: 'PUT', body: JSON.stringify(data) }),
  getDepartments: () => request('/departments'),

  // Activities & Dynamic QR
  getActivities: () => request('/activities'),
  createActivity: (data) => request('/activities', { method: 'POST', body: JSON.stringify(data) }),
  getMyQr: (activityId) => request(`/activities/${activityId}/my-qr`),
  checkinActivity: (data) => request('/activities/checkin', { method: 'POST', body: JSON.stringify(data) }),

  // Tasks & Kanban
  getTasks: (activityId) => request(`/tasks${activityId ? `?activity_id=${activityId}` : ''}`),
  createTask: (data) => request('/tasks', { method: 'POST', body: JSON.stringify(data) }),
  updateTaskStatus: (id, status) => request(`/tasks/${id}/status`, { method: 'PUT', body: JSON.stringify({ status }) }),
  assignTask: (data) => request('/tasks/assign', { method: 'POST', body: JSON.stringify(data) }),

  // AI Features
  generateAnnouncement: (data) => request('/ai/generate-announcement', { method: 'POST', body: JSON.stringify(data) }),
  summarizeActivity: (data) => request('/ai/summarize-activity', { method: 'POST', body: JSON.stringify(data) }),
  suggestAssignments: (data) => request('/ai/suggest-assignments', { method: 'POST', body: JSON.stringify(data) }),

  // Stats
  getDashboardStats: () => request('/stats/dashboard'),
  getLeaderboard: () => request('/stats/leaderboard'),
};
