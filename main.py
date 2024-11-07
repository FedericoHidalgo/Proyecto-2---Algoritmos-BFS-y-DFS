from generadorAlgoritmos import *

i = 4
nodoFuente = 7
g = modeloMalla(i, i)
nombreArchivo = "Malla " + str(i*i) + " nodos"
#Generamos el archivo .gv
g.graphViz(nombreArchivo)

x = BFS(g, nodoFuente)
nombreArchivo = "Arbol " + str(i*i) + " nodos"
x.graphViz(nombreArchivo)
