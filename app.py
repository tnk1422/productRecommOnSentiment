from flask import Flask
from flask import request
from flask import Flask, redirect, url_for, request, render_template,render_template_string


from model import *

app = Flask(__name__)

version=10

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.before_first_request
def before_first_request():
    init()
    yield "<html></head><body>Processing your Request</body></html>"

@app.route('/recommend', methods=['GET'])
def recommend():
	username = request.args.get('username')
	print(f"LOG: Input username is {username}")
	yield "<html></head><body>Processing your Request</body></html>"
	try:
		finalList=getFinalRecommendaions(username)
		tablehtml=pd.DataFrame.from_dict(finalList,orient='index').reset_index().rename(columns={"index": "productName", 0: "recommendationPercentage"}).to_html()
	except Exception as e:
		tablehtml="<p style=\"color:red\"> There is error while recommending product for user "+username+ " Error Message "+str(e)+ " Please try with valid user</p>"

	htmlPage="<!doctype html>	<html> <head> <title>Recommending Top 5 products for User "+username+" </title>"+"<link href=\"static/style.css\" rel=\"stylesheet\">"
	htmlPage=htmlPage+"<body> <h2>Recommending Top 5 products for User "+username+" </h2></body>"+tablehtml+"</html>"
	return htmlPage
	

if __name__ == "__main__":
    app.run()
