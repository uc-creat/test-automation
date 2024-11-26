from findDuplicate import duplicateOne,duplicateTwo
from flask import Flask


from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')


@app.route('/read-form', methods=['POST'])
def read_form():
	data = request.form
	finalScore = duplicateTwo(data)
	return str(finalScore)


