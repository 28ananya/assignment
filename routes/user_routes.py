from flask import Blueprint, request, jsonify
from models.user_model import UserModel, AdminModel
from utils.auth import hash_password, verify_password, generate_jwt
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint('user', __name__)

# Register a new user
@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    if not data.get('email') or not data.get('password'):
        return jsonify({"error": "Email and password are required"}), 400
    
    user = UserModel.find_user_by_email(data['email'])
    if user:
        return jsonify({"error": "User already exists"}), 400
    
    hashed_pw = hash_password(data['password'])
    data['password'] = hashed_pw
    UserModel.insert_user(data)
    return jsonify({"message": "User registered successfully"}), 201

# User login
@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    user = UserModel.find_user_by_email(data['email'])
    if user and verify_password(data['password'], user['password']):
        token = generate_jwt(user['email'])
        return jsonify({"access_token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

# Upload an assignment
@user_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload_assignment():
    data = request.json
    current_user = get_jwt_identity()
    if not data.get('task') or not data.get('admin'):
        return jsonify({"error": "Task and Admin are required"}), 400

    data['user_id'] = current_user
    UserModel.insert_assignment(data)
    return jsonify({"message": "Assignment uploaded successfully"}), 201

# Fetch all admins
@user_bp.route('/admins', methods=['GET'])
@jwt_required()
def fetch_all_admins():
    admins = AdminModel.get_all_admins()
    return jsonify(admins), 200



