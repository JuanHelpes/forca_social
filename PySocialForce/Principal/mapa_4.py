import numpy as np

# mapa da igreja
# caminho relativo do arquivo do mapa sem alterações
arquivo_mapa = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_4\igreja.map"
# caminho relativo do arquivo do mapa com alterações
arquivo_mapa_alterado = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_4\igreja_comodos.map"
# caminho relativo do arquivo do mapa estatico
arquivo_mapa_static = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_4\static_mapa_igreja.txt"
# caminho relativo do arquivo de passos
arquivoPassos = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_4"

# configurações da simulação
# quantidade de pedestres
qtd_pedestres = 172
# valor para saida do comodo
saida_comodo = 1
# valor do vazio
vazio = 100


# limite de intervalo de X
xlim = [-1, 115]
# limite de intervalo de Y
ylim = [-1, 45]
# escala de X
xticks = np.arange(0, 115, 5)
# escala de Y
yticks = np.arange(0, 45, 5)
# numero de passos
n_passos = 200
# caminho de salvamento do arquivo
caminho = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_4"