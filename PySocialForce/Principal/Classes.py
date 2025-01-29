import random
import numpy as np
import json

class Mapa:
    def __init__(self, arquivo_mapa, arquivo_mapa_static, arquivo_mapa_alterado, saida_comodo, vazio):
        self.arquivo_mapa_padrao = arquivo_mapa
        self.arquivo_mapa_static = arquivo_mapa_static
        self.arquivo_mapa_alterado = arquivo_mapa_alterado
        self.saida_comodo = saida_comodo
        self.vazio = vazio

        self.matriz_mapa, self.matriz_mapa_alterado, self.num_linhas, self.num_colunas = self.carrega_mapa()
        self.matriz_mapa_estatico = self.carrega_mapa_estatico()
        self.linhas_do_mapa = self.constroiMapa()
        self.pos_portas = self.posPortas()
        self.pos_portas_internas, self.dicionario_portas_internas_saida = self.posPortasInternas()
        self.pos_comodos = self.posComodos()
        self.portas_por_comodo = self.encontrar_portas_por_comodo()
        self.pos_invalidas = self.posInvalidas()

    def carrega_mapa(self):
        with open(self.arquivo_mapa_padrao, 'r') as f:
            content = f.readlines()

        with open(self.arquivo_mapa_alterado, 'r') as file:
            matriz_mapa_alterado = file.readlines()
        
        matriz = [list(map(int, linha.strip())) for linha in content]
        matriz_mapa_alterado = [list(map(int, linha.strip())) for linha in matriz_mapa_alterado]

        num_linhas = len(matriz)-1
        num_colunas = len(matriz[0])-1
        
        # Feche o arquivo
        f.close()
        file.close()
        return matriz, matriz_mapa_alterado, num_linhas, num_colunas
    
    def carrega_mapa_estatico(self):
        with open(self.arquivo_mapa_static, 'r') as f:
            content = f.read()

        # Remova a última vírgula para tornar o conteúdo um JSON válido
        if content.endswith(','):
            content = content[:-1]

        # Use json.loads para transformar a string em uma matriz
        matriz_estatica = json.loads(content)
        # Feche o arquivo
        f.close()

        return matriz_estatica

    def constroiMapa (self):
        linha = 0
        coluna = 0
        lista_de_linhas_do_mapa = []


        # linha horizontais
        while linha < self.num_linhas:
            coluna = 0
            while coluna < self.num_colunas:
                if self.matriz_mapa[linha][coluna] == 1:
                    if coluna + 1 < self.num_colunas: 
                        if self.matriz_mapa[linha][coluna + 1] == 1:
                            xIni = coluna
                            yIni = linha
                            yFim = linha
                            coluna += 1
                            while self.matriz_mapa[linha][coluna] == 1:
                                xFim = coluna
                                coluna += 1
                            coluna = xFim
                            lista_de_linhas_do_mapa.append([xIni, xFim, yIni, yFim])
                coluna += 1
            linha += 1

        # linha verticais
        linha = 0
        coluna = 0
        while coluna <= self.num_colunas:
            linha = 0
            while linha < self.num_linhas:
                if self.matriz_mapa[linha][coluna] == 1:
                    if linha + 1 < self.num_linhas: 
                        if self.matriz_mapa[linha +1][coluna] == 1:
                            xIni = coluna
                            xFim = coluna
                            yIni = linha
                            linha += 1
                            while self.matriz_mapa[linha][coluna] == 1:
                                yFim = linha
                                linha += 1
                            linha = yFim
                            lista_de_linhas_do_mapa.append([xIni, xFim, yIni, yFim])
                linha += 1
            coluna += 1

        # print("Linhas do mapa:", lista_de_linhas_do_mapa)
        return lista_de_linhas_do_mapa
    
    def posInvalidas (self):
        linha = 0
        coluna = 0
        lista_de_linhas_do_mapa = []


        # linha horizontais
        while linha < self.num_linhas:
            coluna = 0
            while coluna < self.num_colunas:
                if self.matriz_mapa[linha][coluna] == 7:
                    if coluna + 1 < self.num_colunas: 
                        if self.matriz_mapa[linha][coluna + 1] == 7:
                            xIni = coluna
                            yIni = linha
                            yFim = linha
                            coluna += 1
                            while self.matriz_mapa[linha][coluna] == 7:
                                xFim = coluna
                                coluna += 1
                            coluna = xFim
                            lista_de_linhas_do_mapa.append([xIni, xFim, yIni, yFim])
                coluna += 1
            linha += 1

        # linha verticais
        linha = 0
        coluna = 0
        while coluna <= self.num_colunas:
            linha = 0
            while linha < self.num_linhas:
                if self.matriz_mapa[linha][coluna] == 7:
                    if linha + 1 < self.num_linhas: 
                        if self.matriz_mapa[linha +1][coluna] == 7:
                            xIni = coluna
                            xFim = coluna
                            yIni = linha
                            linha += 1
                            while self.matriz_mapa[linha][coluna] == 7:
                                yFim = linha
                                linha += 1
                            linha = yFim
                            lista_de_linhas_do_mapa.append([xIni, xFim, yIni, yFim])
                linha += 1
            coluna += 1

        # print("Linhas do mapa:", lista_de_linhas_do_mapa)
        return lista_de_linhas_do_mapa
   
    def posPortas (self):
        linha = 0
        coluna = 0
        lista_portas_horizontais = []
        lista_portas_verticais = []
        # linhas horizontais
        while linha < self.num_linhas:
            coluna = 0
            while coluna < self.num_colunas:
                if self.matriz_mapa[linha][coluna] == 2:
                    if coluna + 1 < self.num_colunas: 
                        if self.matriz_mapa[linha][coluna + 1] == 2:
                            xIni = coluna
                            yIni = linha
                            yFim = linha
                            coluna += 1
                            while self.matriz_mapa[linha][coluna] == 2:
                                xFim = coluna
                                coluna += 1
                            coluna = xFim
                            lista_portas_horizontais.append([xIni, xFim, yIni, yFim])
                coluna += 1
            linha += 1

        # linha verticais
        linha = 0
        coluna = 0
        while coluna <= self.num_colunas:
            linha = 0
            while linha < self.num_linhas:
                if self.matriz_mapa[linha][coluna] == 2:
                    if linha + 1 < self.num_linhas: 
                        if self.matriz_mapa[linha +1][coluna] == 2:
                            xIni = coluna
                            xFim = coluna
                            yIni = linha
                            linha += 1
                            while self.matriz_mapa[linha][coluna] == 2:
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
            pos_portas += [[x, y]]
        
        for sublista in lista_portas_verticais:
            x = (sublista[0] + sublista[1]) / 2
            y = (sublista[2] + sublista[3]) / 2
            pos_portas += [[x, y]]

        # print("Posição das portas externas:", pos_portas)

        return pos_portas

    def posPortasInternas (self):
        linha = 0
        coluna = 0
        lista_portas_horizontais = []
        lista_portas_verticais = []
        # linha horizontais
        while linha < self.num_linhas:
            coluna = 0
            while coluna < self.num_colunas:
                if self.matriz_mapa_alterado[linha][coluna] == 9:
                    if coluna + 1 < self.num_colunas: 
                        if self.matriz_mapa_alterado[linha][coluna + 1] == 9:
                            xIni = coluna
                            yIni = linha
                            yFim = linha
                            coluna += 1
                            while self.matriz_mapa_alterado[linha][coluna] == 9:
                                xFim = coluna
                                coluna += 1
                            coluna = xFim
                            lista_portas_horizontais.append([xIni, xFim, yIni, yFim])
                coluna += 1
            linha += 1

        # linha verticais
        linha = 0
        coluna = 0
        while coluna <= self.num_colunas:
            linha = 0
            while linha < self.num_linhas:
                if self.matriz_mapa_alterado[linha][coluna] == 9:
                    if linha + 1 < self.num_linhas: 
                        if self.matriz_mapa_alterado[linha +1][coluna] == 9:
                            xIni = coluna
                            xFim = coluna
                            yIni = linha
                            linha += 1
                            while self.matriz_mapa_alterado[linha][coluna] == 9:
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
            if self.matriz_mapa_estatico[int(y + 1)][int(x)] < self.matriz_mapa_estatico[int(y -1)][int(x)]:
                dicionario_saida_porta[tuple(indice)] = [x, y +1]
            else:
                dicionario_saida_porta[tuple(indice)] = [x, y -1]
            
        
        for sublista in lista_portas_verticais:
            x =int( (sublista[0] + sublista[1]) / 2)
            y =int( (sublista[2] + sublista[3]) / 2)
            pos_portas += [[x, y]]
            indice = [x, y]
            if self.matriz_mapa_estatico[int(y)][int(x + 1)] < self.matriz_mapa_estatico[int(y)][int(x -1)]:
                dicionario_saida_porta[tuple(indice)] = [x + self.saida_comodo, y]
            else:
                dicionario_saida_porta[tuple(indice)] = [x - self.saida_comodo, y]

        print("Posição das portas internas:", pos_portas)
        print("Dicionário de saída das portas internas:", dicionario_saida_porta)
        return pos_portas, dicionario_saida_porta

    def posComodos (self):
        linha = 0
        coluna = 0
        pos_comodos = []

        linha =0
        coluna = 0
        for i in range(len(self.matriz_mapa_alterado)):
            for j in range(len(self.matriz_mapa_alterado[i])):
                if self.matriz_mapa_alterado[i][j] == 5:
                    xIni = j
                    yIni = i
                    linha = i
                    coluna = j
                    while self.matriz_mapa_alterado[linha][coluna] == 5:
                        while self.matriz_mapa_alterado[linha][coluna] == 5:
                            self.matriz_mapa_alterado[linha][coluna] = 0
                            xFim = coluna
                            coluna += 1
                        yFim = linha
                        linha += 1
                        coluna = xIni
                    pos_comodos.append([xIni, xFim, yIni, yFim])

        # print("Posição dos comodos:", pos_comodos)
        return pos_comodos

    def encontrar_portas_por_comodo(self):
        portas_por_comodo = {}

        for comodo in self.pos_comodos:
            x_ini, x_final, y_ini, y_final = comodo
            portas_no_comodo = []

            for porta in self.pos_portas_internas:
                x, y = porta
                if x_ini-1 <= x <= x_final+1 and y_ini-1 <= y <= y_final+1:
                    portas_no_comodo.append(porta)
            portas_por_comodo[tuple(comodo)] = portas_no_comodo

        portas_unicas = []
        for comodo, portas in portas_por_comodo.items():
            if len(portas) == 1:
                portas_unicas.append(portas[0])

        for comodo, portas in portas_por_comodo.items():
            if len(portas) > 1:
                portas_por_comodo[comodo] = [porta for porta in portas if porta not in portas_unicas]

        # print("Portas por comodo:", portas_por_comodo)
        return portas_por_comodo


class Pedestres:
    def __init__(self, arquivo_mapa, arquivo_mapa_static, arquivo_mapa_alterado, qtd_pedestres, saida_comodo, vazio, seed):
        self.mapa = Mapa(arquivo_mapa, arquivo_mapa_static, arquivo_mapa_alterado, saida_comodo, vazio)
        self.qtd_pedestres = qtd_pedestres
        self.seed = seed
        self.saida_comodo = saida_comodo
        self.vazio = vazio
        self.pos_pedestres = self.posPedestres()
        self.lista_final = self.verificaCaminho()
           
    def posPedestres(self):
        lista_pedestres = []
        largura_mapa = self.mapa.num_colunas -1
        altura_mapa = self.mapa.num_linhas -1
        # posicoes_possiveis = [(x, y) for x in range(2, largura_mapa) for y in range(2, altura_mapa) if (x, y) not in self.mapa.linhas_do_mapa]
        
        # Cria uma lista de todas as posições possíveis no mapa
        posicoes_possiveis = [(x, y) for x in range(2, largura_mapa) for y in range(2, altura_mapa)]

        # Remove as posições que estão dentro de uma linha do mapa
        for linha in self.mapa.linhas_do_mapa:
            xIni, xFim, yIni, yFim = linha
            posicoes_possiveis = [(x, y) for (x, y) in posicoes_possiveis if not (xIni <= x <= xFim and yIni <= y <= yFim)]

        # Remove as posições que estão dentro de uma linha do mapa
        for linha in self.mapa.pos_invalidas:
            xIni, xFim, yIni, yFim = linha
            posicoes_possiveis = [(x, y) for (x, y) in posicoes_possiveis if not (xIni <= x <= xFim and yIni <= y <= yFim)]


        random.seed(self.seed)
        while len(lista_pedestres) < self.qtd_pedestres:
            pos = random.choice(posicoes_possiveis)
            if pos not in lista_pedestres:
                lista_pedestres.append(pos)
    
        return lista_pedestres

    def portaProxima(self, lista_com_portas_internas, pos_final_pedestre):

        i = 0
        lista_final = []

        for ped in pos_final_pedestre:
            
            # Calcula distâncias para portas externas
            distancias_externas = [np.sqrt((ped[0]-porta[0])**2 + (ped[1]-porta[1])**2) for porta in self.mapa.pos_portas]
            porta_externa_proxima = self.mapa.pos_portas[np.argmin(distancias_externas)]
            porta_proxima = porta_externa_proxima
            if porta_proxima[1] <= 1:
                lista_final.append([lista_com_portas_internas[i][0], lista_com_portas_internas[i][1], 0.5, 0.5, lista_com_portas_internas[i][2], porta_proxima[0], porta_proxima[1], porta_proxima[0], porta_proxima[1] - self.vazio])
            elif porta_proxima[1] >= self.mapa.num_linhas - 2:
                lista_final.append([lista_com_portas_internas[i][0], lista_com_portas_internas[i][1], 0.5, 0.5, lista_com_portas_internas[i][2], porta_proxima[0], porta_proxima[1], porta_proxima[0], porta_proxima[1] + self.vazio])
            elif porta_proxima[0] >= self.mapa.num_colunas - 2:
                lista_final.append([lista_com_portas_internas[i][0], lista_com_portas_internas[i][1], 0.5, 0.5, lista_com_portas_internas[i][2],porta_proxima[0], porta_proxima[1], porta_proxima[0] + self.vazio, porta_proxima[1]])
            else:
                lista_final.append([lista_com_portas_internas[i][0], lista_com_portas_internas[i][1], 0.5, 0.5, lista_com_portas_internas[i][2], porta_proxima[0], porta_proxima[1], porta_proxima[0] -self.vazio, porta_proxima[1]])
            i += 1

        
        lista_final = self.retiraListaAninhada(lista_final)
        # Encontra o tamanho máximo das sub-listas
        max_len = max(len(lst) for lst in lista_final)

        # Preenche sub-listas com np.nan para que todas tenham o mesmo tamanho
        lista_final = [lst + [np.nan]*(max_len-len(lst)) for lst in lista_final]

        # print("Lista final: ", lista_final)
        return lista_final

    def retiraListaAninhada (self, lista):
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

    def verificaCaminho(self):
        lista_final = []
        caminho = []
        comodoId = 0
        comodoId_verificado = []
        pos_final_pedestre = []
        for ped in self.pos_pedestres:
            ped_aux = ped
            comodoId = 0
            comodoId_verificado = []
            while comodoId in range(len(self.mapa.pos_comodos)):
                if comodoId not in comodoId_verificado:
                    if  self.mapa.pos_comodos[comodoId][0]  <= ped_aux[0] <= self.mapa.pos_comodos[comodoId][1] and self.mapa.pos_comodos[comodoId][2] <= ped_aux[1] <= self.mapa.pos_comodos[comodoId][3]:
                        ped_aux = self.mapa.portas_por_comodo[self.mapa.pos_comodos[comodoId][0], self.mapa.pos_comodos[comodoId][1], self.mapa.pos_comodos[comodoId][2], self.mapa.pos_comodos[comodoId][3]][0]
                        ped_aux = self.mapa.dicionario_portas_internas_saida[ped_aux[0], ped_aux[1]]
                        caminho  = caminho + ped_aux
                        comodoId_verificado.append(comodoId)
                        comodoId = 0
                    else:
                        comodoId += 1
                else:
                    comodoId += 1
            pos_final_pedestre.append(ped_aux)
            lista_final.append([ped[0], ped[1], caminho])
            # print("Caminho do pedestre:", caminho)
            caminho = []
        
        return self.portaProxima(lista_final, pos_final_pedestre)



# # caminho relativo do arquivo do mapa sem alterações
# arquivo_mapa = "TCC\PySocialForce\Principal\mapa 3\cinema.txt"
# # caminho relativo do arquivo do mapa com alterações
# arquivo_mapa_alterado = "TCC\PySocialForce\Principal\mapa 3\cinema_comodos.txt"
# # caminho relativo do arquivo do mapa estatico
# arquivo_mapa_static = "TCC\PySocialForce\Principal\mapa 3\static_mapa_cinema.txt"
# # quantidade de pedestres
# qtd_pedestres = 150

# ped = Pedestres(arquivo_mapa, arquivo_mapa_static, arquivo_mapa_alterado, qtd_pedestres)




# print("Lista final: ", ped.lista_final)