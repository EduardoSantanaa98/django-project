import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0',
    port: 3000,
    allowedHosts: [
      "757415c1-de2e-4705-97e2-01570f153aca-00-3jooh70xjxe9t.worf.replit.dev"
    ]
  }

})
