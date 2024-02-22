from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email_address = db.Column(db.String(100), unique=True, nullable=False)
    country = db.Column(db.String(50))

def validate_user_data(first_name, last_name, email_address, country):
    errors = []
    fields = {
        'first_name': first_name,
        'last_name': last_name,
        'email_address': email_address
    }

    errors = {field: f"{field.replace('_', ' ').title()} is required" for field, value in fields.items() if not value}

    if email_address and not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_address):
        errors['email_address'] = 'Invalid email address'


    valid_countries = ['Ireland', 'United States']
    if country and country not in valid_countries:
        errors.append('Invalid country')

    return errors

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'Invalid request body'}), 400

    attributes = data.get('attributes')
    if not attributes:
        return jsonify({'error': 'Attributes are missing'}), 400

    first_name = attributes.get('first_name')
    last_name = attributes.get('last_name')
    email_address = attributes.get('email_address')
    country = attributes.get('country')

    validation_errors = validate_user_data(first_name, last_name, email_address, country)
    if validation_errors:
        return jsonify({'errors': validation_errors}), 400

    try:
        new_user = User(first_name=first_name, last_name=last_name,
                        email_address=email_address, country=country)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email address already exists'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/users', methods=['GET'])
def get_user():
    sort_field = request.args.get('sort', 'first_name')
    if sort_field not in ['first_name', 'last_name', 'email_address', 'country']:
        return jsonify({'error': 'Invalid sort field'}), 400

    users_query = User.query.order_by(getattr(User, sort_field).desc())
    users_list = [{'first_name': user.first_name, 'last_name': user.last_name, 'email_address': user.email_address, 'country': user.country} for user in users_query]
    return jsonify(users_list)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
