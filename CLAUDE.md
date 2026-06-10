# 趣味英语语法绘本 — Grammar Picture Book

## Project
基于《趣味英语语法》1-4册的交互式英语语法学习网页（单页 HTML），面向小学三年级学生。
不是答题/测验，而是**绘本式浏览学习**。

## Key Files
- `PRD_v2.md` — 完整设计需求（必须先读）
- `index.html` — 唯一输出文件

## Tech Stack
- 纯 HTML + CSS + JS（无依赖、无构建步骤）
- 所有样式和脚本内联在 index.html 中
- 字体: Google Fonts "Noto Sans SC"（标题）+ 系统字体
- 不使用任何外部 JS 库或框架

## Design Tokens
- 主色: #FF6B6B, #4ECDC4, #FFE66D, #A29BFE
- 背景: #FFF5F5 → #F0FFF4 渐变
- 圆角: 16-32px
- 按钮/可点击区域: ≥48px
- 正文字体: ≥16px
- 标题: font-weight 900, 颜色 #FF6B6B

## Architecture
采用 **页面切换模式**（类似SPA）:
- `page-home` — 书架视图，显示4册书
- `page-chapters` — 某册书的章节列表
- `page-lesson` — 绘本式翻页学习（核心页面）
- `page-interactive` — 互动示例页面
- `page-progress` — 学习进度

## Data Flow
- 所有课程数据硬编码在 JS 的 `LESSONS` 数组中
- 用户进度存 localStorage（key: `grammar_picture_book`）
- 状态: { completedLessons: [], stars: {}, lastLesson: null }

## Content Priority (基于书本实际内容)
只实现 **第1册和第2册**的内容（适合3年级），第3-4册做占位符。
每课包含:
1. Grammy 猫咪的讲解气泡
2. 3-5页绘本式内容（图文并茂）
3. 1个互动示例（拖拽/点击/滑动）
4. 「动手试试」环节（低压力互动，不记分）

## Coding Conventions
- 所有字符串用中文标注注释
- CSS 使用 flexbox + grid 布局
- 纯原生 JS，用 ES6 class 管理页面
- 动画用 CSS @keyframes + transition
- 变量命名: camelCase，注释用中文
- 手机优先，media query 适配平板

## Critical Rules
1. 不要答题/测验形式 — 是绘本式学习
2. 每个知识点都要有 Grammy 猫咪🐱出现
3. 所有交互必须是低压力、探索式的
4. 必须兼容微信内置浏览器
5. 所有数据存在 localStorage
6. 首次加载必须有欢迎动画
7. 每课完成后有庆祝动画（星星+猫咪跳舞）
