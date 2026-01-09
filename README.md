# Vue-Flask 图书管理系统

## 项目概述
### 核心目标
实现图书新增、查询、删除全流程的数字化管理。

### 核心工作
1. **后端**：基于 Flask 构建 RESTful API，配置 flask-cors 解决跨域问题，使用 Flask-RESTX 实现参数校验和 Swagger 接口文档生成。
2. **前端**：基于 Vue3+Vite 实现组件化 UI 开发，通过 Axios 完成前后端数据通信。
3. **集成测试**：完成前后端联调测试，交付可运行的原型系统。

## 环境启动步骤
### 一、启动后端（Flask）
1. 进入 backend 目录
   ```bash
   cd backend
   ```
2. 安装依赖（包含 flask-restx）
   ```bash
   pip install -r requirements.txt
   ```
3. 启动服务
   ```bash
   python app.py
   ```
4. 验证启动结果
   - 接口访问地址：http://localhost:5000
   - Swagger 文档地址：http://localhost:5000/swagger

### 二、启动前端（Vite + Vue3）
1. 新建一个终端（不要关闭后端终端），回到项目根目录
   ```bash
   cd ..
   ```
2. 安装依赖（首次运行时执行）
   ```bash
   npm install
   ```
3. 启动开发服务器
   ```bash
   npm run dev
   ```
4. 访问前端页面
   - 页面地址：http://localhost:5173

## 补充说明
- 环境要求：本地需提前安装 Python（3.7 及以上版本）和 Node.js（14 及以上版本）。
- 端口注意：启动前确认 5000（后端）、5173（前端）端口未被其他程序占用。
- 接口调试：Swagger 文档可直接用于接口调试，直观验证参数校验规则和接口返回结果。
- 数据库：使用 SQLite 嵌入式数据库，无需手动部署，启动后端后自动生成 / 读取本地数据库文件

