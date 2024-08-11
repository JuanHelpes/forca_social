# Abra o arquivo em modo de leitura
arquivo = open("/home/juan/Área de Trabalho/TCC/forca_social/PySocialForce/construtor mapas/construtor mapas/map.txt", "r")

# Leia todas as linhas do arquivo
todas_linhas = arquivo.readlines()

num_linhas = len(todas_linhas) -1


# Divida a linha nos espaços para obter uma lista de elementos
num_colunas = len(todas_linhas[0]) -1

# Obtenha o número de elementos

print("Número de linhas:", num_linhas)
print("Número de colunas:", num_colunas)

# Inicialize a lista de linhas
lista_de_linhas = []

# linha horizontais
for linha in range(num_linhas):
    for coluna in range(num_colunas):
        # print (coluna)
        if todas_linhas[linha][coluna] == "1":
            if coluna + 1 < num_colunas: 
                if todas_linhas[linha][coluna + 1] == "1":
                    xIni = coluna
                    yIni = linha
                    yFim = linha
                    coluna += 1
                    while todas_linhas[linha][coluna] == "1":
                        xFim = coluna
                        coluna += 1
                coluna = xIni
                lista_de_linhas.append([xIni, xFim, yIni, yFim])

# linha verticais
for coluna in range(num_colunas):
    for linha in range(num_linhas):
        if todas_linhas[linha][coluna] == "1":
            if linha + 1 < num_linhas:
                if todas_linhas[linha + 1][coluna] == "1":
                    xIni = coluna
                    yIni = linha
                    xFim = coluna
                    linha += 1
                    while todas_linhas[linha][coluna] == "1":
                        yFim = linha
                        linha += 1
                linha = yIni
                lista_de_linhas.append([xIni, xFim, yIni, yFim]) 


divisor = 1
lista_de_linhas_dividida = [[elemento / divisor for elemento in linha] for linha in lista_de_linhas]

print(lista_de_linhas_dividida)
# Feche o arquivo
arquivo.close()
