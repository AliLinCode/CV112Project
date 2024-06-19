from flask import request, jsonify, current_app as app
from .models import User, db

@app.route('/')
def index():
    return "Welcome to my Flask app!"

@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'POST':
        username = request.json.get('username')
        email = request.json.get('email')
        if username and email:
            user = User(username=username, email=email)
            db.session.add(user)
            db.session.commit()
            return jsonify({'message': 'User created!'}), 201
        return jsonify({'message': 'Bad request!'}), 400
    users = User.query.all()
    return jsonify([{'username': user.username, 'email': user.email} for user in users])
