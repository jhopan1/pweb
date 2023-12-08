from flask import Blueprint, jsonify, request, render_template
from Models.UserModel import User, db

main_bp = Blueprint('main', __name__)

@main_bp.route('/add_user', methods=['POST'])
def add_user():
    data = request.json  # Mengambil data JSON dari body permintaan

    # Memeriksa keberadaan username dan password dalam data JSON
    if 'username' not in data or 'password_hash' not in data:
        return jsonify({'error': 'Missing username or password'}), 400

    new_user = User(username=data['username'])
    new_user.set_password(data['password_hash'])
    
    db.session.add(new_user)
    db.session.commit()


    return jsonify({'message': 'User added successfully'}), 201

@main_bp.route('/login', methods=['POST'])
def login():
    data = request.json  # Mengambil data JSON dari body permintaan

    # Memeriksa keberadaan username dan password dalam data JSON
    if 'username' not in data or 'password_hash' not in data:
        return jsonify({'error': 'Missing username or password'}), 400

    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password_hash']):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

@main_bp.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username} for user in users]
    return jsonify({'users': user_list})
