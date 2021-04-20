%Practicas 3 IA - UAM --> PROLOG
%By: Guillermo Hoyo Bravo, Saul Almanza del Pie

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
sum_pot_prod(_,_,P,_):- P < 0, print("ERROR 1.1 Potencia"), !, fail.
sum_pot_prod(X,Y,_,_):- length(X,TX), length(Y,TY), TX \= TY, write_log("ERROR 1.2 Longitud"), print("ERROR 1.2 Longitud"), !, fail.
sum_pot_prod(_,_,P,R):- P == 0, R is 1.
sum_pot_prod([],[],_,0).
sum_pot_prod([X|Xs], [Y|Ys], P, C):- sum_pot_prod(Xs, Ys, P, C1), C is C1 + (X*Y)^P.

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

segundo_penultimo(L,_,_):- length(L,T),  (T < 2), write_log("ERROR 1.2 Longitud"), print("ERROR 2.1 Longitud"), !, fail.
segundo_penultimo(L,X,Y):-(segundo(X,L), penultimo(Y,L)).
segundo(X,L):- N = 2, element_at(X, L, N).
% SACAR PENULTIMO ELEMENTO DE UNA LISTA
penultimo(X,[X,_]).
penultimo(X,[_,Y|Ys]) :- penultimo(X,[Y|Ys]).
% SACAR ELEMENTO K DE UNA LISTA
element_at(X,[X|_],1).
element_at(X,[_|L],K) :- K > 1, K1 is K - 1, element_at(X,L,K1).

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
sublista(_, Menor, Mayor, _,_):- Menor > Mayor, write_log("ERROR 3.2 Indices"), print("ERROR 3.2 Indices"), !, fail.
sublista(L, _,Mayor,_, _):- length(L,T), Mayor > T, write_log("ERROR 3.2 Indices"), print("ERROR 3.2 Indices"), !, fail.
sublista(L,_,_,E,_):- no_pertenece(E,L), write_log("ERROR 3.1 Indices"), print("ERROR 3.1 Elemento"), !, fail.

%NO PERTENECE
no_pertenece(_,[]).
no_pertenece(X,[Y|Ys]):- X\=Y, no_pertenece(X, Ys).
%No hemos tenido tiempo a implementar el Ejercicio.


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

espacio_lineal(Menor,Mayor,_,_):- Menor > Mayor, write_log("ERROR 4.1 Indices"), print("ERROR 4.1 Indices"), !, fail.
espacio_lineal(_,_,1,_):- !.
espacio_lineal(Menor,Mayor,Numero_elementos,[Menor|Rejilla]):- Num is Numero_elementos-1,
    Aux is Menor+((Mayor-Menor)/Num),
    espacio_lineal(Aux,Mayor,Num,Rejilla).


%**************
% EJERCICIO 5. normalizar/2
%
%   ENTRADA:
%       Distribucion_sin_normalizar: Vector de numeros reales de entrada. Distribucion sin normalizar.
%   SALIDA:
%       Distribucion: Vector de numeros reales de salida. Distribucion normalizada.
%
%***************/

sum_lista([X|_], _):- X < 0, write_log("ERROR 5.1 Negativos"), print("ERROR 5.1 Negativos"), !, fail.
sum_lista([], 0).
sum_lista([X|Xs], R):- sum_lista(Xs, R2), R is R2 + X.
normalizar(ENTRADA,SALIDA):- sum_lista(ENTRADA, R),  divide_elementos(ENTRADA,R,SALIDA), !.
divide_elementos([],_,[]):-!.
divide_elementos([X|L],R,[Y|SALIDA]):- Y is (X/R), divide_elementos(L,R,SALIDA).

% Control de er

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
%
log_lista([X|_], _, _):- X < 0, write_log("ERROR 6.1 Negativos"), print("ERROR 6.1 Negativos"), !, fail.
log_lista(_,[Y|_], _):- Y < 0, write_log("ERROR 6.1 Negativos"), print("ERROR 6.1 Negativos"), !, fail.
log_lista([],[],0):- !.
log_lista([X|Xs], [Y|Ys], R):- log_lista(Xs, Ys, R2), R is R2 + X*log(X/Y), !.
divergencia(D1,D2,KL):- log_lista(D1, D2, KL), !.

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
