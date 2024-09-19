from Graph import Graph
from AStarSearch import AStarSearch

def main():
    # Ejemplo de grafo en forma matricial
    graph_matrix = [
        [0, 1, 0, 0, 0],  # Conexiones desde 'A'
        [1, 0, 2, 5, 0],  # Conexiones desde 'B'
        [0, 2, 0, 0, 0],  # Conexiones desde 'C'
        [0, 5, 0, 0, 1],  # Conexiones desde 'D'
        [0, 0, 0, 1, 0]   # Conexiones desde 'E'
    ]

    # Lista de etiquetas de los nodos
    node_labels = ['A', 'B', 'C', 'D', 'E']

    start_node = 'A'
    goal_node = 'E'

    # Crear el grafo con etiquetas de nodos
    graph = Graph(graph_matrix, node_labels)

    # Realizar la búsqueda A*
    search = AStarSearch(graph, start_node, goal_node)
    search.a_star()

if __name__ == "__main__":
    main()