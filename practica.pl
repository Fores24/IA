%Practicas 3 IA - UAM --> PROLOG
%By: Guillermo Hoyo Bravo, Saul Almanza del Pie
%

% --------------------------FUNCIONES--GLOBALES-------------------------------%
%FUNCIONES COPIADAS DE PÁGINA - https://www.ic.unicamp.br/~meidanis/courses/mc336/2009s2/prolog/problemas/

% TAMAÑO DE UNA LISTA == FUNCION length(L,tam).
% L es una Lista
% N es el número de elementos de la lista
tam([],0).
tam([_|L],N) :- tam(L,N), N is N + 1.

% SACAR PENULTIMO ELEMENTO DE UNA LISTA
%
penultimo(X,[X,_]).
penultimo(X,[_,Y|Ys]) :- penultimo(X,[Y|Ys]).

% SACAR ELEMENTO K DE UNA LISTA
% X elemento a encontrar
% [X|L] = LISTA [X = Cabeza || L = Cola]
% K = Posición del elemento
element_at(X,[X|_],1).
element_at(X,[_|L],K) :- K > 1, K1 is K - 1, element_at(X,L,K1).

%NO PERTENECE
%
no_pertenece(X,[]).
no_pertenece(X,[Y|Ys]):- X\=Y, no_pertenece(X, Ys).

%----------------------------- - -.CABECERA.- - ----------------------------------%

write_log(S) :- open('error_logs.txt', append, Out), write(Out, S), write(Out, '\n'), close(Out).

/***************
* EJERCICIO 1. sum_pot_prod/4
*
*	ENTRADA:
*		X: Vector de entrada de numeros de valor real.
*		Y: Vector de entrada de numeros de valor real.
*		Potencia: Numero de valor entero, potencia.
*	SALIDA:
*		Resultado: Numero de valor real resultado de la operacion sum_pot_prod. 
*
****************/
sum_pot_prod(X, Y, Potencia, Resultado) :- print('Error. Este ejercicio no esta implementado todavia.'), !, fail.

sum_pot_prod(X,Y,P,R):- (P < 0, write("ERROR 1.1 Potencia"), fail); (tam(X,TX), tam(Y,TY), TX \= TY, write("ERROR 1.2 Longitud"), fail); (P == 0, R is 1, true); (eval(X, Y, P, R)).
%ESCRIBE EN BUCLE ERROR 1.1
%NO ESCRIBE ERROR 1.2 ni lo da!

%
%LINEAS DE ABAJO (eval(...)...) SON CLAVADAS A LAS SUYAS
%
eval([], [], _, 0).
eval([X|Xs], [Y|Ys], P, C):- sum_pot_prod(Xs, Ys, P, C1), C is C1 + (X*Y)^P.

%**************
% EJERCICIO 2. segundo_penultimo/3
%
%   ENTRADA:
%       L: Lista de entrada de numeros de valor real.
%   SALIDA:
%       X : Numero de valor real. Segundo elemento.
%       Y : Numero de valor real. Penultimo elemento.
%
%***************/

segundo_penultimo(L,X,Y):- (tam2(L,T),  (T < 2), write("ERROR 2.1 Longitud"), fail); (segundo(X,L), penultimo(Y,L)).
segundo(X,L):- N = 2, element_at(X, L, N).
%NO ESCRIBE ERROR 2.1 Longitud
%


%**************
% EJERCICIO 3. sublista/5
%
%   ENTRADA:
%       L: Lista de entrada de cadenas de texto.
%       Menor: Numero de valor entero, indice inferior.
%       Mayor: Numero de valor entero, indice superior.
%       E: Elemento, cadena de texto.
%   SALIDA:
%       Sublista: Sublista de salida de cadenas de texto.
%
%***************/
sublista(_, Menor, Mayor, _,_):- Menor > Mayor, write("ERROR 3.2 Indices"), fail.
sublista(L, _,Mayor,_, _):- tam(L,T), Mayor > T, write("ERROR 3.2 Indices"), fail.
sublista(L,_,_,E,_):- no_pertenece(E,L), write("ERROR 3.1 Elemento"), fail.

sublista(L, Menor, Mayor, E, Sublista).


%**************
% EJERCICIO 4. espacio_lineal/4
%
%   ENTRADA:
%       Menor: Numero de valor entero, valor inferior del intervalo.
%       Mayor: Numero de valor entero, valor superior del intervalo.
%       Numero_elementos: Numero de valor entero, numero de valores de la rejilla.
%   SALIDA:
%       Rejilla: Vector de numeros de valor real resultante con la rejilla.
%
%***************/

%**************
% EJERCICIO 5. normalizar/2
%
%   ENTRADA:
%       Distribucion_sin_normalizar: Vector de numeros reales de entrada. Distribucion sin normalizar.
%   SALIDA:
%       Distribucion: Vector de numeros reales de salida. Distribucion normalizada.
%
%***************/

%**************
% EJERCICIO 6. divergencia_kl/3
%
%   ENTRADA:
%       D1: Vector de numeros de valor real. Distribucion.
%       D2: Vector de numeros de valor real. Distribucion.
%   SALIDA:
%       KL: Numero de valor real. Divergencia KL.
%
%***************/


%**************
% EJERCICIO 7. producto_kronecker/3
%
%   ENTRADA:
%       Matriz_A: Matriz de numeros de valor real.
%       Matriz_B: Matriz de numeros de valor real.
%   SALIDA:
%       Matriz_bloques: Matriz de bloques (matriz de matrices) de numeros reales.
%
%***************/

%**************
% EJERCICIO 8a. distancia_euclidea/3
%
%   ENTRADA:
%       X1: Vector de numeros de valor real.
%       X2: Vector de numeros de valor real.
%   SALIDA:
%       D: Numero de valor real. Distancia euclidea.
%
%***************/

%**************
% EJERCICIO 8b. calcular_distancias/3
%
%   ENTRADA:
%       X_entrenamiento: Matriz de numeros de valor real donde cada fila es una instancia representada por un vector.
%       X_test: Matriz de numeros de valor real donde cada fila es una instancia representada por un vector. Instancias sin etiquetar.
%   SALIDA:
%       Matriz_resultados: Matriz de numeros de valor real donde cada fila es un vector con la distancia de un punto de test al conjunto de entrenamiento X_entrenamiento.
%
%***************/

%**************
% EJERCICIO 8c. predecir_etiquetas/4
%
%   ENTRADA:
%       Y_entrenamiento: Vector de valores alfanumericos de una distribucion categorica. Cada etiqueta corresponde a una instancia de X_entrenamiento.
%       K: Numero de valor entero.
%       Matriz_resultados: Matriz de numeros de valor real donde cada fila es un vector con la distancia de un punto de test al conjunto de entrenamiento X_entrenamiento.
%   SALIDA:
%       Y_test: Vector de valores alfanumericos de una distribucion categorica. Cada etiqueta corresponde a una instancia de X_test.
%
%***************/

%**************
% EJERCICIO 8d. predecir_etiqueta/4
%
%   ENTRADA:
%       Y_entrenamiento: Vector de valores alfanumericos de una distribucion categorica. Cada etiqueta corresponde a una instancia de X_entrenamiento.
%       K: Numero de valor entero.
%       Vec_distancias: Vector de valores reales correspondiente a una fila de Matriz_resultados.
%   SALIDA:
%       Etiqueta: Elemento de valor alfanumerico.
%
%***************/

%**************
% EJERCICIO 8e. calcular_K_etiquetas_mas_relevantes/4
%
%   ENTRADA:
%       Y_entrenamiento: Vector de valores alfanumericos de una distribucion categorica. Cada etiqueta corresponde a una instancia de X_entrenamiento.
%       K: Numero de valor entero.
%       Vec_distancias: Vector de valores reales correspondiente a una fila de Matriz_resultados.
%   SALIDA:
%       K_etiquetas: Vector de valores alfanumericos de una distribucion categorica.
%
%***************/

%**************
% EJERCICIO 8f. calcular_etiqueta_mas_relevante/2
%
%   ENTRADA:
%       K_etiquetas: Vector de valores alfanumericos de una distribucion categorica.
%   SALIDA:
%       Etiqueta: Elemento de valor alfanumerico.
%
%***************/

%**************
% EJERCICIO 8g. k_vecinos_proximos/5
%
%   ENTRADA:
%       X_entrenamiento: Matriz de numeros de valor real donde cada fila es una instancia representada por un vector.
%       Y_entrenamiento: Vector de valores alfanumericos de una distribucion categorica. Cada etiqueta corresponde a una instancia de X_entrenamiento.
%       K: Numero de valor entero.
%       X_test: Matriz de numeros de valor real donde cada fila es una instancia representada por un vector. Instancias sin etiquetar.
%   SALIDA:
%       Y_test: Vector de valores alfanumericos de una distribucion categorica. Cada etiqueta corresponde a una instancia de X_test.
%
%***************/
