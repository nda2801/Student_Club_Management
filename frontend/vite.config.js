import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  // Tự động load các biến VITE_* từ file .env ở thư mục gốc (Root)
  envDir: path.resolve(__dirname, '..'),
})

