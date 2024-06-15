from flask import Flask, request

app = Flask(__name__)
@app.route('/')

def inex():
    return 'Response Data'

@app.route('/another')
def another():
    return 'Another Response'

@app.route('/test_request/<test>')
def test_request(test):
    return f'test_request:{request.args.get("dummy")}'