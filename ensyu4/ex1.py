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

# 1. ノイズの生成
# 平均0.0, 分散2.0 の正規分布。np.random.normal の scale は標準偏差なので sqrt(2.0)
noise_raw = np.random.normal(loc=0.0, scale=np.sqrt(2.0), size=n_samples)

# 2. ノイズをさらに半分にする
noise = noise_raw / 2

# 3. 真値にノイズを付与して「観測値」とする
df['観測値'] = df['真値'] + noise

# 4. 内容確認
print(df.head())

# 5. グラフの描画
plt.figure(figsize=(8, 5))

# 線グラフ（真の関数）
x_line = np.linspace(-1, 1, 100)
plt.plot(x_line, true_function(x_line), label='True function', color='blue', alpha=0.5)

# 演習1.2のプロット（真値：赤い点）
plt.scatter(df['観測点'], df['真値'], color='red', label='True samples (Ex 1.2)', s=30, alpha=0.5)

# 演習1.3のプロット（観測値：緑の×印など、見分けやすく）
plt.scatter(df['観測点'], df['観測値'], color='green', marker='x', label='Observed samples (With noise)', s=50)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Exercise 1.3: Adding Noise to Samples')
plt.legend()
plt.grid(True)

# 保存
plt.savefig('ex1.3.png')
plt.show()