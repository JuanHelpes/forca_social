import Classes
import numpy as np
# mapa escola
# caminho relativo do arquivo do mapa sem alterações
arquivo_mapa = "TCC\PySocialForce\construtor mapas\escola.map"
# caminho relativo do arquivo do mapa com alterações
arquivo_mapa_alterado = "TCC\PySocialForce\construtor mapas\escola.map"
# caminho relativo do arquivo do mapa estatico
arquivo_mapa_static = "TCC/PySocialForce/mapa script/unified/static.txt"
# valor para saida do comodo



resultado = Classes.Pedestres(arquivo_mapa, arquivo_mapa_static, arquivo_mapa_alterado)
mapa = Classes.Mapa(arquivo_mapa, arquivo_mapa_static, arquivo_mapa_alterado)
print("mapa: " , mapa.linhas_do_mapa)
print("Pos pedestres: ", resultado.lista_final)


