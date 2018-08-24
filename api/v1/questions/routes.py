from flask import Flask,jsonify

app = Flask(__name__)

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

@app.route('/api/v1/questions', methods = ['GET'])
def questions():
	#return all questions
	return jsonify({'questions':posts})

if __name__ == "__main__":
	app.run(debug=True)
