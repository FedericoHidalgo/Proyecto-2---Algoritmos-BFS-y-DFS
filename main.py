from generadorAlgoritmos import *
"""
BFS
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
DFS RECURSIVO
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