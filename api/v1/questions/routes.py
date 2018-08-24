from flask import Flask,jsonify
from flask_restful import Resource, Api,abort

app = Flask(__name__)
api = Api(app)

#questions held in a dictionary
posts = [
	{
	  'question_id':101,
	  'user_id':300,
	  'questions':'What is REST?'
	},
	{
	  'question_id':102,
	  'user_id':301,
	  'questions':'What is Api?'
	},
	{
	  'question_id':103,
	  'user_id':302,
	  'questions':'What RESTful Api?'
	},
	{
	  'question_id':104,
	  'user_id':303,
	  'questions':'What are the commonly used webservices?'
	}
]

#Get all questions
@app.route('/api/v1/questions', methods = ['GET'])
def get_questions():
	#return all questions
	return jsonify({'questions':posts})

#Get a question
@app.route('/api/v1/questions/<int:question_id>', methods = ['GET'])
def get_question(question_id):
	#return a question
	return jsonify({'questions':posts[question_id]})

if __name__ == "__main__":
	app.run(debug=True)
