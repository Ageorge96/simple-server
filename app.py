from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def get_index():
    return "<a href=\"/response\">Hello, world!</a>"

@app.route('/response')
def get_response():
    return "Hey, Andre!"



if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0')