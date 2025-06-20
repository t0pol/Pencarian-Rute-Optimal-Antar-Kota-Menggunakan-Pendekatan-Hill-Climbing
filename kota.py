def get_neighbours(city, graph):
    return graph[city]

def select_best_neighbour(neighbours, heuristic_value):
    best_neighbour = None
    best_cost = float('inf')
    for neighbour in neighbours:
        cost = heuristic_value[neighbour]
        if cost < best_cost:
            best_neighbour = neighbour
            best_cost = cost
    return best_neighbour

def hill_climbing(graph, start, goal, heuristic_value):
    path = [start]
    current_city = start
    while current_city != goal:
        neighbours = get_neighbours(current_city, graph)
        best_neighbour = select_best_neighbour(neighbours, heuristic_value)
        if best_neighbour is None or heuristic_value[best_neighbour] >= heuristic_value[current_city]:
            break
        current_city = best_neighbour
        path.append(best_neighbour)
    return path

indonesia_graph = {
    'Jakarta': ['Bekasi', 'Bandung', 'Serang'],
    'Bekasi': ['Jakarta', 'Karawang'],
    'Bandung': ['Jakarta', 'Cimahi', 'Garut'],
    'Serang': ['Jakarta', 'Cilegon'],
    'Karawang': ['Bekasi', 'Purwakarta'],
    'Purwakarta': ['Karawang', 'Subang'],
    'Cimahi': ['Bandung'],
    'Garut': ['Bandung', 'Tasikmalaya'],
    'Tasikmalaya': ['Garut', 'Banjar'],
    'Banjar': ['Tasikmalaya', 'Ciamis'],
    'Ciamis': ['Banjar', 'Majalengka'],
    'Majalengka': ['Ciamis', 'Cirebon'],
    'Cirebon': ['Majalengka', 'Tegal'],
    'Tegal': ['Cirebon', 'Pekalongan'],
    'Pekalongan': ['Tegal', 'Semarang'],
    'Semarang': ['Pekalongan', 'Salatiga'],
    'Salatiga': ['Semarang', 'Boyolali'],
    'Boyolali': ['Salatiga', 'Solo'],
    'Solo': ['Boyolali', 'Sragen'],
    'Sragen': ['Solo', 'Ngawi'],
    'Ngawi': ['Sragen', 'Madiun'],
    'Madiun': ['Ngawi', 'Nganjuk'],
    'Nganjuk': ['Madiun', 'Kediri'],
    'Kediri': ['Nganjuk', 'Blitar'],
    'Blitar': ['Kediri', 'Malang'],
    'Malang': ['Blitar', 'Surabaya'],
    'Surabaya': ['Malang', 'Sidoarjo'],
    'Sidoarjo': ['Surabaya'],
    'Cilegon': ['Serang']
}

heuristic = {
    'Jakarta': 780,
    'Bekasi': 760,
    'Bandung': 730,
    'Serang': 800,
    'Karawang': 710,
    'Purwakarta': 690,
    'Cimahi': 725,
    'Garut': 700,
    'Tasikmalaya': 670,
    'Banjar': 650,
    'Ciamis': 640,
    'Majalengka': 620,
    'Cirebon': 600,
    'Tegal': 580,
    'Pekalongan': 550,
    'Semarang': 500,
    'Salatiga': 480,
    'Boyolali': 470,
    'Solo': 450,
    'Sragen': 430,
    'Ngawi': 400,
    'Madiun': 370,
    'Nganjuk': 350,
    'Kediri': 320,
    'Blitar': 290,
    'Malang': 200,
    'Surabaya': 0,
    'Sidoarjo': 20,
    'Cilegon': 790
}
