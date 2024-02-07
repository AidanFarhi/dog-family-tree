from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update():
    print(request.get_json())
    return {'msg': 'hello'}

@app.route('/')
def hello():
    return render_template('index.html')
