from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from llm_integration import get_llm_response

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def query():
    data = request.json
    user_input = data.get('input', '')
    response = get_llm_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
