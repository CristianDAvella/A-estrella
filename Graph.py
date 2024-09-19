class Graph:
    def __init__(self, matrix, labels):
        self.matrix = matrix
        self.nodes = labels  # Lista de etiquetas, p. ej. ['A', 'B', 'C', ...]

    def heuristic(self, node1, node2):
        # Calculamos la heurística usando los índices de las etiquetas
        index1 = self.nodes.index(node1)
        index2 = self.nodes.index(node2)
        return abs(index1 - index2)
    
    def neighbors(self, node):
        # Devuelve los vecinos de un nodo basado en la matriz de adyacencia
        index = self.nodes.index(node)
        neighbors = []
        for i, weight in enumerate(self.matrix[index]):
            if weight > 0:  # Hay conexión con peso positivo
                neighbors.append((self.nodes[i], weight))
        return neighbors