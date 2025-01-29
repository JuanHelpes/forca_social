import numpy as np

# mapa cinema
# caminho relativo do arquivo do mapa sem alterações
arquivo_mapa = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_3\cinema.txt"
# caminho relativo do arquivo do mapa com alterações
# arquivo_mapa_alterado = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_3\cinema_comodos.txt"
arquivo_mapa_alterado = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_3\cinema_comodos.txt"
# caminho relativo do arquivo do mapa estatico
arquivo_mapa_static = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_3\static_mapa_cinema.txt"
# caminho relativo do arquivo de passos
arquivoPassos = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_3"

# configurações da simulação
# quantidade de pedestres
qtd_pedestres = 140
# valor para saida do comodo
saida_comodo = 1
# valor do vazio
vazio = 100


# limite de intervalo de X
xlim = [-1, 55]
# limite de intervalo de Y
ylim = [-1, 30]
# escala de X
xticks = np.arange(0, 55, 5)
# escala de Y
yticks = np.arange(0, 30, 5)
# numero de passos
n_passos = 420
# caminho de salvamento do arquivo
caminho = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_3"


