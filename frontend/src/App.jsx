import React, { useState, useEffect } from 'react';
import { getStoredUser, getAuthToken, removeAuthToken } from './api/client';
import Login from './pages/Login';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import Members from './pages/Members';
import Activities from './pages/Activities';
import Tasks from './pages/Tasks';
import AIHub from './pages/AIHub';
import Leaderboard from './pages/Leaderboard';

import ToastContainer from './components/ToastContainer';

export default function App() {
  const [user, setUser] = useState(null);
  const [activeTab, setActiveTab] = useState('dashboard');
  const [aiHubSubTab, setAiHubSubTab] = useState('suggest');

  useEffect(() => {
    const token = getAuthToken();
    const storedUser = getStoredUser();
    if (token && storedUser) {
      setUser(storedUser);
    }
  }, []);

  const handleLoginSuccess = (loggedInUser) => {
    setUser(loggedInUser);
    setActiveTab('dashboard');
  };

  const handleLogout = () => {
    removeAuthToken();
    setUser(null);
  };

  const handleNavigateToAiHub = (subTab = 'suggest') => {
    setAiHubSubTab(subTab);
    setActiveTab('aihub');
  };

  if (!user) {
    return (
      <>
        <Login onLoginSuccess={handleLoginSuccess} />
        <ToastContainer />
      </>
    );
  }

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column', background: 'var(--bg-main)', color: 'var(--text-main)', transition: 'background-color 0.25s ease' }}>
      <Navbar user={user} onLogout={handleLogout} />

      <div style={{ display: 'flex', flex: 1 }}>
        <Sidebar activeTab={activeTab} setActiveTab={setActiveTab} />

        <main style={{ flex: 1, padding: '28px 36px', overflowY: 'auto', maxWidth: '1400px' }}>
          {activeTab === 'dashboard' && <Dashboard currentUser={user} onNavigate={(tab) => setActiveTab(tab)} />}
          {activeTab === 'members' && <Members currentUser={user} />}
          {activeTab === 'activities' && <Activities currentUser={user} />}
          {activeTab === 'tasks' && <Tasks currentUser={user} onNavigateToAiHub={handleNavigateToAiHub} />}
          {activeTab === 'aihub' && <AIHub initialTab={aiHubSubTab} />}
          {activeTab === 'leaderboard' && <Leaderboard />}
        </main>
      </div>

      <ToastContainer />
    </div>
  );
}
