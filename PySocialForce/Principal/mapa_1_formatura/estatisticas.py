import matplotlib.pyplot as plt
import collections

# Ler o arquivo e extrair os dados
with open('D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa 1\passos.txt', 'r') as file:
    data = file.readlines()

# Processar os dados
tempo_chegada = []
for line in data:
    parts = line.strip().split('; ')
    tempo = int(parts[1].split(': ')[1])
    tempo_chegada.append(tempo)

# Contar a quantidade de pedestres para cada tempo de chegada
contador = collections.Counter(tempo_chegada)
tempos = sorted(contador.keys())
quantidade_pedestres = [contador[tempo] for tempo in tempos]

# Criar a lista cumulativa de pedestres
quantidade_cumulativa = []
total_pedestres = 0
for quantidade in quantidade_pedestres:
    total_pedestres += quantidade
    quantidade_cumulativa.append(total_pedestres)

# Criar o gráfico cumulativo
plt.figure(figsize=(10, 6))
plt.step(tempos, quantidade_cumulativa, where='post')
plt.xlabel('Tempo em iterações')
plt.ylabel('Quantidade Cumulativa de Pedestres')
plt.title('Quantidade Cumulativa de Pedestres x Tempo de Chegada')
plt.grid(True)
plt.show()
