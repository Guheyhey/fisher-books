from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    headers = {
        'content-type': 'application/json'
    }
    payload = ('hello', 'world')
    return jsonify(payload), 200, headers


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])
