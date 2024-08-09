from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["100 per day", "10 per hour"]
)

# Example route that is rate-limited
@app.route('/test', methods=['GET'])
@limiter.limit("5 per minute")
def test_route():
    return jsonify({'message': 'You have access!'})

if __name__ == '__main__':
    app.run(debug=True)
