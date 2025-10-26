# 简单的Django项目

这是一个基础的Django项目，包含基本的功能和配置。

## 项目结构

```
dj/
├── manage.py          # Django项目管理脚本
├── mysite/            # 项目主目录
│   ├── __init__.py
│   ├── settings.py    # 项目设置
│   ├── urls.py        # URL路由配置
│   ├── wsgi.py        # WSGI配置
├── myapp/             # 自定义应用
│   ├── __init__.py
│   └── views.py       # 视图函数
├── venv/              # Python虚拟环境
└── requirements.txt   # 项目依赖
```

## 安装和运行

1. **激活虚拟环境**（Windows）：
   ```powershell
   venv\Scripts\activate
   ```

2. **安装依赖**：
   ```powershell
   pip install -r requirements.txt
   ```

3. **运行数据库迁移**：
   ```powershell
   python manage.py migrate
   ```

4. **创建超级用户**（可选，用于管理后台）：
   ```powershell
   python manage.py createsuperuser
   ```

5. **启动开发服务器**：
   ```powershell
   python manage.py runserver
   ```

6. **访问网站**：
   - 首页：http://127.0.0.1:8000/
   - 管理后台：http://127.0.0.1:8000/admin/

## 功能特性

- ✅ Django 5.0 框架
- ✅ SQLite 数据库
- ✅ 管理后台
- ✅ 中文语言设置
- ✅ 亚洲/上海时区
- ✅ 基本的Web界面

## 下一步

您可以：
1. 添加更多应用和功能
2. 自定义模板和样式
3. 连接其他数据库
4. 部署到生产环境