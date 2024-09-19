import tkinter as tk
from tkinter import messagebox
from Graph import Graph
from AStarSearch import AStarSearch

class AStarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Búsqueda A* - Interfaz Gráfica")

        # Etiquetas y campos de entrada
        self.graph_label = tk.Label(root, text="Matriz de adyacencia (separada por comas):")
        self.graph_label.pack()
        self.graph_entry = tk.Entry(root, width=50)
        self.graph_entry.pack()

        self.labels_label = tk.Label(root, text="Etiquetas de nodos (separadas por comas):")
        self.labels_label.pack()
        self.labels_entry = tk.Entry(root, width=50)
        self.labels_entry.pack()

        self.start_label = tk.Label(root, text="Nodo inicial:")
        self.start_label.pack()
        self.start_entry = tk.Entry(root, width=5)
        self.start_entry.pack()

        self.goal_label = tk.Label(root, text="Nodo objetivo:")
        self.goal_label.pack()
        self.goal_entry = tk.Entry(root, width=5)
        self.goal_entry.pack()

        # Botón para ejecutar la búsqueda
        self.search_button = tk.Button(root, text="Buscar Ruta", command=self.run_a_star)
        self.search_button.pack()

        # Campo de resultado
        self.result_label = tk.Label(root, text="Resultado:")
        self.result_label.pack()
        self.result_text = tk.Text(root, height=15, width=60)
        self.result_text.pack()

    def parse_matrix(self, matrix_str):
        try:
            matrix = []
            rows = matrix_str.strip().split(';')
            for row in rows:
                matrix.append([int(x) for x in row.split(',')])
            return matrix
        except ValueError:
            messagebox.showerror("Error", "Formato de matriz inválido.")
            return None

    def parse_labels(self, labels_str):
        return [label.strip() for label in labels_str.split(',')]

    def update_ui(self, message):
        """Callback para actualizar la interfaz con los resultados de cada iteración."""
        self.result_text.insert(tk.END, message)
        self.result_text.see(tk.END)  # Desplazar automáticamente al final

    def run_a_star(self):
        # Obtener los valores de los campos de entrada
        matrix_str = self.graph_entry.get()
        labels_str = self.labels_entry.get()
        start_node = self.start_entry.get().strip()
        goal_node = self.goal_entry.get().strip()

        # Parsear la matriz y las etiquetas
        matrix = self.parse_matrix(matrix_str)
        labels = self.parse_labels(labels_str)

        # Validar si se ha ingresado todo correctamente
        if matrix is None or not labels or not start_node or not goal_node:
            messagebox.showerror("Error", "Por favor, completa todos los campos correctamente.")
            return

        if start_node not in labels or goal_node not in labels:
            messagebox.showerror("Error", "Nodos de inicio u objetivo inválidos.")
            return

        # Limpiar el campo de texto antes de mostrar los resultados
        self.result_text.delete(1.0, tk.END)

        # Crear el grafo y ejecutar la búsqueda A*
        graph = Graph(matrix, labels)
        search = AStarSearch(graph, start_node, goal_node, ui_callback=self.update_ui)
        path = search.a_star()

        # Mostrar el resultado final en la interfaz
        if path:
            self.result_text.insert(tk.END, f"\nRuta encontrada: {' -> '.join(path)}\n")
        else:
            self.result_text.insert(tk.END, "\nNo se encontró ninguna ruta.\n")

# Función principal para iniciar la interfaz
def main():
    root = tk.Tk()
    app = AStarApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()