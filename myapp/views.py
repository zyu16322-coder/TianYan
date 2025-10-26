from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """首页视图"""
    return HttpResponse("""
    <html>
    <head>
        <title>我的Django网站</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h1 { color: #333; }
            .container { max-width: 800px; margin: 0 auto; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>欢迎来到我的Django网站！</h1>
            <p>这是一个简单的Django项目示例。</p>
            <p>功能包括：</p>
            <ul>
                <li>Django管理后台</li>
                <li>SQLite数据库</li>
                <li>基本的Web框架</li>
            </ul>
            <p><a href="/admin/">访问管理后台</a></p>
        </div>
    </body>
    </html>
    """)