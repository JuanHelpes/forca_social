import os
import statistics
import matplotlib.pyplot as plt

# Diretório principal onde estão as pastas "seed_X"
diretorio_principal = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_4"

# Listas para armazenar os valores extraídos
tempos_execucao = []
passos_finais = []
taxas_saida = []

# Itera por cada pasta "seed_X" dentro de "mapa_4"
for pasta_seed in os.listdir(diretorio_principal):
    caminho_pasta_seed = os.path.join(diretorio_principal, pasta_seed)
    
    # Confirma que é uma pasta "seed_X"
    if os.path.isdir(caminho_pasta_seed) and pasta_seed.startswith("seed_"):
        
        # Lê o arquivo tempoExecucao.txt para coletar o tempo de execução
        caminho_tempo = os.path.join(caminho_pasta_seed, "tempoExecucao.txt")
        if os.path.exists(caminho_tempo):
            with open(caminho_tempo, "r") as arquivo:
                tempo = float(arquivo.read().strip())
                tempos_execucao.append(tempo)
        
        # Lê o arquivo passos_seed_X.txt para coletar o passo final e a taxa de saída
        caminho_passos = os.path.join(caminho_pasta_seed, f"passos_{pasta_seed}.txt")
        if os.path.exists(caminho_passos):
            with open(caminho_passos, "r") as arquivo:
                linhas = arquivo.readlines()
                
                # Extrai o último passo (última linha com "passo: <valor>")
                ultima_linha = linhas[-2]
                ultimo_passo = int(ultima_linha.split(":")[-1].strip())
                passos_finais.append(ultimo_passo)
                
                # Extrai a taxa de saída (última linha com "Taxa de saída: <valor>%")
                taxa_saida = float(linhas[-1].split(":")[-1].strip().replace("%", ""))
                taxas_saida.append(taxa_saida)

# Cálculo das estatísticas
media_tempo_execucao = statistics.mean(tempos_execucao)
media_taxa_saida = statistics.mean(taxas_saida)
media_passos = statistics.mean(passos_finais)
mediana_passos = statistics.median(passos_finais)
min_passos = min(passos_finais)
max_passos = max(passos_finais)
variancia_passos = statistics.variance(passos_finais)
desvio_padrao_passos = statistics.stdev(passos_finais)

# Estatísticas adicionais para tempo de execução
variancia_tempo_execucao = statistics.variance(tempos_execucao)
desvio_padrao_tempo_execucao = statistics.stdev(tempos_execucao)
mediana_tempo_execucao = statistics.median(tempos_execucao)
min_tempo_execucao = min(tempos_execucao)
max_tempo_execucao = max(tempos_execucao)

# Estatísticas adicionais para taxa de saída
variancia_taxa_saida = statistics.variance(taxas_saida)
desvio_padrao_taxa_saida = statistics.stdev(taxas_saida)
mediana_taxa_saida = statistics.median(taxas_saida)
min_taxa_saida = min(taxas_saida)
max_taxa_saida = max(taxas_saida)

# Diretório para salvar os resultados
diretorio_saida = diretorio_principal
caminho_arquivo_estatisticas = os.path.join(diretorio_saida, "estatisticas_resultados.txt")

# Salva os resultados em um arquivo
with open("D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_4\estatisticas_resultados.txt", "w") as arquivo_saida:
    arquivo_saida.write(f"Media do tempo de execucao: {media_tempo_execucao:.2f} segundos\n")
    arquivo_saida.write(f"Variancia do tempo de execucao: {variancia_tempo_execucao:.2f}\n")
    arquivo_saida.write(f"Desvio padrao do tempo de execucao: {desvio_padrao_tempo_execucao:.2f}\n")
    arquivo_saida.write(f"Mediana do tempo de execucao: {mediana_tempo_execucao:.2f}\n")
    arquivo_saida.write(f"Minimo do tempo de execucao: {min_tempo_execucao:.2f}\n")
    arquivo_saida.write(f"Maximo do tempo de execucao: {max_tempo_execucao:.2f}\n\n")
    
    arquivo_saida.write(f"Media da taxa de saida: {media_taxa_saida:.2f}%\n")
    arquivo_saida.write(f"Variancia da taxa de saida: {variancia_taxa_saida:.2f}\n")
    arquivo_saida.write(f"Desvio padrao da taxa de saida: {desvio_padrao_taxa_saida:.2f}\n")
    arquivo_saida.write(f"Mediana da taxa de saida: {mediana_taxa_saida:.2f}\n")
    arquivo_saida.write(f"Minimo da taxa de saida: {min_taxa_saida:.2f}%\n")
    arquivo_saida.write(f"Maximo da taxa de saida: {max_taxa_saida:.2f}%\n\n")
    
    arquivo_saida.write(f"Media dos passos finais: {media_passos:.2f}\n")
    arquivo_saida.write(f"Mediana dos passos finais: {mediana_passos:.2f}\n")
    arquivo_saida.write(f"Minimo dos passos finais: {min_passos}\n")
    arquivo_saida.write(f"Maximo dos passos finais: {max_passos}\n")
    arquivo_saida.write(f"Variancia dos passos finais: {variancia_passos:.2f}\n")
    arquivo_saida.write(f"Desvio padrao dos passos finais: {desvio_padrao_passos:.2f}\n")

# Gera e salva os gráficos boxplot
plt.figure(figsize=(10, 6))

# Boxplot para tempos de execução
plt.boxplot(tempos_execucao, vert=True, patch_artist=True, labels=["Tempo de Execução"])
plt.title("Boxplot do Tempo de Execução")
plt.ylabel("Tempo (s)")
caminho_boxplot_tempo = os.path.join(diretorio_saida, "boxplot_tempo_execucao.png")
plt.savefig(caminho_boxplot_tempo)
plt.close()

# Boxplot para passos finais
plt.figure(figsize=(10, 6))
plt.boxplot(passos_finais, vert=True, patch_artist=True, labels=["Passos Finais"])
plt.title("Boxplot dos Passos Finais")
plt.ylabel("Número de Passos")
caminho_boxplot_passos = os.path.join(diretorio_saida, "boxplot_passos_finais.png")
plt.savefig(caminho_boxplot_passos)
plt.close()

print(f"Estatísticas calculadas e salvas em '{caminho_arquivo_estatisticas}'")
print(f"Gráficos boxplot salvos em '{caminho_boxplot_tempo}' e '{caminho_boxplot_passos}'")
