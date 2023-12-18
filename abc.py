from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Placeholder for user credentials (replace with a proper database in a real application)
users = {'ops_user': 'ops_password'}


# Define a decorator function to check if the user is an Ops User
def ops_user_required(f):
    def wrapper(*args, **kwargs):
        user_type = request.headers.get('User-Type')
        if user_type == 'Ops':
            return f(*args, **kwargs)
        else:
            return jsonify({'error': 'Unauthorized'}), 401

    return wrapper


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username] == password:
        # For simplicity, assuming all users are Ops users in this example
        return render_template('upload.html', username=username)
    else:
        return render_template('login.html', error='Invalid credentials')


#@app.route('/upload', methods=['POST'])
#@ops_user_required
#def upload_file():
    # Your existing upload_file code here

# Rest of the code remains unchanged


if __name__ == '__main__':
    app.run(debug=True)