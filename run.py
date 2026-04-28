import datasets
from regression import LinearRegression

X, Y = datasets.load_linear_example1()

model = LinearRegression()
model.fit(X, Y)

print("theta:", model.theta)