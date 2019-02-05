from flask import Flask, jsonify, make_response, request
from app.models import Parties

app = Flask(__name__)

party_list = []
@app.route('/api/V1/parties', methods=['GET'])
def get():
    all_parties = Parties.get_all()
    return make_response(jsonify({
        "status": 200,
        "data": all_parties
    }))

@app.route('/createparty', methods=['POST'])
def create_party():
    data = request.get_json()
    name = data['name']
    email = data['email']

    new_user = {
        "name": name,
        "email": email
    }


