from flask import Flask, request, jsonify, Response, abort
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
    if len(records) > 0:
        return jsonify(records)
    return Response(204)

@app.route('/api/v1/records/<int:id>', methods=['GET'])
def get(id):
    for rec in records:
        if rec['id'] == id:
            return jsonify(rec)
    return Response(status=204)

@app.route('/api/v1/records', methods=['POST'])
def post():
    data = request.data
    content = json.loads(data)
    records.append(content)
    return jsonify(content)

@app.route('/api/v1/records/<int:id>', methods=['PUT'])
def put(id):
    found = False
    data = request.data
    content = json.loads(data)
    for rec in records:
        if rec['id']==id:
            indx = records.index(rec)
            records[indx] = content
            found = True
            break
    if found:
        return Response(status=200)
    return abort(404)

@app.route('/api/v1/records/<int:id>', methods=['DELETE'])
def delete(id):
    found = False
    for rec in records:
        if rec['id']==id:
            found = True
            records.remove(rec)
            break
    if found:
        return Response(status=200)
    return abort(404)

@app.route('/api/v1/image', methods=['POST'])
def postImage():
    reqData = request.data
    reqMimetype = request.mimetype
    return Response(response=reqData, status=200, mimetype=reqMimetype)

if __name__ == '__main__':
    app.run()
