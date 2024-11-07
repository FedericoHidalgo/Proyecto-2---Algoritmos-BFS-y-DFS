from generadorGrafos import Grafo
from generadorModelos import *

nodosDeAristas = {}

def nodosDeArista(self, nodo):
    """
    Método que obtiene los nodos adyacentes a un nodo de interes
    Asignar un método de gteneración de grafo
    nodo -> nodo de interes
    """
    #Obtenemos las aristas generadas en el modelo
    aristaGrafo = self.aristas.values()
    #Generar una lista de nodos conectados por la arista
    n1 = []
    #Obtenemos el segundo nodo unido a la arista
    for i in aristaGrafo:
        #Obtenemos los nodos (u, v)        
        n2 = i.split(' -> ', 1)
        if str(n2[0]) == nodo:       #Obtenemos el segundo nodo
            n1.append(n2[1])
        elif str(n2[1]) == nodo:     #Obtenemos el segundo nodo
            n1.append(n2[0])
    #Retornamos la lista de nodos adyacentes
    return n1

def BFS(modelo, s):
    """
    Búsqueda a lo Ancho
    Genera un Arbol a partir de un Grafo. Explora desde s 
    en todas las direcciones posibles agregando nodos una capa a la ves.
    self -> Modelo de Grafo
    """
    G = Grafo()         #GenerarAristas para el arbol
    L = {}              #Diccionario de capas del arbol
    contCapa = 0        #Contador de capa
    descubierto = {}    #Diccionario para indicar si el nodo ya fue descubierto
    nodoFuente = modelo.nodos.get(s)    #Nodo Fuente
    nodosCapa = []                      #Lista donde se almacenan los nodos de cada capa
    nodosSiguientes = []                #Lista que almacena los nodos de la siguiente capa
    #Si el nodo fuente no existe, termina el proceso
    if nodoFuente == None:
        print("El nodo Fuente no pertenece al modelo")
        return False
    #El primer nodo descubierto es el nodo Fuente
    descubierto[nodoFuente] = True
    #Obtenemos los nodos generados en el modelo
    nodoGrafo = modelo.nodos.values()
    #Para cada nodo v que pertenece al Grafo con v != nodoFuente
    for i in nodoGrafo:        
        if i != str(nodoFuente):
            descubierto[i] = False
    #La capa cero es el nodo fuente
    L[0] = [nodoFuente]
    while L.get(contCapa)  != []:
        #Variable auxiliar para almacenar valores en diccionario de capas
        capaSiguiente = contCapa + 1
        #Obtenemos los nodos que conforman la capa actual
        nodosCapa = L.get(contCapa)
        #Asignamos una cadena vacia a la capa siguiente
        L[capaSiguiente] = []
        #Para cada nodo perteneciente a la capa, se agrega al diccionario+
        for u in nodosCapa:
            #Se agrega un nodo al archivo .gv
            G.agregarNodo(u)
            #Obtenemos los vecinos de u en cada ciclo
            nodosIncidentes = nodosDeArista(modelo, u)
            #Recorremos los nodos vecinos en busqueda de nodos no explorados
            for v in nodosIncidentes:
                #Si un nodo fue descubierto se marca como explorado y se añade a
                #la lista de nodos de la siguiente capa
                if descubierto.get(str(v)) == False:
                    descubierto[str(v)] = True
                    #Añadir v a las capas
                    nodosSiguientes.append(v) 
                    #Agregamos una arista al archivo .gv
                    G.agregarArista(u, v, ' -> ')  
        #Añadimos al diccionario de capas los nodos de la siguiente capa             
        L[capaSiguiente] = nodosSiguientes
        #Vaciamos nuestra lista de nodos, para que pueda recibir los nuevos nodos
        nodosSiguientes = []
        #Aumentamos un digito a nuestra busqueda de capas
        contCapa += 1
    return G

def dfsRecursiva(modelo, s, listaExplorados, g):
    """
    Búsqueda en Profundidad
    Genera un Arbol a partir de un Grafo. Recorriendo todos los
    nodos desde s de manera ordenada pero no uniforme.
    s - nodo ancestro
    modelo - Grafo a evaluar
    g - nuevo grafo generado
    Se generta de forma recursiva.
    """
    s = modelo.nodos.get(int(s))             #Nodo ancentro
    #Si el nodo ancestro no existe, termina el proceso
    if s == None:
        print("El nodo no pertenece al modelo")
        return False
    descubierto = listaExplorados             #Diccionario para indicar si el nodo ya fue descubierto
    #Marcar s como explorado
    descubierto[s] = True
    #Obtenemos los vecions de u
    nodosIncidentes = nodosDeArista(modelo, s)
    #Recorremos los nodos en busqueda de los no explorados
    for v in nodosIncidentes:
        #Si v esta marcado como no explorado
        if descubierto.get(str(v)) == False:
            #Agregamos una arista al arbol generado
            g.agregarArista(s, v, ' -> ')
            #Invocar recursivamente DFS
            dfsRecursiva(modelo, v, listaExplorados, g)
    return g

def dfsIterativa(self, s):
    """
    Búsqueda en Profundidad
    Genera un Arbol a partir de un Grafo. Recorriendo todos los
    nodos desde s de manera ordenada pero no uniforme.
    Se generta de forma iterativa.
    """
    return True

G= Grafo()
i = 4
nodoFuente = 6
g = modeloMalla(i, i)

descubierto = {}                    #Diccionario para indicar si el nodo ya fue descubierto
#Obtenemos los nodos generados en el modelo
nodoGrafo = g.nodos.values()
#Para cada nodo v que pertenece al Grafo con v != nodoFuente
for u in nodoGrafo:
    descubierto[u] = False
    G.agregarNodo(u)

x = dfsRecursiva(g, nodoFuente, descubierto, G)

nombreArchivo = "Arbol " + str(i*i) + " nodos"
x.graphViz(nombreArchivo)