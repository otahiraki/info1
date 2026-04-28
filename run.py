import datasets
import regression
import importlib

importlib.reload(regression)

X, Y = datasets.load_linear_example1()

model = regression.LinearRegression()

# fit
model.fit(X, Y)
print("theta:", model.theta)

# predict
print("predict:", model.predict(X))

# score
print("score:", model.score(X, Y))