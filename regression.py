import numpy as np

class LinearRegression:
    def __init__(self):
        self.x = None
        self.y = None
        self.theta = None

    # 学習
    def fit(self, x, y):
        self.x = x
        self.y = y
        temp = np.linalg.inv(np.dot(x.T, x))
        self.theta = np.dot(np.dot(temp, x.T), y)

    # 予測
    def predict(self, x):
        return np.dot(x, self.theta)

    # 誤差（残差平方和）
    def score(self, x, y):
        error = self.predict(x) - y
        return (error ** 2).sum()