
from random import sample

def roullete(population):
    pass


def rank(population):
    pass


def tournament(population):
    pool = sample(population, 4)
    pool.sort(key=lambda x: x.rank)
    return pool[0], pool[1]


def boltzmann(population):
    pass