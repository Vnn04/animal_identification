from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         uname = request.form['']
#         if uname:
#             return 
#     return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)