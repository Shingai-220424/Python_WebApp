from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from test_model import Person
from test_model import Human

app = Flask(__name__)
# Pythonを使用しての開発_Webアプリ2のpowerpointスライド26
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')

def inex():
    return 'Response Data'

@app.route('/another')
def another():
    return 'Another Response'

@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'
@app.route('/exercise_request/<test>')
def exercise_request(test):
    return f"request:{test}"

@app.route('/show_html')
def show_html():
    return render_template('test_html.html')

@app.route('/exercise')
def exercise():
    return render_template('exercise.html')

@app.route('/answer', methods=["GET", "POST"])
def amswer():
    name = request.args.get("my_name")
    return render_template('answer.html', name = name )

@app.route('/try_rest',  methods=["POST"])
def try_rest():
    # リクエストデータをJSONとして受け取る
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json":request_json}
    return jsonify(response_json)

# Pythonを使用しての開発_Webアプリ2のpowerpointスライド27
@app.route('/person_search')
def person_search():
    return render_template('./person_search.html')
@app.route('/person_result')
def person_result():
    search_size = request.args.get("search_size")
    persons = db.session.query(Person).filter(Person.size > search_size)
    return render_template('./person_result.html', persons=persons, search_size=search_size)
@app.route('/human-search')
def human_search():
    return render_template('./human_search.html')
@app.route('/human-result')
def human_result():
    search_height = request.args.get("search-height")
    search_weight = request.args.get("search-weight")
    humans = db.session.query(Human).filter(Human.height > search_height and Human.weight > search_weight)
    return render_template('./human_result.html', humans = humans, search_height=search_height, search_weight=search_weight)