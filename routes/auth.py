from flask import request, jsonify
from app import app, db
from models import User

import bcrypt

from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

from datetime import timedelta


# REGISTER API
@app.route('/register', methods=['POST'])
def register():

    data = request.get_json()

    hashed_password = bcrypt.hashpw(
        data['password'].encode('utf-8'),
        bcrypt.gensalt()
    )

    new_user = User(
        username=data['username'],
        password=hashed_password.decode('utf-8')
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    })


# LOGIN API
@app.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    user = User.query.filter_by(
        username=data['username']
    ).first()

    if not user:
        return jsonify({
            "message": "User not found"
        }), 404

    if bcrypt.checkpw(
        data['password'].encode('utf-8'),
        user.password.encode('utf-8')
    ):

        access_token = create_access_token(
            identity=user.username,
            expires_delta=timedelta(hours=1)
        )

        return jsonify({
            "token": access_token
        })

    return jsonify({
        "message": "Invalid credentials"
    }), 401


# PROTECTED ROUTE
@app.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():

    current_user = get_jwt_identity()

    return jsonify({
        "message": f"Welcome {current_user}"
    })