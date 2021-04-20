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

%EJERICIO 1 - Producto, Potencua, Sumatorio --> sum_pot_prod/4
%sum_pot_prod(X, Y, P, R)
%    X = Lista Numérica
%    Y = Lista Numérica
%    P = Potencia
%    R = Resultado
%
%    Enunciado: Multiplicar terminos de cada lista, elevar esos número a
%    P y sumarlos para obtener R.
%

sum_pot_prod(X,Y,P,R):- (P < 0, write("ERROR 1.1 Potencia"), fail); (tam(X,TX), tam(Y,TY), TX \= TY, write("ERROR 1.2 Longitud"), fail); (P == 0, R is 1, true); (eval(X, Y, P, R)).
%ESCRIBE EN BUCLE ERROR 1.1
%NO ESCRIBE ERROR 1.2 ni lo da!

%
%LINEAS DE ABAJO (eval(...)...) SON CLAVADAS A LAS SUYAS
%
eval([], [], _, 0).
eval([X|Xs], [Y|Ys], P, C):- sum_pot_prod(Xs, Ys, P, C1), C is C1 + (X*Y)^P.


%EJERCICIO 2 - Segundo y Penultimo de la Lista --> segundo_penultimo/3
%segundo_penultimo(L,X,Y)
%    L es la Lista para extrar los elementos
%    X es el segundo número de la lista
%    Y es el penúltimo número de la lista
%

segundo_penultimo(L,X,Y):- (tam2(L,T),  (T < 2), write("ERROR 2.1 Longitud"), fail); (segundo(X,L), penultimo(Y,L)).
segundo(X,L):- N = 2, element_at(X, L, N).
%NO ESCRIBE ERROR 2.1 Longitud
%

%EJERCICIO 3 - Sublista que contiene un Elemento --> sublista/5
%Sublista(L, Menor, Mayor, E, Sublista)
%    L = Lista de numeros
%    Menor = Indice menor a buscar en L
%    Mayor = Indice mayor a buscar en L
%    E = Elemento dado
%    Sublista = Resultado de L
%
%Crear sublista desde indice menor al mayor.
%
sublista(_, Menor, Mayor, _,_):- Menor > Mayor, write("ERROR 3.2 Indices"), fail.
sublista(L, _,Mayor,_, _):- tam(L,T), Mayor > T, write("ERROR 3.2 Indices"), fail.
sublista(L,_,_,E,_):- no_pertenece(E,L), write("ERROR 3.1 Elemento"), fail.

sublista(L, Menor, Mayor, E, Sublista).




%EJERCICIO 4 - Determina el espacio Lineal --> espacio_lineal/4
%Espacio_lineal(Mayor, Menor, N, Rejilla)
%    Menor, Mayor = Indices superiores e inferiores donde se despliega
%    el espacio lineal
%    N = Numero de valores en las regíllas
%    Rejilla = Lista de números del Espacio Lineal
%







%EJERCICIO 5 - Normalizarción de listas --> normalizar/2
%Normalizar(Distribucion_sin_Normalizar, Distribucion_Nomalizada).
%    Distribucion_sin_Normalizar = Lista de Número a Normalizar
%    Distribucion_Normalizada = Lista de Números Normalziados
%
%    No pueden ser negativos
%

%EJERCICIO 6 - Divergencia --> divergencia_k1/3
%Divergencia_k1(D1,D2,KL)
%    D1 = Lista de números
%    D2 = Lista de números
%    KL =
%
