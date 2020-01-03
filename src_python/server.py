from flask import Flask, redirect, url_for, request, send_from_directory
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import pickle
import numpy as np

# the all-important app variable:
app = Flask(__name__)
responseObj = {
	"flower-type": "xyz"
}

@app.route("/classify")
def hello():
	#number_string = '4.6,3.1,1.5,0.2'
	number_string = request.args.get('dimensions')
	number_string = number_string.split(',')
	number_string = [float(i) for i in number_string]
	print(number_string)
	filename = 'finalized_model.sav'
	loaded_model = pickle.load(open(filename, 'rb'))
	#test_data = np.array([4.6, 3.1, 1.5, 0.2])
	test_data = np.array(number_string)
	test_data = test_data.reshape(1,4)
	print("Test data is")
	print(test_data)
	result = loaded_model.predict(test_data)
	print(result)
	responseObj["flower-type"] = result[0]
	return responseObj

@app.route('/app/<path:path>')
def send_js(path):
    return send_from_directory('build', path)

if __name__ == "__main__":
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(host='0.0.0.0', debug=True, port=8081)