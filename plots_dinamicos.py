from turtle import color
import numpy as np
import matplotlib.pyplot as plt

#x = np.arange(1,6)
x = ['Recomenda','Não \nRecomenda','Compra \nNovamente','Não Compra \nNovamente']
plt.style.use('ggplot')

plt.ion() #ligando o modo dinamico
for i in range(5):
    dados = np.random.randint(20,300,4) #intervalo de numeros gerados e quantidade de barras (deve coincidir com a quantidade de elementos 'x')
    plt.cla()
    plt.clf()
    plt.bar(x,dados,color='red')
    plt.xlabel('O que foi avaliado')
    plt.ylabel('Quantidade de Pessoas Avaliadas')
    plt.title('Pesquisa de satisfação')
    plt.pause(1)

plt.ioff() #desligando o modo dinamico
plt.show()