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

#ノイズを生成して半分に
noise_raw = np.random.normal(loc=0.0, scale=np.sqrt(2.0), size=n_samples)
noise = noise_raw / 2

#ノイズを付与
df['観測値'] = df['真値'] + noise

print(df.head())


plt.figure(figsize=(8, 5))

x_line = np.linspace(-1, 1, 100)
plt.plot(x_line, true_function(x_line), label='True function', color='blue', alpha=0.5)
plt.scatter(df['観測点'], df['真値'], color='red', label='True samples (Ex 1.2)', s=30, alpha=0.5)
plt.scatter(df['観測点'], df['観測値'], color='green', marker='x', label='Observed samples (With noise)', s=50)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exercise 1.3: Adding Noise to Samples')
plt.legend()
plt.grid(True)

# 保存
plt.savefig('ex1.3.png')
plt.show()

# --- 演習1.4 ---

df.to_csv('dataset.tsv', sep='\t', index=False)

print("TSV形式で出力保存")