# Flask LLM Web Application

This project is a Flask-based web application that allows users to input queries via a landing page, which are then sent to a locally running language model (LLM) using the `langchain-community` package. The response from the LLM is displayed asynchronously on the same page.

## Project Structure

```
llmFlask/
│
├── app.py
├── static/
│   └── js/
│       └── main.js
├── templates/
│   └── index.html
├── requirements.txt
└── llm_integration.py
```

- **app.py**: Main Flask application file.
- **static/js/main.js**: JavaScript file for handling asynchronous communication with the backend.
- **templates/index.html**: HTML template for the landing page.
- **requirements.txt**: Lists the dependencies for the project.
- **llm_integration.py**: Contains the logic to interact with the local LLM using `langchain-community`.

## Requirements

- Python 3.10 or higher
- pip

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/lordofthemind/llmFlask.git
   cd llmFlask
   ```

2. **Create a virtual environment and activate it**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask server**:

   ```bash
   python app.py
   ```

2. **Access the application**:

   Open a web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

1. **Landing Page**: The landing page contains an input field where users can type their queries and a submit button.

2. **Submit Query**: Users can type their questions and either press the "Submit" button or press "Enter" to submit the query.

3. **Display Response**: The response from the local LLM is displayed asynchronously below the input field.

## Code Explanation

### `app.py`

This is the main Flask application file. It defines the routes and handles the requests.

```python
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
```

### `llm_integration.py`

This file contains the logic to interact with the local LLM using `langchain-community`.

```python
from langchain_community.llms import Ollama

def get_llm_response(query):
    llm = Ollama(model="gemma:2b")
    response = llm.query(query)
    return response
```

### `templates/index.html`

This is the HTML template for the landing page.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LLM Flask App</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</head>
<body>
    <div>
        <h1>Ask the LLM</h1>
        <input type="text" id="userInput" placeholder="Type your question here...">
        <button id="submitButton">Submit</button>
    </div>
    <div>
        <h2>Response:</h2>
        <p id="responseText"></p>
    </div>
</body>
</html>
```

### `static/js/main.js`

This JavaScript file handles the asynchronous communication between the front-end and back-end.

```javascript
$(document).ready(function() {
    $('#submitButton').click(function() {
        var userInput = $('#userInput').val();
        $.ajax({
            url: '/api/query',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ input: userInput }),
            success: function(response) {
                $('#responseText').text(response.response);
            },
            error: function(error) {
                $('#responseText').text('Error: ' + error.responseText);
            }
        });
    });

    $('#userInput').keypress(function(e) {
        if (e.which == 13) {
            $('#submitButton').click();
        }
    });
});
```

### `requirements.txt`

Lists all the necessary Python packages needed for the project.

```
Flask==2.0.1
flask-cors==3.0.10
langchain-community==0.1.0
```

## Contributing

Feel free to fork this project, make modifications, and submit pull requests. Contributions are always welcome!

## License

This project is licensed under the MIT License.
```