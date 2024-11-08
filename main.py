from generadorAlgoritmos import *
from generadorModelos import *


#Numero de muestras que se graficaran por modelo
numNodos = [30, 100, 500]
#Matriz para el modelo malla
matriz = {30:[6, 5], 100: [10, 10], 500: [25, 20]}
#Nodo Fuente para crear el arbol
nodoFuente = 10

"""
Modelo Malla
"""
for i in numNodos:    
    modelo = modeloMalla(matriz[i][0], matriz[i][1])
    nombreArchivo = "Malla " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)
    """
    BFS
    """
    arbol = BFS(modelo, nodoFuente)
    nombreArchivo = "Arbol " + str(i) + " nodos"
    #Generamos el archivo .gv
    arbol.graphViz(nombreArchivo)



"""
#Generamos el modelo Malla para 30 nodos
modelo = modeloMalla(6, 5)
nombreArchivo = "Malla " + str(30) + " nodos"
#Generamos el archivo .gv
modelo.graphViz(nombreArchivo)

#Generamos el modelo Malla para 100 nodos
modelo = modeloMalla(10, 10)
nombreArchivo = "Malla " + str(100) + " nodos"
#Generamos el archivo .gv
modelo.graphViz(nombreArchivo)

#Generamos el modelo para 500 nodos
modelo = modeloMalla(25, 20)
nombreArchivo = "Malla " + str(500) + " nodos"
#Generamos el archivo .gv
modelo.graphViz(nombreArchivo)
"""
#
"""
#Modelo Erdos - Renyi
for i in numNodos:
    #Generamos el modelo para 30, 100 y 500 nodos
    modelo = modeloErdosRenyi(i, i-1)
    nombreArchivo = "Erdos-Renyi " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)

#Modelo Gilbert
p = 0.1
#Damos una probabilidad de 0.1 para la conexión de nodos
for i in numNodos:
    #Generamos el modelo para 30, 100 y 500 nodos
    modelo = modeloGilbert(p, i)
    nombreArchivo = "Gilbert "  + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)

#Modelo Geografico Simple
r = 0.1 #Distancia máxima entre nodos
for i in numNodos:
    #Generamos el modelo para 30, 100 y 500 nodos
    modelo = modeloGeograficoSimple(i, r)
    nombreArchivo = "GeograficoSimple " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)

#Modelo Barabasi-Albert
d = 8 #Número máximo de conexiones por vertice
for i in numNodos:
    #Generamos el modelo para 30, 100 y 500 nodos
    modelo = modeloBarabasiAlbert(i, d)
    nombreArchivo = "Barabasi-Albert " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)

for i in numNodos:
    #Generamos el modelo para 30, 100 y 500 nodos
    modelo = modeloDorogovtsevMendes(i)
    nombreArchivo = "Dorogovtsev-Mendes " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)
"""
#BFS
"""
i = 4
nodoFuente = 7
g = modeloMalla(i, i)
nombreArchivo = "Malla " + str(i*i) + " nodos"
#Generamos el archivo .gv
g.graphViz(nombreArchivo)

x = BFS(g, nodoFuente)
nombreArchivo = "Arbol " + str(i*i) + " nodos"
x.graphViz(nombreArchivo)
"""
#DFS RECURSIVO
"""
#Creamos el objeto del nuevo grafo DFS
G= Grafo()
#Crewamos el modelo de donde se obtendra el arbol
i = 4
nodoFuente = 6
g = modeloMalla(i, i)

descubierto = {}                    #Diccionario para indicar si el nodo ya fue descubierto
#Obtenemos los nodos generados en el modelo
nodoGrafo = g.nodos.values()
#Para cada nodo v que pertenece al Grafo con v != nodoFuente
for u in nodoGrafo:
    descubierto[u] = False
    #Agregamos un nodo al arbol generado
    G.agregarNodo(u)

x = dfsRecursiva(g, nodoFuente, descubierto, G)

nombreArchivo = "Arbol " + str(i*i) + " nodos"
x.graphViz(nombreArchivo)
#####################


G= Grafo()
i = 5
j = 6
nodoFuente = 16
g = modeloMalla(i, j)

y = dfsIterativa(g, nodoFuente, G)

descubierto = {}                    #Diccionario para indicar si el nodo ya fue descubierto
#Obtenemos los nodos generados en el modelo
nodoGrafo = g.nodos.values()
#Para cada nodo v que pertenece al Grafo con v != nodoFuente
for u in nodoGrafo:
    descubierto[u] = False
    #Agregamos un nodo al arbol generado
    G.agregarNodo(u)

x = dfsRecursiva(g, nodoFuente, descubierto, G)

nombreArchivo = "Arbol iterativo " + str(i*i) + " nodos"
nombreArchivo2 = "Arbol recursivo" + str(i*i) + " nodos"
x.graphViz(nombreArchivo)
y.graphViz(nombreArchivo2)
"""