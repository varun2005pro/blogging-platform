from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy blog data
blogs = []

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(blogs)

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    blogs.append(data)
    return jsonify({"message": "Post added"}), 201

if __name__ == '__main__':
    app.run(debug=True)