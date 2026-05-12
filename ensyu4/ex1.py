import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

np.random.seed(0)
n_samples = 20

x_observed = np.random.uniform(-1, 1, n_samples)
y_true = true_function(x_observed)

df = pd.DataFrame({
    '観測点': x_observed,
    '真値': y_true
})

print(df.head())

plt.figure(figsize=(8, 5))

x_line = np.linspace(-1, 1, 100)
plt.plot(x_line, true_function(x_line), label='True function', zorder=1)

plt.scatter(df['観測点'], df['真値'], color='red', label='Samples', s=30, zorder=2)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Exercise 1.2: Observed points and True values')
plt.legend()
plt.grid(True)

# 保存
plt.savefig('ex1.2.png')
plt.show()