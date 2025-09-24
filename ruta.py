# Sistema Inteligente de Rutas

# Se define la base de conocimiento como un conjunto de reglas lógicas
# Cada regla conecta dos estaciones con un costo (distancia, tiempo o número de estaciones)
conexiones = [
    ("A", "B", 5),   # Regla: de A a B con costo 5
    ("A", "C", 2),   
    ("B", "D", 4),  
    ("C", "D", 7),   
    ("C", "E", 3),   
    ("D", "F", 1),   
    ("E", "F", 5),   
]

# Se construye un grafo a partir de las reglas anteriores
# El grafo se representa como un diccionario donde cada nodo tiene sus vecinos
grafo = {}
for origen, destino, costo in conexiones:
    grafo.setdefault(origen, []).append((destino, costo))   # Se agrega conexión origen → destino
    grafo.setdefault(destino, []).append((origen, costo))   # Se agrega conexión destino → origen (es bidireccional)


# Se importa heapq, que permite usar colas de prioridad para aplicar el algoritmo de Dijkstra
import heapq

# Ahora se define la función que encuentra la mejor ruta usando Dijkstra
def mejor_ruta(origen, destino):
    # Se crea una cola de prioridad que guarda (costo acumulado, nodo actual, camino recorrido)
    cola = [(0, origen, [origen])]
    # Se usa un conjunto para guardar los nodos ya visitados y evitar ciclos
    visitados = set()

    # Mientras haya elementos en la cola de prioridad seguimos explorando
    while cola:
        # Extraemos el nodo con menor costo acumulado hasta ahora
        costo_actual, nodo, camino = heapq.heappop(cola)

        # Si ya se visitó este nodo lo saltamos
        if nodo in visitados:
            continue
        # Se marca el nodo como visitado
        visitados.add(nodo)

        # Si llegamos al destino devuelve el costo y el camino completo
        if nodo == destino:
            return costo_actual, camino

        # Se recorre los vecinos del nodo actual
        for vecino, costo in grafo.get(nodo, []):
            # Si el vecino no ha sido visitado, se agrega a la cola con el nuevo costo
            if vecino not in visitados:
                heapq.heappush(cola, (costo_actual + costo, vecino, camino + [vecino]))
    
    # Si no existe una ruta posible, se vuelve a None
    return None


# Ejecución de prueba del sistema inteligente

# Se define el punto de inicio y destino
origen = "A"
destino = "F"

# Llamamos a la función para calcular la mejor ruta
resultado = mejor_ruta(origen, destino)

# Mostramos el resultado obtenido
if resultado:
    costo, ruta = resultado
    print(f"Mejor ruta de {origen} a {destino}: {' -> '.join(ruta)} (Costo total del recorrido: {costo})")
else:
    print("No existe ruta posible.")