from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import pickle
import numpy as np


number_string = '4.6, 3.1, 1.5, 0.2'
number_string = number_string.split(',')
number_string = [float(i) for i in number_string]
print(number_string)

filename = 'finalized_model.sav'
string_data = list(eval('4.6, 3.1, 1.5, 0.2'))

loaded_model = pickle.load(open(filename, 'rb'))
#test_data = np.array([4.6, 3.1, 1.5, 0.2])
test_data = np.array(number_string)
test_data = test_data.reshape(1,4)
print("Test data is")
print(test_data)
result = loaded_model.predict(test_data)
print(type(result[0]))
print(result[0])
