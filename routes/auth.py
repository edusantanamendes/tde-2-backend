from flask import Blueprint, request, jsonify
from app import db
from models.user_model import User
from utils.jwt_util import generate_token
from datetime import datetime
auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    email = data.get('email')
    senha = data.get('senha')
    if not email or not senha:
        return jsonify({'erro':'email e senha obrigatórios'}), 400
    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(senha):
        return jsonify({'erro':'credenciais inválidas'}), 401
    token = generate_token(user.id, user.tipo)
    return jsonify({'token': token, 'usuario': user.to_dict()}), 200
