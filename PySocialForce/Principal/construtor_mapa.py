import random
import numpy as np
import json


# Abra o arquivo em modo de leitura
arquivo = open(r"D:\Faculdade\TCC\Codigo\TCC\PySocialForce\construtor mapas\map.txt", "r")
# arquivo_mapa_estatico = open(r"D:\Faculdade\TCC\Codigo\TCC\PySocialForce\mapa script\unified\static.txt", "r")


# Abra o arquivo e leia o conteúdo
with open(r"D:\Faculdade\TCC\Codigo\TCC\PySocialForce\mapa script\unified\static.txt", 'r') as f:
    content = f.read()

# Remova a última vírgula para tornar o conteúdo um JSON válido
if content.endswith(','):
    content = content[:-1]

# Use json.loads para transformar a string em uma matriz
matriz_estatica = json.loads(content)

# print(matriz_estatica[0][0])

# Leia todas as linhas do arquivo
todas_linhas = arquivo.readlines()
# todas_linhas_estatica = arquivo_mapa_estatico.readlines()
matriz = [list(map(int, linha.strip())) for linha in todas_linhas]
# matriz_estatica = [list(map(int, linha.strip())) for linha in todas_linhas_estatica]
num_linhas = len(todas_linhas) -1


# Divida a linha nos espaços para obter uma lista de elementos
num_colunas = len(todas_linhas[0]) -1

# Obtenha o número de elementos

print("Número de linhas:", num_linhas)
print("Número de colunas:", num_colunas)

# Inicialize a lista de linhas
lista_de_linhas = []

def constroiMapa ():
    linha = 0
    coluna = 0
    # linha horizontais
    while linha < num_linhas:
        coluna = 0
        while coluna < num_colunas:
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
                        coluna = xFim
                        lista_de_linhas.append([xIni, xFim, yIni, yFim])
            coluna += 1
        linha += 1

    # linha verticais
    linha = 0
    coluna = 0
    while coluna <= num_colunas:
        linha = 0
        while linha < num_linhas:
            if todas_linhas[linha][coluna] == "1":
                if linha + 1 < num_linhas: 
                    if todas_linhas[linha +1][coluna] == "1":
                        xIni = coluna
                        xFim = coluna
                        yIni = linha
                        linha += 1
                        while todas_linhas[linha][coluna] == "1":
                            yFim = linha
                            linha += 1
                        linha = yFim
                        lista_de_linhas.append([xIni, xFim, yIni, yFim])
            linha += 1
        coluna += 1
    return lista_de_linhas
   
def posPortas ():
    linha = 0
    coluna = 0
    lista_portas_horizontais = []
    lista_portas_verticais = []
    # linha horizontais
    while linha < num_linhas:
        coluna = 0
        while coluna < num_colunas:
            if todas_linhas[linha][coluna] == "2":
                if coluna + 1 < num_colunas: 
                    if todas_linhas[linha][coluna + 1] == "2":
                        xIni = coluna
                        yIni = linha
                        yFim = linha
                        coluna += 1
                        while todas_linhas[linha][coluna] == "2":
                            xFim = coluna
                            coluna += 1
                        coluna = xFim
                        lista_portas_horizontais.append([xIni, xFim, yIni, yFim])
            coluna += 1
        linha += 1

    # linha verticais
    linha = 0
    coluna = 0
    while coluna <= num_colunas:
        linha = 0
        while linha < num_linhas:
            if todas_linhas[linha][coluna] == "2":
                if linha + 1 < num_linhas: 
                    if todas_linhas[linha +1][coluna] == "2":
                        xIni = coluna
                        xFim = coluna
                        yIni = linha
                        linha += 1
                        while todas_linhas[linha][coluna] == "2":
                            yFim = linha
                            linha += 1
                        linha = yFim
                        lista_portas_verticais.append([xIni, xFim, yIni, yFim])
            linha += 1
        coluna += 1

    pos_portas = []
    for sublista in lista_portas_horizontais:
        x = (sublista[0] + sublista[1]) / 2
        y = (sublista[2] + sublista[3]) / 2
        if y > 10:
            y = y +1
        else:
            y = y -1
        pos_portas += [[x, y]]
    
    for sublista in lista_portas_verticais:
        x = (sublista[0] + sublista[1]) / 2
        y = (sublista[2] + sublista[3]) / 2
        if x > 40:
            x = x +1
        else:
            x = x -1
        pos_portas += [[x, y]]

    # print("Posição das portas externas:", pos_portas)

    return pos_portas

def posPortasInternas ():
    linha = 0
    coluna = 0
    lista_portas_horizontais = []
    lista_portas_verticais = []
    # linha horizontais
    while linha < num_linhas:
        coluna = 0
        while coluna < num_colunas:
            if todas_linhas[linha][coluna] == "9":
                if coluna + 1 < num_colunas: 
                    if todas_linhas[linha][coluna + 1] == "9":
                        xIni = coluna
                        yIni = linha
                        yFim = linha
                        coluna += 1
                        while todas_linhas[linha][coluna] == "9":
                            xFim = coluna
                            coluna += 1
                        coluna = xFim
                        lista_portas_horizontais.append([xIni, xFim, yIni, yFim])
            coluna += 1
        linha += 1

    # linha verticais
    linha = 0
    coluna = 0
    while coluna <= num_colunas:
        linha = 0
        while linha < num_linhas:
            if todas_linhas[linha][coluna] == "9":
                if linha + 1 < num_linhas: 
                    if todas_linhas[linha +1][coluna] == "9":
                        xIni = coluna
                        xFim = coluna
                        yIni = linha
                        linha += 1
                        while todas_linhas[linha][coluna] == "9":
                            yFim = linha
                            linha += 1
                        linha = yFim
                        lista_portas_verticais.append([xIni, xFim, yIni, yFim])
            linha += 1
        coluna += 1

    pos_portas = []
    dicionario_saida_porta = {}
    for sublista in lista_portas_horizontais:
        x = (sublista[0] + sublista[1]) / 2
        y = (sublista[2] + sublista[3]) / 2
        pos_portas += [[x, y]]
        indice =[x, y]
        # if y > 10:
        #     y = y +1
        # else:
        #     y = y -1
        if matriz_estatica[int(y + 1)][int(x)] < matriz_estatica[int(y -1)][int(x)]:
            dicionario_saida_porta[tuple(indice)] = [x, y +1]
        else:
            dicionario_saida_porta[tuple(indice)] = [x, y -1]
        
    
    for sublista in lista_portas_verticais:
        x =int( (sublista[0] + sublista[1]) / 2)
        y =int( (sublista[2] + sublista[3]) / 2)
        pos_portas += [[x, y]]
        indice = [x, y]
        # if x > 40:
        #     x = x +1
        # else:
        #     x = x -1
        if matriz_estatica[int(y)][int(x + 1)] < matriz_estatica[int(y)][int(x -1)]:
            dicionario_saida_porta[tuple(indice)] = [x +1, y]
        else:
            dicionario_saida_porta[tuple(indice)] = [x -1, y]

    # print("Posição das portas internas:", pos_portas, dicionario_saida_porta)

    return pos_portas, dicionario_saida_porta


def posComodos ():
    linha = 0
    coluna = 0
    pos_comodos = []

    linha =0
    coluna = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 5:
                xIni = j
                yIni = i
                linha = i
                coluna = j
                while matriz[linha][coluna] == 5:
                    while matriz[linha][coluna] == 5:
                        matriz[linha][coluna] = 0
                        xFim = coluna
                        coluna += 1
                    yFim = linha
                    linha += 1
                    coluna = xIni
                pos_comodos.append([xIni, xFim, yIni, yFim])
                            
    print("Posição dos comodos:", pos_comodos)

    return pos_comodos


def posPedestres(lista_linhas, num_pedestres):
    lista_pedestres = []
    largura_mapa = num_colunas- 3
    altura_mapa = num_linhas- 2
    posicoes_possiveis = [(x+1, y) for x in range(largura_mapa) for y in range(altura_mapa) if (x+1, y) not in lista_linhas]

    while len(lista_pedestres) < num_pedestres:
        pos = random.choice(posicoes_possiveis)
        if pos not in lista_pedestres:
            lista_pedestres.append(pos)
    
    print("Posição dos pedestres:", lista_pedestres)
    return lista_pedestres

def portaProxima(pos_pedestre, pos_portas, lista_com_portas_internas):
    i = 0
    lista_final = []

    print("pos pedestre:", pos_pedestre)
    print("pos portas:", pos_portas)
    print("lista com portas internas:", lista_com_portas_internas)

    for ped in pos_pedestre:
        
        # Calcula distâncias para portas externas
        distancias_externas = [np.sqrt((ped[0]-porta[0])**2 + (ped[1]-porta[1])**2) for porta in pos_portas]
        porta_externa_proxima = pos_portas[np.argmin(distancias_externas)]
        porta_proxima = porta_externa_proxima
        print("Porta externa mais próxima:", porta_proxima)
        if porta_proxima[1] <= 0:
            lista_final.append([lista_com_portas_internas[i][0], lista_com_portas_internas[i][1], 0.5, 0.5, lista_com_portas_internas[i][2], porta_proxima[0], porta_proxima[1], porta_proxima[0], porta_proxima[1] -10])
        elif porta_proxima[1] >= num_linhas:
            lista_final.append([lista_com_portas_internas[i][0], lista_com_portas_internas[i][1], 0.5, 0.5, lista_com_portas_internas[i][2], porta_proxima[0], porta_proxima[1], porta_proxima[0], porta_proxima[1] + 80])
        elif porta_proxima[0] >= num_colunas - 1 :
            lista_final.append([lista_com_portas_internas[i][0], lista_com_portas_internas[i][1], 0.5, 0.5, lista_com_portas_internas[i][2],porta_proxima[0], porta_proxima[1], porta_proxima[0] + 100, porta_proxima[1]])
        else:
            lista_final.append([lista_com_portas_internas[i][0], lista_com_portas_internas[i][1], 0.5, 0.5, lista_com_portas_internas[i][2], porta_proxima[0], porta_proxima[1], porta_proxima[0] -10, porta_proxima[1]])
        i += 1

    
    lista_final = retiraListaAninhada(lista_final)
    # Encontra o tamanho máximo das sub-listas
    max_len = max(len(lst) for lst in lista_final)

    # # Preenche sub-listas com np.nan para que todas tenham o mesmo tamanho
    lista_final = [lst + [np.nan]*(max_len-len(lst)) for lst in lista_final]
    print("Lista final:", lista_final)

    return lista_final

def retiraListaAninhada (lista):
    nova_final = []

    # Percorre cada elemento na lista original
    for sublist in lista:
        # Cria uma sublista temporária
        temp_list = []
        # Percorre cada item na sublista
        for item in sublist:
            # Se o item é uma lista, estende a sublista temporária com os itens
            if isinstance(item, list):
                temp_list.extend(item)
            # Se o item não é uma lista, apenas adiciona o item à sublista temporária
            else:
                temp_list.append(item)
        # Adiciona a sublista temporária à nova lista
        nova_final.append(temp_list)

    return nova_final

def verificaCaminho(pos_pedestre, pos_portas, portas_por_comodo, lista_comodos, dicionario_portas_internas_frente):
    i=0
    lista_final = []
    caminho = []
    comodoId = 0
    pos_final_pedestre = []
    for ped in pos_pedestre:
        inComodo = True
        ped_aux = ped
        comodoId = 0
        while comodoId in range(len(lista_comodos)):
            # print("yMin:", lista_comodos[comodoId][2])
            # print("yMax:", lista_comodos[comodoId][3])
            # print("ped_aux:", ped_aux)
            # print("comodo pos xmin xmax ymin ymax:", lista_comodos[comodoId][0], lista_comodos[comodoId][1], lista_comodos[comodoId][2], lista_comodos[comodoId][3])
            # print("comodoId:", comodoId)
            # print("comp 1" , lista_comodos[comodoId][0]  <= ped_aux[0] <= lista_comodos[comodoId][1])
            # print("comp 2" , lista_comodos[comodoId][2] <= ped_aux[1] <= lista_comodos[comodoId][3])
            # print("ped:", lista_comodos[comodoId][0]  <= ped_aux[0] <= lista_comodos[comodoId][1] and lista_comodos[comodoId][2] <= ped_aux[1] <= lista_comodos[comodoId][3])
            if  lista_comodos[comodoId][0]  <= ped_aux[0] <= lista_comodos[comodoId][1] and lista_comodos[comodoId][2] <= ped_aux[1] <= lista_comodos[comodoId][3]:
                
                # print("Caminho:", caminho)

                ped_aux = portas_por_comodo[lista_comodos[comodoId][0], lista_comodos[comodoId][1], lista_comodos[comodoId][2], lista_comodos[comodoId][3]][0]
                ped_aux = dicionario_portas_internas_frente[ped_aux[0], ped_aux[1]]
                caminho  = caminho + ped_aux
                
                # print("ped aux:", ped_aux)
                comodoId += 1
            else:
                comodoId += 1
        pos_final_pedestre.append(ped_aux)
        lista_final.append([ped[0], ped[1], caminho])
        caminho = []

    portaProxima(pos_final_pedestre, pos_portas, lista_final)
    return 0

# certa
def encontrar_portas_por_comodo(comodos, portas):
    portas_por_comodo = {}

    for comodo in comodos:
        x_ini, x_final, y_ini, y_final = comodo
        portas_no_comodo = []

        for porta in portas:
            x, y = porta
            # print(x, y)
            # print(x_ini, x_final, y_ini, y_final)
            if x_ini-1 <= x <= x_final+1 and y_ini-1 <= y <= y_final+1:
                portas_no_comodo.append(porta)
        portas_por_comodo[tuple(comodo)] = portas_no_comodo

    # print("Portas por comodo:", portas_por_comodo)
    portas_unicas = []
    for comodo, portas in portas_por_comodo.items():
        if len(portas) == 1:
            portas_unicas.append(portas[0])

    for comodo, portas in portas_por_comodo.items():
        if len(portas) > 1:
            portas_por_comodo[comodo] = [porta for porta in portas if porta not in portas_unicas]

    # print("Portas únicas:", portas_por_comodo)
    return portas_por_comodo


def read_file_to_matrix(filename):
    with open(filename, 'r') as f:
        matrix = json.load(f)
    return matrix

def define_porta_estatico(comodos, portas, static):
    portas_por_comodo = {}

    for comodo in comodos:
        x_ini, x_final, y_ini, y_final = comodo
        portas_no_comodo = []

        for porta in portas:
            x, y = porta
            if x_ini-1 <= x <= x_final+1 and y_ini-1 <= y <= y_final+1:
                portas_no_comodo.append(porta)

        portas_por_comodo[tuple(comodo)] = portas_no_comodo


    for comodo, portas in portas_por_comodo.items():
        print(f"Comodo {comodo}: Portas {portas}")


lista_de_linhas = constroiMapa()


# lista_portas = posPortas()

lista_comodos = posComodos()
lista_portas_internas, dicionario_portas_internas_frente = posPortasInternas()
portas_por_comodo = encontrar_portas_por_comodo(lista_comodos, lista_portas_internas)

ped = [(83, 3), (80, 20), (82, 55)]
# ped  = posPedestres(lista_de_linhas, 5)
verificaCaminho(ped, posPortas(), portas_por_comodo, lista_comodos, dicionario_portas_internas_frente)

# port= portaProxima(ped, posPortas(), lista_portas_internas)
# pos_ped  = posPedestres(lista_de_linhas, 3)
# print (pos_ped)
# static = read_file_to_matrix(r'D:\Faculdade\TCC\Codigo\TCC\PySocialForce\mapa script\unified\static.txt')
# define_porta_estatico(lista_comodos, lista_portas_internas, static)


# for comodo, portas in portas_por_comodo.items():
#     print(f"Comodo {comodo}: Portas {portas}")

# print("Lista de comodos:", lista_comodos)

# ped = posPedestres(lista_de_linhas, 10)
# verificaCaminho(ped, lista_portas)

# lista_final = portaProxima(posPedestres(lista_de_linhas, 30), lista_portas, lista_portas_internas)
# print("Lista final:", lista_final)

# Feche o arquivo
arquivo.close()
