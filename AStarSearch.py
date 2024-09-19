from Graph import Graph

class AStarSearch:
    def __init__(self, graph, start_node, goal_node, ui_callback=None):
        self.graph = graph
        self.start_node = start_node
        self.goal_node = goal_node
        self.ui_callback = ui_callback  # Callback para actualizar la interfaz en cada iteración

    def a_star(self):
        open_set = {self.start_node}
        came_from = {}

        # g_score: Distancia desde el nodo inicial
        g_score = {node: float('inf') for node in self.graph.nodes}
        g_score[self.start_node] = 0

        # f_score: g_score + heurística
        f_score = {node: float('inf') for node in self.graph.nodes}
        f_score[self.start_node] = self.graph.heuristic(self.start_node, self.goal_node)

        iteration = 0
        while open_set:
            iteration += 1
            current = min(open_set, key=lambda node: f_score[node])

            if current == self.goal_node:
                if self.ui_callback:
                    self.ui_callback(f"Iteración {iteration}: Nodo actual {current}, Nodos abiertos: {open_set}\n")
                return self.reconstruct_path(came_from)

            open_set.remove(current)

            for neighbor, weight in self.graph.neighbors(current):
                tentative_g_score = g_score[current] + weight

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.graph.heuristic(neighbor, self.goal_node)

                    if neighbor not in open_set:
                        open_set.add(neighbor)

            if self.ui_callback:
                self.ui_callback(f"Iteración {iteration}: Nodo actual {current}, Open set: {open_set}\n")

        if self.ui_callback:
            self.ui_callback("No se encontró ninguna ruta.\n")
        return None

    def reconstruct_path(self, came_from):
        current = self.goal_node
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path