import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2])
y = np.array([99,86,87,88,111])
text = np.array(["A","B","C","D","E"])

plt.scatter(x, y)

for i in range(len(x)): 
    plt.annotate(text[i], (x[i], y[i] + 0.2)) 
   
plt.show()