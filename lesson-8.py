from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


iris = load_iris()
x, y = iris.data, iris.target

np.random.seed(42)
np.random.rand(3, 3)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)


model = GaussianNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print(f"accuracy {accuracy_score(y_test, y_pred):.2%}")

new_flower = [[7, 2.7, 0.8, 1.7]]
pred = model.predict(new_flower)
print(f"bashorat {iris.target_names[[pred[0]]]}")