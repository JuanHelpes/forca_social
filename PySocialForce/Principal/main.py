import Classes
import Simulador
import Estatisticas
import sys
import importlib
import os
# O primeiro argumento é o nome do módulo que queremos importar
module_name = sys.argv[1]

seed = sys.argv[2]


# Importando o módulo usando importlib
config = importlib.import_module(module_name)
os.makedirs("D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\\" + str(module_name) + "\seed_" + str(seed), exist_ok=True)

resultado = Classes.Pedestres(config.arquivo_mapa, config.arquivo_mapa_static, config.arquivo_mapa_alterado, config.qtd_pedestres, config.saida_comodo, config.vazio, seed)

Simulador.Simular(resultado.lista_final, resultado.mapa.linhas_do_mapa, config.n_passos, config.xlim, config.ylim, config.xticks, config.yticks, config.caminho, config.arquivoPassos, seed).iniciar_simulacao()

estatistica =  Estatisticas.Estatistica("D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\\" + str(module_name) + "\seed_" + str(seed) + "\passos_seed_" + str(seed) + ".txt", config.qtd_pedestres, config.caminho, seed)

estatistica.plotar_grafico()
estatistica.calcular_taxa_saida()

# python main.py mapa_X seed