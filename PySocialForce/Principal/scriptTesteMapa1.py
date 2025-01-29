import subprocess
import time

# Número de vezes que você quer executar o comando
n = 100
inicio = time.time()

# Loop para variar o valor de X de 1 a n
for x in range(1, n + 1):
    comando = f'python main.py mapa_1 {x}'
    print(f"Executando: {comando}")
    subprocess.run(comando, shell=True)


fim = time.time()

# Calcula o tempo de execução
tempo_execucao = fim - inicio

# Salva os resultados em um arquivo
with open("D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\execucaoTotalMapa1.txt", "w") as arquivo_saida:
    arquivo_saida.write(f"Tempo total de execucao: {tempo_execucao:.2f}\n")