from flask import Blueprint, request, jsonify
from models.user_model import AdminModel
from utils.auth import hash_password, verify_password, generate_jwt
from flask_jwt_extended import jwt_required, get_jwt_identity

admin_bp = Blueprint('admin', __name__)

# Register a new admin
@admin_bp.route('/register', methods=['POST'])
def register_admin():
    data = request.json
    if not data.get('email') or not data.get('password'):
        return jsonify({"error": "Email and password are required"}), 400
    
    admin = AdminModel.find_admin_by_email(data['email'])
    if admin:
        return jsonify({"error": "Admin already exists"}), 400
    
    hashed_pw = hash_password(data['password'])
    data['password'] = hashed_pw
    AdminModel.insert_admin(data)
    return jsonify({"message": "Admin registered successfully"}), 201

# Admin login
@admin_bp.route('/login', methods=['POST'])
def login_admin():
    data = request.json
    admin = AdminModel.find_admin_by_email(data['email'])
    if admin and verify_password(data['password'], admin['password']):
        token = generate_jwt(admin['email'])
        return jsonify({"access_token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

# View assignments tagged to the admin
@admin_bp.route('/assignments', methods=['GET'])
@jwt_required()
def view_assignments():
    current_admin = get_jwt_identity()
    assignments = AdminModel.get_assignments_for_admin(current_admin)
    return jsonify(assignments), 200

# Accept an assignment
@admin_bp.route('/assignments/<assignment_id>/accept', methods=['POST'])
@jwt_required()
def accept_assignment(assignment_id):
    AdminModel.update_assignment_status(assignment_id, "Accepted")
    return jsonify({"message": "Assignment accepted"}), 200

# Reject an assignment
@admin_bp.route('/assignments/<assignment_id>/reject', methods=['POST'])
@jwt_required()
def reject_assignment(assignment_id):
    AdminModel.update_assignment_status(assignment_id, "Rejected")
    return jsonify({"message": "Assignment rejected"}), 200
