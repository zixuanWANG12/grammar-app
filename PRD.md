# 🎯 小学三年级趣味英语语法学习应用

## 一、项目概述

一个面向小学三年级学生的趣味英语语法学习网页应用。**通过微信分享链接即可打开**，无需安装任何软件。界面卡通可爱、互动性强，让孩子在闯关游戏中掌握基础英语语法。

## 二、目标用户

- **主要用户**：小学三年级学生（8-9岁），英语语法基础薄弱
- **使用场景**：在微信里打开链接，用手机/平板学习
- **设计原则**：有趣＞严谨，鼓励＞纠错，简单＞全面

## 三、技术方案

- 纯前端单页应用（HTML + CSS + JavaScript）
- 单个 HTML 文件（或少量文件），方便部署
- **Mobile-first** 响应式设计，适配手机屏幕
- 兼容微信内置浏览器
- 部署到 GitHub Pages / Vercel 等免费托管

## 四、UI/UX 设计要求

### 整体风格
- **配色**：明亮活泼。主色 #FF6B6B（珊瑚红）、#4ECDC4（青绿）、#FFE66D（明黄）
- **字体**：圆润可爱，使用系统字体 + 适当 emoji 装饰
- **圆角**：大圆角（16-24px），所有卡片/按钮都有圆角
- **按钮**：大尺寸（至少 48px 高度），适合儿童手指点击
- **动画**：轻微的弹出、滑动、跳动动画，使交互有反馈感
- **背景**：渐变色或带小装饰的纯色背景

### 页面结构

#### 1. 首页（学习主题选择）
- 顶部：可爱的应用标题 🎮 "英语语法大冒险" + 吉祥物 emoji 🐼
- 中间：8 个学习主题卡片，每个卡片包含：
  - 主题图标（emoji）
  - 主题名称（中英文）
  - 已完成/总题数（如 "⭐ 4/5"）
  - 未完成时显示"🔒" 或 "👉 开始"
- 底部：总星星数 / 总进度

#### 2. 答题页
- 顶部：当前主题名称 + 题目进度（如 "第 3/5 题"）
- 中部：题目展示区
  - 一句话题干（中英文对照更佳）
  - 句子中填空处用 ____ 或 [  ] 标记
  - 4 个选项按钮（大圆角卡片）
  - 选项可以是 A/B/C/D 或直接点选项
- 选择后：
  - ✅ 正确：绿色闪烁 + "太棒了！🎉" + 下一题按钮
  - ❌ 错误：红色 + "再想想哦～💪" + 正确答案高亮 + 下一题按钮（2秒后自动出现）

#### 3. 主题完成页
- 星星评分：0-3 星（≥4/5 正确=3星, ≥3/5=2星, <3=1星, 0=0星）
- 鼓励语：不同评分配不同的话
- "继续闯关"按钮返回首页
- "再学一次"按钮重新答题

## 五、语法学习内容（8个主题，每个5题）

### 主题1：a 还是 an？ 🎯
判断名词前面用 a 还是 an，**标注拼音**帮助认字。

题目示例：
1. ____ apple  → an
2. ____ cat    → a
3. ____ elephant → an
4. ____ dog    → a
5. ____ orange → an

### 主题2：am / is / are（我是谁）👤
人称代词与 be 动词的搭配。

题目示例：
1. I ____ a student. → am
2. She ____ my sister. → is
3. They ____ happy. → are
4. He ____ a teacher. → is
5. We ____ friends. → are

### 主题3：have / has（谁有谁）🎒
have / has 的用法区分。

题目示例：
1. I ____ a book. → have
2. She ____ a cat. → has
3. They ____ toys. → have
4. He ____ a bike. → has
5. We ____ a big house. → have

### 主题4：名词变复数 🐱🐱
单数变复数的基本规则（+s / +es）。

题目示例：
1. one cat, two ____ → cats
2. one bus, two ____ → buses
3. one dog, two ____ → dogs
4. one box, two ____ → boxes
5. one book, two ____ → books

### 主题5：人称代词 👧👦
I / you / he / she / it 的区分。

题目示例：
1. ____ am a girl. (我) → I
2. ____ is my father. (他) → He
3. ____ is a cat. (它) → It
4. ____ are my friend. (你) → You
5. ____ is my mother. (她) → She

### 主题6：do / does（问问题）❓
一般现在时疑问句中 do / does 的用法。

题目示例：
1. ____ you like apples? → Do
2. ____ she like cats? → Does
3. ____ they play football? → Do
4. ____ he go to school? → Does
5. ____ we have time? → Do

### 主题7：形容词比一比 📏
big / bigger, small / smaller 等基本比较级。

题目示例：
1. A car is ____ than a bike. (faster) → faster
2. An elephant is ____ than a cat. (bigger) → bigger
3. A mouse is ____ than a dog. (smaller) → smaller
4. A rabbit is ____ than a turtle. (faster) → faster
5. A giraffe is ____ than a horse. (taller) → taller

### 主题8：变否定句 ✋
在句子中加 don't / doesn't。

题目示例：
1. I ____ like broccoli. (don't) → don't
2. She ____ have a pet. (doesn't) → doesn't
3. They ____ play chess. (don't) → don't
4. He ____ eat meat. (doesn't) → doesn't
5. We ____ go to school on Sunday. (don't) → don't

## 六、功能规格

### 核心功能
1. 选择主题开始答题
2. 每题 4 个选项，点击选择
3. 即时反馈（正确/错误 + 鼓励语 + 音效）
4. 每题自动显示正确答案（选错时）
5. 主题完成后显示星星评分
6. 进度持久化（localStorage）

### 进度保存
- 使用浏览器的 localStorage
- 保存每个主题的最高分数（星星数）
- 保存每个主题的完成状态
- 下次打开自动恢复进度

### 趣味元素
- 每次答对显示随机鼓励语（"太棒了！🎉" "你真聪明！⭐" "继续加油！💪" 等 10+ 种）
- 答错时显示温和的提示
- 全部完成后显示庆祝动画（彩纸/星星）
- 顶部显示总星星收集进度

## 七、技术约束

- 必须兼容微信内置浏览器（基于 Chromium）
- 无需登录、无需注册、无后端
- 所有数据存在 localStorage
- 页面体积尽量小，加载快
- 支持触控交互（touch events）
- 字体大小至少 16px，防止 iOS 自动缩放

## 八、交付物

- 1 个完整的 HTML 文件（含所有 CSS 和 JavaScript）
- 在浏览器中打开即可使用
- 可直接部署到 GitHub Pages
