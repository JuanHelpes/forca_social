import matplotlib.pyplot as plt
import collections
import collections

import matplotlib.pyplot as plt

class Estatistica:
    def __init__(self, file_path, total_peds, caminho_grafico, seed):
        self.file_path = file_path
        self.total_peds = total_peds
        self.caminho = caminho_grafico + '\\seed_' + str(seed)

    def plotar_grafico(self):
        # Ler o arquivo e extrair os dados
        with open(self.file_path, 'r') as file:
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
        # plt.show()
        plt.savefig(self.caminho + '\grafico_peds.png')

    def calcular_taxa_saida(self):
        # Ler o arquivo e contar o número de linhas
        with open(self.file_path, 'r') as file:
            num_linhas = sum(1 for line in file)

        # Calcular a taxa de saída em porcentagem
        taxa_saida = (num_linhas / self.total_peds) * 100

        # Salvar a taxa de saída no arquivo
        with open(self.file_path, 'a') as file:
            file.write(f'Taxa de saida: {taxa_saida:.2f}%\n')
    
# Exemplo de uso da classe
# estatisticas = Estatistica('D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa 1\passos_seed_10.txt', 150)
# estatisticas.calcular_taxa_saida()
# estatisticas.plotar_grafico()
