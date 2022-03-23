import numpy as np


class TableroAutomatico:
    ganador: int
    tablero: np.ndarray
    turnos: int

    def __init__(self, configuracion: np.ndarray):
        if len(configuracion) != 9:
            raise ValueError('La configuración del tablero debe ser de 9 individuos')
        else:
            if self.__validar(configuracion):
                ganador = self.__definirGanador()

                if self.turnos < 9:
                    if ganador != 0:
                        if ganador != -1:
                            self.ganador = ganador
                        else:
                            raise ValueError("Existen 2 ganadores en la configuracion")
                    else:
                        raise ValueError("La configuración es un juego incompleto")

                elif ganador != -1:
                    self.ganador = ganador
                else:
                    raise ValueError("Existen 2 ganadores en la configuracion")
            else:
                raise ValueError("El tablero no tiene una configuración adecuada")

    def __validar(self, conf) -> bool:
        vacio = np.count_nonzero(conf == 0)
        equis = np.count_nonzero(conf == 1)
        circulo = np.count_nonzero(conf == 2)
        if (vacio % 2 == 0 and vacio <= 4) and (equis - 1 == circulo or equis + 1 == circulo):
            self.tablero = conf
            self.turnos = equis + circulo
            return True
        elif equis == circulo and vacio <= 3:
            self.tablero = conf
            self.turnos = equis + circulo
            return True
        else:
            return False

    def __definirGanador(self) -> int:
        arr = self.tablero

        ganador = -1
        if arr.item(0) != 0:
            eval = arr.item(0)
            # Linea 1, 2, 3
            if (eval == arr.item(1)) and eval == arr.item(2):
                if ganador != -1:
                    return -1
                ganador = eval
            # Diagonal 1, 5, 9
            if (eval == arr.item(3)) and eval == arr.item(6):
                if ganador != -1:
                    return -1
                ganador = eval
            # Linea 1, 4, 7
            if (eval == arr.item(4)) and eval == arr.item(8):
                if ganador != -1:
                    return -1
                ganador = eval
        if arr.item(3) != 0:
            eval = arr.item(3)
            # Linea 4, 5, 6
            if (eval == arr.item(4)) and eval == arr.item(5):
                if ganador != -1:
                    return -1
                ganador = eval
        if arr.item(6) != 0:
            eval = arr.item(6)
            # Linea 7, 5, 3
            if (eval == arr.item(4)) and eval == arr.item(2):
                if ganador != -1:
                    return -1
                ganador = eval
            # Linea 7, 8, 9
            if (eval == arr.item(7)) and eval == arr.item(8):
                if ganador != -1:
                    return -1
                ganador = eval
        if arr.item(1) != 0:
            eval = arr.item(1)
            # Linea 2, 5, 8
            if (eval == arr.item(4)) and eval == arr.item(7):
                if ganador != -1:
                    return -1
                ganador = eval
        if arr.item(2) != 0:
            eval = arr.item(2)
            # Linea 3, 6, 9
            if (eval == arr.item(5)) and eval == arr.item(8):
                if ganador != -1:
                    return -1
                ganador = eval

        if ganador != -1:
            return ganador

        return 0

    def __str__(self):
        msg = f"El tablero es: {self.tablero}\n" \
              f"La cantidad de turnos fue: {self.turnos}\n"
        if self.ganador == 0:
            msg += f"El resultado fue un empate\n"
        elif self.ganador == 1:
            msg += f"Ganaron las X\n"
        else:
            msg += f"Ganaron los O\n"

        return msg
