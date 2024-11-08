from generadorGrafos import Grafo
from generadorModelos import *
import random

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

def nodosVisitados(diccionario, lista):
    """
    Regresa True si todos los nodos ya han sido marcados como visitados,
    regresa False si existen nodos sin visitar en la lista
    """
    for i in lista:
        if diccionario.get(i) != True:
            return False
    return True
        

def BFS(modelo, s):
    """
    Búsqueda a lo Ancho
    Genera un Arbol a partir de un Grafo. Explora desde s 
    en todas las direcciones posibles agregando nodos una capa a la ves.
    self -> Modelo de Grafo
    """
    print("Iniciando BFS")
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

def getDfsRecursiva(modelo, s):
    """
    Método de apoyo para generar un arbol por busqueda a lo largo
    DFS Recursiva
    """
    print("Iniciando DFS Recursiva")
    g = Grafo()
    descubierto = {}                    #Diccionario para indicar si el nodo ya fue descubierto
    #Obtenemos los nodos generados en el modelo
    nodoGrafo = modelo.nodos.values()
    #Para cada nodo v que pertenece al Grafo con v != nodoFuente
    for u in nodoGrafo:
        descubierto[u] = False
        #Agregamos un nodo al arbol generado
        g.agregarNodo(u)
    arbol = dfsRecursiva(modelo, s, descubierto, g)
    return arbol
    


def dfsIterativa(modelo, s):
    """
    Búsqueda en Profundidad
    Genera un Arbol a partir de un Grafo. Recorriendo todos los
    nodos desde s de manera ordenada pero no uniforme.
    Se genera de forma iterativa.
    s - nodo fuente
    modelo - Grafo a evaluar
    g - nuevo grafo generado
    """
    print("Iniciando DFS Iterativa")
    g = Grafo()
    s = modelo.nodos.get(int(s))             #Nodo fuente
    #Si el nodo fuente no existe, termina el proceso
    if s == None:
        print("El nodo no pertenece al modelo")
        return False
    descubierto = {}    #Diccionario para indicar si el nodo ya fue descubierto
    #El primer nodo descubierto es el nodo Fuente
    descubierto[s] = True
    g.agregarNodo(s)
    #Obtenemos los nodos generados en el modelo
    nodoGrafo = modelo.nodos.values()
    #Para cada nodo v que pertenece al Grafo con v != nodoFuente
    for i in nodoGrafo:        
        if i != str(s):
            descubierto[i] = False
            g.agregarNodo(i)
    #Iteración principal, termina cuando todos los nodos fueron recorridos
    while(nodosVisitados(descubierto, nodoGrafo) != True):
        #Nodos vecinos de s
        nodosIncidentes = nodosDeArista(modelo, str(s))
        #Se recorren los nodos vecinos en busqueda de crear una arista
        for i in nodosIncidentes:
            #Al encontrar el primer nodo sin conexión se crea una arista
            if descubierto.get(i) != True:
                g.agregarArista(s, i, ' -> ')
                descubierto[i] = True
                #La punta del arbol sera nuestro nuevo nodo fuente y regresa a while
                s = i                
                break
            #Si ya no existen nodos vecinos disponibles
            elif nodosVisitados(descubierto, nodosIncidentes) == True:
                #Si aun quedan nodos del grafo sin conectar
                if nodosVisitados(descubierto, nodoGrafo) != True:
                    #Recorremos la lista de grafos en busqueda de nodos sin conexión
                    #La busqueda es de atras a adelante
                    for j in reversed(nodoGrafo):
                        #Nodo sin conexión descubierto
                        if descubierto[str(j)] != True:
                            descubierto[j] = True
                            #Localizamos sus nodos vecinos
                            nVecino = nodosDeArista(modelo, str(j))
                            #Lo conectamos con el vecino que forme parte de la rama principal
                            for k in nVecino:
                                if descubierto[k] == True:
                                    g.agregarArista(j, k, ' -> ')
                                    s = j
                                    #Nueva punta del arbol
                                #Ciclo de busqueda de vecinos
                                break
                            #Ciclo de busqueda de nodos sin conectar en inversa
                            break
                #Break del for principal
                break

    return g