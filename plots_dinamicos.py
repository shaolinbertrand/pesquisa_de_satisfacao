import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,6)

plt.style.use('ggplot')

plt.ion() #ligando o modo dinamico
for i in range(10):
    dados = np.random.randint(20,300,5)
    plt.cla()
    plt.clf()
    plt.bar(x,dados)
    plt.pause(3)

plt.ioff() #desligando o modo dinamico