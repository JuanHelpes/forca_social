from pathlib import Path
import numpy as np
import pysocialforce as psf


class Simular:
    def __init__(self, inicial_state, obs, passos, xlim, ylim, xticks, yticks, caminho, arquivoPassos, seed, groups= None):
        # initial states, each entry is the position, velocity and goal of a pedestrian in the form of (px, py, vx, vy, gx, gy)
        self.inicial_state = np.array( inicial_state)
        # list of linear obstacles given in the form of (x_min, x_max, y_min, y_max)
        self.obs = obs
        self.passos = passos
        self.xlim = xlim
        self.ylim = ylim
        self.xticks = xticks
        self.yticks = yticks
        # social groups informoation is represented as lists of indices of the state array
        self.groups = groups
        self.caminho = caminho + '\\seed_' + str(seed) + '\mapa_seed_' + str(seed)
        self.arquivoPassos = arquivoPassos + '\\seed_' + str(seed) + '\passos_seed_' + str(seed) + '.txt'

        # print("Simulador criado")
        # print(type(self.inicial_state))

    def iniciar_simulacao(self):
        # initiate the simulator,
        s = psf.Simulator(
            self.inicial_state,
            groups= self.groups,
            obstacles= self.obs,
            config_file=Path(__file__).resolve().parent.joinpath("example.toml"),
        )
        
        s.step(self.passos)

        with psf.plot.SceneVisualizer(s, self.caminho) as sv:
            sv.ax.set_xlim(self.xlim)
            sv.ax.set_ylim(self.ylim)
            sv.ax.set_xticks(self.xticks)
            sv.ax.set_yticks(self.yticks)
            sv.animate()
            s.fim_movimento_peds(self.passos, self.arquivoPassos)
            # sv.plot()
