import numpy as np

# caminho relativo do arquivo do mapa sem alterações
arquivo_mapa = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_1\map_padrao.txt"
# caminho relativo do arquivo do mapa com alterações
arquivo_mapa_alterado = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_1\map_comodos.txt"
# caminho relativo do arquivo do mapa estatico
arquivo_mapa_static = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_1\static_map.txt"
# caminho relativo do arquivo de passos
arquivoPassos = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_1"
# quantidade de pedestres ambiente de culto
qtd_pedestres = 145

# quantidade de pedestres ambiente de formatura
# qtd_pedestres = 320


# valor para saida do comodo
saida_comodo = 1
# valor do vazio
vazio = 50

# configurações da simulação
# limite de intervalo de X
xlim = [-1, 90]
# limite de intervalo de Y
ylim = [-1, 77]
# escala de X
xticks = np.arange(0, 90, 5)
# escala de Y
yticks = np.arange(0, 80, 5)
# numero de passos
n_passos = 180
# caminho de salvamento do arquivo
caminho = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_1"