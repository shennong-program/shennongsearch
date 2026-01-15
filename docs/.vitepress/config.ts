import { defineConfig } from 'vitepress'

const zhSidebar = [
  {
    text: 'API',
    items: [
      { text: 'Name 查询接口', link: '/zh/api/name' },
      { text: 'SNNMM 查询接口', link: '/zh/api/snnmm' },
    ],
  },
]

const enSidebar = [
  {
    text: 'API',
    items: [
      { text: 'Name Query API', link: '/en/api/name' },
      { text: 'SNNMM Query API', link: '/en/api/snnmm' },
    ],
  },
]

export default defineConfig({
  title: 'ShennongSearch',
  description: 'Python SDK for ShennongAlpha search APIs',
  base: process.env.BASE_URL || '/',
  cleanUrls: true,
  lang: 'en-US',
  themeConfig: {
    search: {
      provider: 'local',
    },
  },
  locales: {
    zh: {
      label: '中文',
      lang: 'zh-CN',
      link: '/zh/',
      themeConfig: {
        nav: [{ text: 'API', link: '/zh/api/name' }],
        sidebar: {
          '/zh/': zhSidebar,
        },
      },
    },
    en: {
      label: 'English',
      lang: 'en-US',
      link: '/en/',
      themeConfig: {
        nav: [{ text: 'API', link: '/en/api/name' }],
        sidebar: {
          '/en/': enSidebar,
        },
      },
    },
  },
})
