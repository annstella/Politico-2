from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

user_list = []
@app.route('/get_hello', methods=['GET'])
def hello():
    return 'This is a content from Kenya-tech.com'


