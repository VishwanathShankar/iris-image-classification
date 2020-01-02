# make predictions
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import pickle
import numpy as np

# Load dataset
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv("iris.csv", names=names)
# Split-out validation dataset

array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)
# Make predictions on validation dataset
print("X validation is")
print(X_validation)
print("Y validation is")
print(Y_validation)
model = SVC(gamma='auto')
model.fit(X_train, Y_train)

test_data = np.array([4.6, 3.1, 1.5, 0.2])
test_data = test_data.reshape(1,4)
print("Test data is")
print(test_data)
#predictions = model.predict(X_validation)
predictions = model.predict(test_data)
# Evaluate predictions
#print(accuracy_score(Y_validation, predictions))

print("Preictions are")
print(predictions)

print("X_validation tyoe")
print(type(X_validation))

# filename = 'finalized_model.sav'
# pickle.dump(model, open(filename, 'wb'))

# loaded_model = pickle.load(open(filename, 'rb'))
# result = loaded_model.score(X_validation, Y_validation)
# print(result)
