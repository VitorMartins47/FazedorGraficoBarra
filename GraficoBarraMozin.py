import matplotlib.pyplot as plt

categorias = []
valores = []

n = int(input("Quandos valores você vai inserir ? "))



for i in range(n):
    categoria = str(input(f"Digite a categoria {i+1}: "))
    categorias.append(categoria)

for i in range(n):
    valor = int(input(f"Digite o valor {i+1}: "))
    valores.append(valor)
    
plt.bar(categorias, valores)
plt.show()