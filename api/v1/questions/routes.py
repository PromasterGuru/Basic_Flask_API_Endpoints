from flask import Flask, jsonify, request
from flask_restful import Resource, Api,abort

app = Flask(__name__)
api = Api(app)

#Questions held in a dictionary
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

#Qnswers held in a dictionary
answers = []

#Get all questions
@app.route('/questions', methods = ['GET'])
def get_questions():
	#return all questions
	return jsonify({'questions':posts}),200 #Success/Ok

#Get a question
@app.route('/questions/<int:questionId>', methods = ['GET'])
def get_question(questionId):
	post = [post for post in posts if post['question_id'] == questionId]
	if len(post) == 0:
		abort(404) #Not found
	#return a question
	return jsonify({'questions':post[0]}),200 #Success/Ok

#Post a question
@app.route('/questions', methods = ['POST'])
def post_question():
	if not request.json or not 'user_id' in request.json:
		abort(400) #Bad request
	question = {
		'question_id':request.json['questionId'],
		'user_id':request.json['user_id'],
		'questions':request.json.get('questions',"")
	}
	posts.append(question)
	#return all questions
	return jsonify({'questions':posts}),201 #created

#Post an answer to a question
@app.route('/questions/<int:questionId>/answers', methods = ['POST'])
def post_answer(questionId):
	if not request.json or not 'answers' in request.json:
		abort(400) #Bad request'''
	post = [post for post in posts if post['question_id'] == questionId]
	if len(post) == 0:
		abort(404) #Not found
	else:
		answer = {
			'question_id':questionId,
			'answer':request.json.get('answers',"")
			}
	answers.append(answer)
	return jsonify({"Answers":answers})
		
if __name__ == "__main__":
	app.run(debug=True)
