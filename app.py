from flask import Flask, request, jsonify, Response
import json

app = Flask(__name__)

records = [
    {
        'id': 1,
        'description': 'this is the test record 1'
    },
    {
        'id': 2,
        'description': 'this is the test record 2'
    },
    {
        'id': 3,
        'description': 'this is the test record 3'
    }
]

@app.route('/')
def home():
    return 'FLASK REST API!'

@app.route('/api/v1/records', methods=['GET'])
def get_all():
    return jsonify(records)

@app.route('/api/v1/records/<int:id>', methods=['GET'])
def get(id):
    for rec in records:
        if rec['id'] == id:
            return jsonify(rec)

@app.route('/api/v1/records', methods=['POST'])
def post():
    data = request.data
    content = json.loads(data)
    records.append(content)
    return Response(status=200)

@app.route('/api/v1/records/<int:id>', methods=['PUT'])
def put(id):
    data = request.data
    content = json.loads(data)
    for rec in records:
        if rec['id']==id:
            indx = records.index(rec)
            records[indx] = content
            break
    return Response(status=200)

@app.route('/api/v1/records/<int:id>', methods=['DELETE'])
def delete(id):
    for rec in records:
        if rec['id']==id:
            records.remove(rec)
            break
    return Response(status=200)

@app.route('/api/v1/image', methods=['POST'])
def postImage():
    data = request.data
    mimetype = request.mimetype
    return Response(response=data, status=200, mimetype=mimetype)

if __name__ == '__main__':
    app.run()
