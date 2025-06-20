from uas import hill_climbing, indonesia_graph
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx

root = tk.Tk()
root.title("Pencarian Rute Optimal - Hill Climbing")

heuristic_values = {
    'Jakarta': 780, 'Bekasi': 760, 'Bandung': 730, 'Serang': 800,
    'Karawang': 710, 'Purwakarta': 690, 'Cimahi': 725, 'Garut': 700,
    'Tasikmalaya': 670, 'Banjar': 650, 'Ciamis': 640, 'Majalengka': 620,
    'Cirebon': 600, 'Tegal': 580, 'Pekalongan': 550, 'Semarang': 500,
    'Salatiga': 480, 'Boyolali': 470, 'Solo': 450, 'Sragen': 430,
    'Ngawi': 400, 'Madiun': 370, 'Nganjuk': 350, 'Kediri': 320,
    'Blitar': 290, 'Malang': 200, 'Surabaya': 0, 'Sidoarjo': 20,
    'Cilegon': 790
}

graph = nx.Graph(indonesia_graph)
pos = {
    'Jakarta': (0.1, 0.5),
    'Bekasi': (0.2, 0.5),
    'Bandung': (0.3, 0.4),
    'Serang': (0.05, 0.55),
    'Karawang': (0.25, 0.5),
    'Purwakarta': (0.3, 0.6),
    'Subang': (0.32, 0.62),
    'Cimahi': (0.35, 0.45),
    'Garut': (0.4, 0.4),
    'Tasikmalaya': (0.45, 0.35),
    'Banjar': (0.5, 0.3),
    'Ciamis': (0.52, 0.28),
    'Majalengka': (0.53, 0.33),
    'Cirebon': (0.55, 0.35),
    'Tegal': (0.6, 0.38),
    'Pekalongan': (0.65, 0.4),
    'Semarang': (0.7, 0.42),
    'Salatiga': (0.72, 0.37),
    'Boyolali': (0.75, 0.35),
    'Solo': (0.78, 0.33),
    'Sragen': (0.8, 0.3),
    'Ngawi': (0.83, 0.28),
    'Madiun': (0.85, 0.25),
    'Nganjuk': (0.87, 0.22),
    'Kediri': (0.89, 0.2),
    'Blitar': (0.91, 0.18),
    'Malang': (0.93, 0.15),
    'Surabaya': (0.97, 0.12),
    'Sidoarjo': (0.99, 0.1),
    'Cilegon': (0.0, 0.52),
}


def find_path():
    start = start_var.get()
    goal = goal_var.get()
    path = hill_climbing(indonesia_graph, start, goal, heuristic_values)

    ax.clear()
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color='skyblue',
            font_size=9, font_color='black', ax=ax)
    ax.set_title("Peta Kota Indonesia (Pulau Jawa)")

    if path:
        nx.draw_networkx_nodes(graph, pos, nodelist=path, node_color='orange', node_size=700, ax=ax)
        nx.draw_networkx_edges(graph, pos, edgelist=[(path[i], path[i + 1]) for i in range(len(path) - 1)],
                               width=3, edge_color='red', ax=ax)

    canvas.draw()

input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

tk.Label(input_frame, text="Kota Awal:", font="Arial 11 italic").grid(row=0, column=0, sticky="w")
start_var = tk.StringVar()
start_box = ttk.Combobox(input_frame, width=20, textvariable=start_var)
start_box['values'] = list(indonesia_graph.keys())
start_box.grid(row=0, column=1, pady=5)
start_box.set("Jakarta")

tk.Label(input_frame, text="Kota Tujuan:", font="Arial 11 italic").grid(row=1, column=0, sticky="w")
goal_var = tk.StringVar()
goal_box = ttk.Combobox(input_frame, width=20, textvariable=goal_var)
goal_box['values'] = list(indonesia_graph.keys())
goal_box.grid(row=1, column=1, pady=5)
goal_box.set("Surabaya")

tk.Button(input_frame, text="Cari Rute", font="Arial 11 bold", bg="#4CAF50", fg="white",
          command=find_path).grid(row=2, column=0, columnspan=2, pady=10)

fig, ax = plt.subplots(figsize=(7, 7))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()

nx.draw(graph, pos, with_labels=True, node_size=700, node_color='skyblue',
        font_size=9, font_color='black', ax=ax)
nx.draw_networkx_edges(graph, pos, width=1.0, alpha=0.5, ax=ax)
ax.set_title("Peta Kota Indonesia (Pulau Jawa)")

canvas_widget.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()
