from mongo_functions import *
from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = '825'
is_loggedin = False

@app.route('/')
def index():
    if 'username' in session:
        is_loggedin = session.pop('is_loggedin', False)

        if is_loggedin:
            return render_template('index.html', is_loggedin=True, button_text="Logout")

        else:
            return render_template('index.html', is_loggedin=False, button_text="Login | Sign In")

    return render_template('index.html', is_loggedin=False, button_text="Login | Sign In")
    # return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'is_loggedin' in session:
        session['is_loggedin'] = False

    if request.method == 'POST':
        username = request.form.get('username') 
        password = request.form.get('password')
        
        if authenticate_team(username, password):
            session['username'] = username
            session['is_loggedin'] = True

            return redirect(url_for('index'))
        else:
            redirect(url_for('signup'))

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form.get('fullname').strip()
        username = request.form.get('username').strip()
        email = request.form.get('email').strip()
        password = request.form.get('password')
        
        print(colored(f"{full_name, username, email, password}", "green"))

        if add_user(
            full_name,
            username,
            email,
            password
        ):
            return redirect(url_for('login'))
        else:
            return jsonify({"message": "failed to add the user"})

    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('is_loggedin', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()