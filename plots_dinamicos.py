import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,6)
dados = np.random.randint(20,30,5)

plt.bar(x,dados)
plt.show()