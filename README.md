# vue-flask-book
Core Objective: Full-process digital management of book creation, query &amp; deletion. Core Work: 1. Backend: Build RESTful APIs (Flask), configure flask-cors, use Flask-RESTX for param verification &amp; Swagger docs. 2. Frontend: Componentized UI (Vue3+Vite), data communication via Axios. 3. Integration testing &amp; deliver runnable prototype.

启动后端（Flask）
  # 进入 backend 目录
  cd backend
  # 安装依赖（新增 flask-restx）
  pip install flask flask-cors flask-restx
  # 启动服务
  python app.py
  # 成功后访问：
  # - 接口地址：http://localhost:5000/api/books
  # - Swagger 文档：http://localhost:5000/swagger
启动前端（Vite + Vue）
  # 回到项目根目录
  cd ..
  # 安装依赖（首次运行）
  npm install
  # 启动开发服务器
  npm run dev
  # 访问页面：http://127.0.0.1:5173
