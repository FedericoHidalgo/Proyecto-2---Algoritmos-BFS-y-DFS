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
    G = Grafo()     #GenerarAristas para el arbol
    L = {}      #Diccionario de capas del arbol
    contCapa = 0    #Contador de capa
    descubierto = {}    #Diccionario para indicar si el nodo ya fue descubierto
    nodoFuente = modelo.nodos.get(s)  #Nodo Fuente
    nodosCapa = []     #Lista donde se almacenan los nodos de cada capa
    nodosSiguientes = []    #Lista que almacena los nodos de la siguiente capa
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
    #Mientras las capas no permanezcan vacias
    while L.get(contCapa)  != []:
        nodosCapa = L.get(contCapa)
        #Asignamos una cadena vacia a la capa siguiente
        L[contCapa + 1] = []
        #Para cada nodo perteneciente a la capa, se agrega al diccionario
        for u in nodosCapa:
            print("Nodo: ", u)
            nodosIncidentes = nodosDeArista(modelo, u)
            print("Nodos incidentes: ", nodosIncidentes)
            for v in nodosIncidentes:
                if descubierto.get(str(v)) == False:
                    descubierto[str(v)] = True
                    #Añadir v a las capas
                    nodosSiguientes.append(v)
            L[contCapa + 1] = nodosSiguientes
            print("Capa actual: ", L[contCapa])
            print("Capa siguiente: ", L[contCapa + 1])
        #contCapa += 1
    print("Encontrado: ", descubierto)
    return True

def dfsRecursiva(self, s):
    """
    Búsqueda en Profundidad
    Genera un Arbol a partir de un Grafo. Recorriendo todos los
    nodos desde sde manera ordenada pero no uniforme.
    Se generta de forma recursiva.
    """
    aristasConectadas = self.aristas.values()
    print("Aristas conectadas: ")
    for i in aristasConectadas:
        x = i.split(' -> ', 1)
        if x[0] == nodoFuente or x[1] == nodoFuente:
            G.agregarArista(x[0], x[1], ' - ')

    print("Aristas: ", G.aristas.values())
    return True

def dfsIterativa(self, s):
    """
    Búsqueda en Profundidad
    Genera un Arbol a partir de un Grafo. Recorriendo todos los
    nodos desde s de manera ordenada pero no uniforme.
    Se generta de forma iterativa.
    """
    return True

i = 3
nodoFuente = 4
g = modeloMalla(i, i)
x = BFS(g, nodoFuente)
print(x)
