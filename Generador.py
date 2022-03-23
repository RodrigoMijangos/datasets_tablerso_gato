import numpy as np
import random as rn
from typing import List


def configuracionOpuesta(conf: np.ndarray):
    for d in range(conf.size):
        if conf.item(d) == 1:
            conf[d] = 2
        elif conf.item(d) == 2:
            conf[d] = 1
    return conf


def generarConfiguracion(equis: int, circulos: int, conTablero: List[int] = None):
    if conTablero is None:
        conTablero = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif len(conTablero) != 9:
        raise ValueError("Las configuraciones deben ser de 9 de longitud")

    for x in range(circulos):
        terminado = False
        while not terminado:
            pos = rn.randint(0, 8)
            if conTablero[pos] == 0:
                conTablero[pos] = 2
                terminado = True
    for x in range(equis):
        terminado = False
        while not terminado:
            pos = rn.randint(0, 8)
            if conTablero[pos] == 0:
                conTablero[pos] = 1
                terminado = True

    return conTablero
