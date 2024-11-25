# Import necessary modules from Flask
# 从Flask导入必要的模块
from flask import Flask, render_template, request

# Initialize Flask application
# 初始化Flask应用
app = Flask(__name__)


# Route decorator to handle both GET and POST requests at root URL "/"
# 路由装饰器处理根URL"/"的GET和POST请求
@app.route("/", methods=["GET", "POST"])
def hello():
    # Check if the request method is POST (form submission)
    # 检查请求方法是否为POST（表单提交）
    if request.method == "POST":
        # Extract form data using request.form dictionary, .get() method safely returns None if field doesn't exist.
        # 使用request.form字典提取表单数据，.get()方法在字段不存在时安全地返回None。
        name = request.form.get("name")
        email = request.form.get("email")

        # Return a simple confirmation message with submitted data
        # In a real application, you might:
        # - Save to database
        # - Validate the data
        # - Redirect to another page
        # 返回一个包含提交数据的简单确认消息
        # 在实际应用中，你可能需要：
        # - 保存到数据库
        # - 验证数据
        # - 重定向到另一个页面
        return f"Form submitted! Name: {name}, Email: {email}"

    # If request is GET, render the form template
    # index.html should be in the templates directory
    # 如果请求是GET，渲染表单模板
    # index.html应该在templates目录中
    return render_template("index.html")


# Run the application if this file is executed directly
# 如果直接执行此文件，则运行应用
if __name__ == "__main__":
    # Start Flask development server on port 8080
    # Debug mode is off by default for security
    # 在端口8080上启动Flask开发服务器
    # 出于安全考虑，调试模式默认关闭
    app.run(port=8080)
