# Grammar Adventure — 英语语法大冒险

## Project
趣味英语语法学习网页应用，面向小学三年级学生。单 HTML 文件，纯前端。

## Key Files
- PRD.md — 完整需求文档（必须先读）
- index.html — 唯一输出文件

## Tech Stack
- 纯 HTML + CSS + JS（无依赖、无构建步骤）
- 所有样式和脚本内联在 index.html 中
- Google Fonts 只允许用 CDN link 引入一个圆润字体（如 "Noto Sans SC"）
- 不加任何 npm 包或构建工具

## Design Tokens
- 主色: #FF6B6B（珊瑚红）, #4ECDC4（青绿）, #FFE66D（明黄）
- 圆角: 16-24px
- 按钮高度: ≥48px
- 字体大小: ≥16px
- 背景: 渐变配小装饰

## Coding Conventions
- 使用 ES6+ 语法
- 所有文本字符串用中文注释说明
- CSS 使用 flexbox 布局
- 移动端优先，media query 适配平板
- 变量名用英文，注释用中文

## Rules
- 必须兼容微信内置浏览器
- 所有数据持久化到 localStorage
- 无需后端、无需登录
- 使用 touch-action: manipulation 防止双击缩放
