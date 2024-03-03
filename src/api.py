from flask import Flask, request, jsonify
from chess_converter import san_to_lan

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    if 'pgn' not in data:
        return jsonify({'error': 'No PGN data provided'}), 400
    pgn = data['pgn']
    lan = san_to_lan(pgn)
    return jsonify({'lan': lan})

@app.route('/santolan/<path:pgn>', methods=['GET'])
def convert_get(pgn):
    san_moves = pgn.split(',')
    result = san_to_lan(san_moves)
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 400
    return jsonify({'lan': result})

if __name__ == '__main__':
    app.run(debug=True)
