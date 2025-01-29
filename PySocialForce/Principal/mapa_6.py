import numpy as np

# caminho relativo do arquivo do mapa sem alterações
arquivo_mapa = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_6\mapa_exemplo.txt"
# caminho relativo do arquivo do mapa com alterações
arquivo_mapa_alterado = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_6\mapa_exemplo_comodos.txt"
# caminho relativo do arquivo do mapa estatico
arquivo_mapa_static = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_6\static_mapa_exemplo.txt"
# caminho relativo do arquivo de passos
arquivoPassos = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_6"
# quantidade de pedestres ambiente de culto
qtd_pedestres = 50

# quantidade de pedestres ambiente de formatura
# qtd_pedestres = 320


# valor para saida do comodo
saida_comodo = 1
# valor do vazio
vazio = 30

# configurações da simulação
# limite de intervalo de X
xlim = [-1, 22]
# limite de intervalo de Y
ylim = [-1, 22]
# escala de X
xticks = np.arange(0, 22, 5)
# escala de Y
yticks = np.arange(0, 22, 5)
# numero de passos
n_passos = 200
# caminho de salvamento do arquivo
caminho = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_6"