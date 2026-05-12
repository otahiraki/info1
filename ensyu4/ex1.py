import numpy as np
import matplotlib.pyplot as plt

def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

def test_true_function():
    assert true_function(0) == 0 #テスト
    print("Test Passed: true_function(0) is 0")

if __name__ == "__main__":
    test_true_function()

    x = np.linspace(-1, 1, 100) 
    y = true_function(x)
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='True function $y = 10 \sin(0.8 \pi x)$')
    
    # グラフの設定
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Exercise 1.1: True Function')
    plt.legend()
    plt.grid(True)

    plt.savefig('ex1.1.png')
    print("Graph saved as ex1.1.png")
    plt.show()