from Tablero import TableroAutomatico, np
from Generador import configuracionOpuesta, generarConfiguracion
import math
import csv

arr = []
fallidos = []
vueltas = 0
CONFS = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 0]
]
equis = 3
circulos = 2
eje = True

while equis <= 4 and circulos <= 4:

    espacios = 9 - (equis + circulos)

    esperados = math.factorial(6) / (math.factorial(espacios) * math.factorial(equis - 3) * math.factorial(circulos))

    for i in range(len(CONFS)):
        fallidosAux = []
        arrAux = []
        while (len(arrAux) + len(fallidosAux)) < esperados:
            configuracion = []
            for it in CONFS[i]:
                configuracion.append(it)

            tablero = generarConfiguracion(equis - 3, circulos, configuracion)

            conf = np.array(tablero)

            evaluado = False

            if len(fallidosAux) != 0:
                for x in fallidosAux:
                    if np.allclose(x, conf):
                        evaluado = True
                        break
            if len(arrAux) != 0:
                for x in arrAux:
                    if np.allclose(x.tablero, conf):
                        evaluado = True
                        break

            try:
                if not evaluado:
                    clase = TableroAutomatico(conf)
                    arrAux.append(clase)
            except:
                if ValueError:
                    fallidosAux.append(tablero)
            vueltas += 1

        arr.append(arrAux)
        fallidos.append(fallidosAux)

    if eje:
        eje = False
        circulos += 1
    else:
        eje = True
        equis += 1

espacios = 9 - (equis + circulos)

esperados = math.factorial(9) / (math.factorial(espacios) * math.factorial(equis) * math.factorial(circulos))

arrAux = []
fallidosAux = []

while (len(arrAux) + len(fallidosAux)) < esperados:
    tablero = generarConfiguracion(equis, circulos)
    conf = np.array(tablero)

    evaluado = False

    if len(fallidosAux) != 0:
        for x in fallidosAux:
            if np.allclose(x, conf):
                evaluado = True
                break
    if len(arrAux) != 0:
        for x in arrAux:
            if np.allclose(x.tablero, conf):
                evaluado = True
                break

    try:
        if not evaluado:
            clase = TableroAutomatico(conf)
            arrAux.append(clase)
    except:
        if ValueError:
            fallidosAux.append(tablero)
    vueltas += 1
arr.append(arrAux)
top = len(arr)
for x in range(top):
    arrAux = []
    for y in arr[x]:
        aux = []
        for lt in range(len(y.tablero)):
            aux.append(y.tablero.item(lt))
        tablero = configuracionOpuesta(np.array(aux))
        clase = TableroAutomatico(tablero)
        arrAux.append(clase)
    arr.append(arrAux)

with open("gatoSets.csv", "w") as csvFile:
    fieldnames = ['POS1', 'POS2', 'POS3', 'POS4', 'POS5', 'POS6', 'POS7', 'POS8', 'POS9', 'Ganador', 'Turnos']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)

    writer.writeheader()
    for x in arr:
        for y in x:
            writer.writerow({
                'POS1': y.tablero.item(0),
                'POS2': y.tablero.item(1),
                'POS3': y.tablero.item(2),
                'POS4': y.tablero.item(3),
                'POS5': y.tablero.item(4),
                'POS6': y.tablero.item(5),
                'POS7': y.tablero.item(6),
                'POS8': y.tablero.item(7),
                'POS9': y.tablero.item(8),
                'Ganador': y.ganador,
                'Turnos': y.turnos
            })
print("Terminado")