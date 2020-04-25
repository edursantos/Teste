import matplotlib.pyplot as plt
x1 = [0, 2, 4, 6, 8]
y1 = [1, 3, 5, 7, 9]

x2 = [1, 3, 5, 7, 9]
y2 = [2, 4, 7, 6, 8]

titulo = 'Gráfico de barras'
eixox = 'Eixo X'
eixoy = 'Eixo Y'
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.bar(x1, y1, label ='Grupo 1')
plt.bar(x2,y2, label ='Grupo 2')
plt.legend()
plt.show()

