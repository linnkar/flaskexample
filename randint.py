from flask import Flask, render_template, request
import random
import json

category = [
   { 'category' : 'Operator', 'text' : 'Operaattori' },
   { 'category' : 'Payments', 'text' : 'Maksut'},
   { 'category' : 'Cat1', 'text' : 'Ryhma 1'},
   { 'category' : 'Cat2', 'text' : 'Ryhma 2'},
]

saved = [
   { 'category' : 'Payments', 'text' : 'Maksut'},
   { 'category' : 'Cat2', 'text' : 'Ryhma 2'},
]

app = Flask (__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def roll_dice():
	dice_roll = random.randint (1,6)
		
	return render_template ('randint.html', dice_roll=dice_roll, category=category, saved=saved)
	

@app.route('/', methods=['POST'])	
def dispute ():
	new_saved = request.form.getlist("dispute")
	print new_saved
	return json.dumps(new_saved)
	
	
if __name__ == '__main__' :
	app.run (debug=True)
	
	