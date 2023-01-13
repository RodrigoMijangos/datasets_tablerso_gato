# Generador de entradas de un tablero de GATO
## Introducción 
Calcula posibles entradas y verifica que sean entradas posibles en cuanto un tablero de gato se refiere.
Para ello se usará numpy, puesto que la posición de cada caracter se parece a la de un arreglo con 9 de longitud 
y comparará arreglos que se encuentren ya calculados.
- Un 0 equivale a un espacio vacío, un 1 equivale a una equis y un 2 equivale a un círculo.
 
Ejemplo:
>
>       [ 0 0 0 
>         0 1 2 
>         0 0 0 ]
> 
> Espacios vacíos: 7

Este arreglo nos dice que existe una equis en el centro y un círculo a su lado

> Justo así:
> 
>       Cada posición en el arreglo simboliza una posición en el tablero
> 
>         |   |   |   | [ 0 1 2 ]
>         |---|---|---| 
>         |   | X | O | [ 3 4 5 ]
>         |---|---|---|
>         |   |   |   | [ 6 7 8 ]

Cada arreglo será llamado configuración de ahora en adelante, puesto que el orden de los elementos necesita
de un orden especifico para conocer la posición de las fichas

## Definiendo las reglas

### Definiendo las configuraciones Totales

Existen un total muy extenso de configuraciones posibles, la forma de saber cuales configuraciones existen
es primero definiendo como son nuestras configuraciones
- Existen 9 posiciones en el tablero.
- Cada posición puede ser ocupada por un 0, un 1 y un 2.
- El orden de los elementos dentro del arreglo importa.

La formula y el resultado es el siguiente: $Valores^{Posiciones} = 3^9 = 19,683$

### Configuraciones útiles

Dentro de este total de configuraciones hay muchas que no nos sirven.
Necesitamos todas aquellas configuraciones que definan un juego terminado, ya sea en empate o en victoria para cualquiera de los 2 bandos.

La configuración vacia no nos es útil pues significa que nadie ha tirado aún.

>       |   |   |   | [ 0 0 0 ]
>       |---|---|---| 
>       |   |   |   | [ 0 0 0 ]
>       |---|---|---|
>       |   |   |   | [ 0 0 0 ]      

No nos sirven esas configuraciones donde solo un jugador tira.

>       | X | X | X | [ 1 1 1 ]
>       |---|---|---| 
>       | X | X | X | [ 1 1 1 ]
>       |---|---|---|
>       | X | X | X | [ 1 1 1 ]

No nos sirven esas configuraciones donde no es posible hacer un __tres en raya__.

>       | X | X |   | [ 1 1 0 ]
>       |---|---|---| 
>       | O | O |   | [ 2 2 0 ]
>       |---|---|---|
>       |   |   |   | [ 0 0 0 ] 

#### Factores clave para entender las cadenas válidas

- En el mejor de los casos una ronda durará 5 turnos si el símbolo que empieza es el que gana.
- En el peor de los casos una ronda durará 9 turnos y nadie ganará.
- Un jugador no puede tirar más de una vez de manera consecutiva y siempre tendrá que esperar a que el otro jugador termine su turno.
- Un jugador no puede cambiar de simbolo a mitad de una ronda.
- El jugador que empieza puede hacerlo con cualquier símbolo de su elección. (__X__ o __O__)
- No pueden haber dos ganadores.
- Un jugador no puede ganar 2 veces.
- los empates solo pueden darse si ya no hay espacios en blanco disponibles.

>   Ejemplo de dos ganadores:
>
>       | X | X | X | [ 1 1 1 ]
>       |---|---|---| 
>       | O | O | O | [ 2 2 2 ]
>       |---|---|---|
>       |   |   |   | [ 0 0 0 ]

>   Ejemplo de ganr 2 veces:
>
>       | X | X | X | [ 1 1 1 ]
>       |---|---|---| 
>       | X | O | O | [ 1 2 2 ]
>       |---|---|---|
>       | X | O | O | [ 1 2 2 ]

>   Ejemplo de empate con espacios vacios (_Juego no terminado_):
>
>       | X | X | O | [ 1 1 2 ]
>       |---|---|---| 
>       | X |   | O | [ 1 0 2 ]
>       |---|---|---|
>       |   |   |   | [ 0 0 0 ] 

#### Reglas que definen una configuración válida.

- La cantidad de turnos que una ronda puede durar es mayor o igual que 5 y menor o igual que 9.
- La cantidad de espacios vacios es menor o igual que 5 e igual o mayor a 0.
- La cantidad de espacios vacios es equivalente a la resta entre 9 y la cantidad de turnos efectuados.
- Si la cantidad de espacios vacios es par entonces la cantidad de simbolos equis (__X__) es mayor que la cantidad de simbolos circulo (__O__) en una unidad o
 la cantidad de simbolos circulo (__O__) es mayor a la cantidad de simbolos (__X__) en una unidad.
- Si la cantidad de espacios vacios es impar entonces la cantidad de simbolos equis (__X__) es igual a la cantidad de simbolos circulo (__O__) si y solo si la
 posición de ambos símbolos no permite una doble victoria.
- Si existen espacios vacios el resultado deberá ser una victoria para cualquier símbolo

#### Defiendo parámetros

Para encontrar la cantidad de configuraciones válidas que existen debemos encontrar los límites de los casos según la cantidad de turnos y la cantidad de espacios vacios para saber si nuestras definiciones son correctas.

__Cuando inician las equis (_X_)__
| Cantidad de Turnos| Cantidad de Espacios Vacios | Cantidad de equis (__X__) | Cantidad de Circulos (__O__) |
|------------|---------------|------------|----------|
| 0 | 9 - 0 = 9 | 0 | 0 |
| 1 | 9 - 1 = 8 | 1 | 0 |
| 2 | 9 - 2 = 7 | 1 | 1 |
| 3 | 9 - 3 = 6 | 2 | 1 |
| 4 | 9 - 4 = 5 | 2 | 2 |
| 5 | 9 - 5 = 4 | 3 | 2 |
| 6 | 9 - 6 = 3 | 3 | 3 |
| 7 | 9 - 7 = 2 | 4 | 3 |
| 8 | 9 - 8 = 1 | 4 | 4 |
| 9 | 9 - 9 = 0 | 5 | 4 |

__Cuando inician los circulos (_O_)__
| Cantidad de Turnos| Cantidad de Espacios Vacios | Cantidad de equis (__X__) | Cantidad de Circulos (__O__) |
|------------|---------------|------------|----------|
| 0 | 9 - 0 = 9 | 0 | 0 |
| 1 | 9 - 1 = 8 | 0 | 1 |
| 2 | 9 - 2 = 7 | 1 | 1 |
| 3 | 9 - 3 = 6 | 1 | 2 |
| 4 | 9 - 4 = 5 | 2 | 2 |
| 5 | 9 - 5 = 4 | 2 | 3 |
| 6 | 9 - 6 = 3 | 3 | 3 |
| 7 | 9 - 7 = 2 | 3 | 4 |
| 8 | 9 - 8 = 1 | 4 | 4 |
| 9 | 9 - 9 = 0 | 4 | 5 |

Como se puede observar las tablas son muy similares, pero siguiendo las reglas del juego, respetando que cada jugador debe esperar el turno del otro y que no
 puede cambiar de ficha en mitad de la ronda, con menos de tres simbolos iguales es imposible hacer un tres en raya en cualquier dirección por lo cual es a 
 partir del turno 5 cuando tenemos suficientes fichas para poder cumplir el objetivo del juego.

Se observa que la cantidad de espacios vacios es la resta entre 9 y los turnos efectuados, también se observa que cuando la cantidad espacios vacios es un
 número par; el simbolo que empieza la ronda tiene una cantidad de repeticiones mayor por una unidad a su contraparte. Por el contrario, si es un número impar
 entonces el símbolo que empieza tiene la misma cantidad de repeticiones que su contraparte.

#### Definiendo operaciones de conteo y elementos totales

Dicho lo anterior la problemática se resume en que es una permitación con repetición de 3 elementos con una longitud de 9 y dependiendo de la cantidad de turnos y de espacios vacios 
 nos será útil una operacion u otra.

Ya que en cuanto a uso de elementos y a fines prácticos es lo mismo (_matemáticamente hablando_) tener 4 espacios en blanco, 3 equis y 2 circulos que tener 4 espacios en blanco, 3 circulos y 2 equis, cada
 operación con espacios vacios pares será multiplicada por 2.
<center>

__Para turnos de 5__

$$ {PR}_9^{4,3,2} = ( \frac{9!}{4! . 3! . 2!}) \times 2 = 2,520 $$

__Para turnos de 6__

$$ {PR}_9^{3,3,3} = \frac{9!}{3! . 3! . 3!} = 1,680 $$

__Para turnos de 7__ 

$$ {PR}_9^{2,4,3} = ( \frac{9!}{2! . 4! . 3!}) \times 2 = 2,520 $$

__Para turnos de 8__

$$ {PR}_9^{1,4,4} = \frac{9!}{1! . 4! . 4!} = 630 $$

__Para turnos de 9__

$$ {PR}_9^{5,4} = ( \frac{9!}{5! . 4!}) \times 2 = 252 $$

</center>

Estos conteos incluyen todos las configuraciones posibles, incluyendo aquellas en las que existen dos ganadores, en las que un jugador gana dos veces o en las que se produce un juego sin terminar, por lo
que estos casos serán seleccionados y apartados mediante algoritmos computacionales.

## Configuración opuesta

Por cada configuración existe una denominada opuesta. Dicha configuración consiste en intercambiar todos los 1 por 2 y todos los 2 por uno, 
 dando lugar a una nueva configuración en las que existen más círculos que X y viceversa.

Ejemplo:
> Para la configuración: [ 1, 1, 1, 2, 2, 0, 0, 0, 0 ]
> 
> Existe la configuración [ 2, 2, 2, 1, 1, 0, 0, 0, 0 ]
>      
>       | X | X | X |         | O | O | O |
>       |---|---|---|         |---|---|---|
>       | O | O |   |         | X | X |   |
>       |---|---|---|         |---|---|---|
>       |   |   |   |         |   |   |   |