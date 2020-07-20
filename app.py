from flask import Flask, request
from funcs import count_islands
import os

app = Flask(__name__)
port = os.getenv('ENDPOINT_PORT') or 5000
host = os.getenv('ENDPOINT_HOST') or '0.0.0.0'


@app.route('/api/islands', methods=['POST'])
def islands():
    body_dict = request.json
    x = body_dict['x']
    y = body_dict['y']
    a = body_dict['map']
    return count_islands(a, x, y)


if __name__ == '__main__':
    app.run(host=host, port=port)
