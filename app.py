from flask import Flask, render_template

app = Flask(__name__)

# Định nghĩa tuyến đường chính (URL /)
@app.route('/')
def home():
    # Render file index.html từ thư mục templates
    return render_template('index.html')

if __name__ == '__main__':
    # Chạy ứng dụng Flask
    app.run(debug=True)