import numpy as np

# mapa da igreja
# caminho relativo do arquivo do mapa sem alterações
arquivo_mapa = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_5\\nishihari.map"
# caminho relativo do arquivo do mapa com alterações
arquivo_mapa_alterado = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_5\\nishihari.map"
# caminho relativo do arquivo do mapa estatico
arquivo_mapa_static = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_5\static_mapa_nishihari.txt"
# caminho relativo do arquivo de passos
arquivoPassos = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_5"

# configurações da simulação
# quantidade de pedestres
qtd_pedestres = 300
# valor para saida do comodo
saida_comodo = 1
# valor do vazio
vazio = 100


# limite de intervalo de X
xlim = [-1, 100]
# limite de intervalo de Y
ylim = [-1, 100]
# escala de X
xticks = np.arange(0, 100, 5)
# escala de Y
yticks = np.arange(0, 100, 5)
# numero de passos
n_passos = 900
# caminho de salvamento do arquivo
caminho = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_5"