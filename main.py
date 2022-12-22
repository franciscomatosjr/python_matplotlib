import matplotlib.pyplot as plt

x = [2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035]

convencional = [95.09, 129.34, 140.08, 142.04, 142.34, 142.44, 140.05, 136.82, 134.12, 131.26, 127.76, 123.15]
valor_minimo = min(convencional)
valor_maximo = max(convencional)

incentivada = [123.68, 158.80, 169.29, 170.93, 170.91, 169.82, 167.11, 163.01, 160.11, 155.76, 151.56, 146.76]

if valor_maximo < max(incentivada):
    valor_maximo = max(incentivada)

valor_maximo += 60

if valor_minimo > min(incentivada):
    valor_minimo = min(incentivada)

valor_minimo -= 30

plt.plot(x, convencional, label='FONTE CONVENCIONAL SE/CO',
         linewidth=4,
         markersize=10,
         color='cornflowerblue',
         marker='o',
         markerfacecolor='snow',
         markerfacecoloralt='lightsteelblue',
         markeredgecolor='cornflowerblue'
         )
plt.plot(x, incentivada, label='FONTE INCENTIVADA 50% SE/CO',
         linewidth=4,
         markersize=10,
         color='gray',
         marker='o',
         markerfacecolor='snow',
         markerfacecoloralt='lightsteelblue',
         markeredgecolor='gray')

plt.rcParams['figure.figsize'] = (20, 10)
plt.rcParams["figure.autolayout"] = True

# plt.xlabel('Anos projeção')
plt.ylabel('Preços (R$/MWh)')

plt.title("Preços na apuração mensal de Novembro de 2022 de produtos de longuíssimo prazo", fontdict={'size': 16}, pad=20)

# loc=best o python coloca as legendas da melhor forma possível no gráfico
plt.legend(loc='best')
plt.grid(True)

for index in range(len(x)):
    # os parâmetros verticalalignment e horizontalalignment são responsável para que o valor não fique truncado na linha do gráfico
    plt.text(x[index], convencional[index]+2, str(convencional[index]).replace('.', ','), size=10, verticalalignment='bottom', horizontalalignment='right')
    plt.text(x[index], incentivada[index]+2, str(incentivada[index]).replace('.', ','), size=10, verticalalignment='bottom', horizontalalignment='right')

# Exibir os labels do eixo x e y
plt.xticks(x, size=10)

# No eixo y é colocada um valor descrescido do valor mínimo encontrado nas duas linhas do gráfico e da mesma forma é feita no valor máximo, fazendo isso o gráfico fica mais uniforme
plt.yticks([i for i in range(int(valor_minimo), int(valor_maximo), 30)], size=10)

# plt.savefig('nome_da_imagem.png'`, transparent = True)

plt.show()
