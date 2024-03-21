from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# trang home
@app.route('/home')
def home():
    return render_template('index1.html')


# trang login
@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        uname = request.form['uname']
        psw = request.form['psw']
        if uname and psw is not None:
            return redirect(url_for('home'))
    return render_template('login.html')

# trang sign up
@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9999', debug=True)