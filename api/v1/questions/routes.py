from flask import Flask, jsonify, request
from flask_restful import Resource, Api,abort

app = Flask(__name__)
api = Api(app)
#Users
users = [
	{
	  'user_id': 1001,
	  'username':'promaster',
	  'password': 'promaster2018'
	},
	{
	  'user_id': 1002,
	  'username':'paul',
	  'password': 'paul2018'
	},
	{
	  'user_id': 1003,
	  'username':'James',
	  'password': 'james2018'
	},
	{
	  'user_id': 1004,
	  'username':'daniel',
	  'password': 'daniel2018'
	}
]
#Questions
posts = [
	{
	  'question_id':101,
	  'user_id':users[0]['user_id'],
	  'questions':'What is REST?'
	},
	{
	  'question_id':102,
	  'user_id':users[1]['user_id'],
	  'questions':'What is Api?'
	},
	{
	  'question_id':103,
	  'user_id':users[2]['user_id'],
	  'questions':'What RESTful Api?'
	},
	{
	  'question_id':104,
	  'user_id':users[2]['user_id'],
	  'questions':'What are the commonly used webservices?'
	}
]

#Qnswers
answers = [
	{
	  'question_id': posts[0]['question_id'],
	  'user_id': users[0]['user_id'],
	  'answer_id': 200,
	  'answer':"REpresentational State Transfer",
	  'complete':False
	}
]

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
		abort(400) #Bad request
	post = [post for post in posts if post['question_id'] == questionId]
	if len(post) == 0:
		abort(404) #Not found
	else:
		answer = {
			'question_id':questionId,
			'user_id':request.json.get("userId"),
			'answer_id':request.json.get("answerId"),
			'answer':request.json.get('answers',""),
			'complete':False
			}
	answers.append(answer)
	return jsonify({"Answers":answers}),200 #OK
		
#Delete a question
@app.route('/questions/<int:questionId>', methods = ['DELETE'])
def delete_question(questionId):
	post = [post for post in posts if post['question_id'] == questionId]
	if len(post) == 0:
		abort(404) #Not found
	posts.remove(post[0])
	return jsonify({'Questions': posts}),200 #OK

#Mark answer as complet or update the answer
@app.route('/questions/<int:questionId>/answers/<int:answerId>',methods = ['PUT'])
def update_question(questionId,answerId):
	if not request.json or not 'answers' in request.json:
		abort(400) #Bad request
	answer = [answer for answer in answers if (answer['question_id'] == questionId and answer['answer_id'] == answerId)]
	if len(answer) == 0:
		abort(404) #Not found
	pos = answers.index(answer[0])
	answers[pos]['answer'] = request.json.get('answers')
	return jsonify({"Answers": answers}),200 #OK

if __name__ == "__main__":
	app.run(debug=True)
