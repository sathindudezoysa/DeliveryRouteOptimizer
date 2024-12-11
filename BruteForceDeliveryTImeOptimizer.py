import itertools
import numpy as np
import matplotlib.pyplot as plt
import time

def distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

def total_distance(path, cities, adjacency_matrix):
    total = 0
    for i in range(len(path) - 1):
        if adjacency_matrix[path[i]][path[i + 1]] == 0:
            return float('inf')  # Invalid path due to disconnected cities
        total += adjacency_matrix[path[i]][path[i + 1]]
    return total

def path_exists(path, adjacency_matrix):
    for i in range(len(path) - 1):
        if adjacency_matrix[path[i]][path[i + 1]] == 0:
            return False
    return True

def selected_cities_avaliable(path, selected_cities):
    if set(selected_cities).issubset(set(path)):
        return True
    else:
        return False

def tsp_brute_force(cities, adjacency_matrix, selected_cities):
    num_cities = len(cities)
    city_indices = list(range(num_cities))
    print(city_indices)
    min_distance = float('inf')
    best_path = None

    # For visualization
    all_paths = []
    all_distances = []

    for r in range(len(selected_cities), num_cities):
        for path in itertools.combinations(city_indices, r):
            if not path_exists(path, adjacency_matrix):
                continue

            if not selected_cities_avaliable(path, selected_cities):
                continue


            dist = total_distance(path, cities, adjacency_matrix)
            all_paths.append(path)
            all_distances.append(dist)

            if dist < min_distance:
                min_distance = dist
                best_path = path

            # plot_tsp(cities, adjacency_matrix, best_path, path, selected_cities)
            # time.sleep(0.5)
    plot_tsp(cities, adjacency_matrix, best_path, path, selected_cities)
    return best_path, min_distance, all_paths, all_distances



def plot_tsp(cities, adjacency_matrix, best_path, current_path, selected_cities):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

    # Plot all connections in the adjacency matrix
    for i in range(len(cities)):
        for j in range(len(cities)):
            if adjacency_matrix[i][j] != 0:
                x_values = [cities[i][0], cities[j][0]]
                y_values = [cities[i][1], cities[j][1]]
                ax1.plot(x_values, y_values, color='gray', linestyle='dotted', alpha=0.5)

    # Highlight selected cities
    for city in selected_cities:
        ax1.scatter(cities[city][0], cities[city][1], color='green', s=100, label='Selected City' if city == selected_cities[0] else "")
        ax2.scatter(cities[city][0], cities[city][1], color='green', s=100, label='Selected City' if city == selected_cities[0] else "")

    # Plot the best path
    if best_path:
        best_x = [cities[city][0] for city in best_path]
        best_y = [cities[city][1] for city in best_path]
        ax1.plot(best_x, best_y, color='red', label='Best Path', linewidth=2)

    # Plot the current path
    current_x = [cities[city][0] for city in current_path]
    current_y = [cities[city][1] for city in current_path]
    ax2.plot(current_x, current_y, color='blue', label='Current Path', linewidth=1)

    # Mark cities in both plots
    for j, (x, y) in enumerate(cities):
        ax1.scatter(x, y, color='blue')
        ax1.text(x, y, str(j), color='black', fontsize=12)
        ax2.scatter(x, y, color='blue')
        ax2.text(x, y, str(j), color='black', fontsize=12)

    ax1.set_title('All Connections')
    ax2.set_title('Current Path')
    ax2.legend()
    plt.show()


# Example city coordinates
cities = [
    [4, 2], [7, 3], [10, 1], [12, 4], [9, 6], [4, 7], [2, 5], [1, 9], [4, 11],
    [9, 9], [14, 7], [17, 4], [19, 8], [15, 12], [18, 14], [14, 15], [9, 17], [5, 16],
    [4, 18], [1, 15]
]


# Example usage:
adjacency_matrix = [
    [0, 5, 7, 0, 0, 3, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
    [5, 0, 6, 4, 2, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
    [7, 6, 0, 3, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
    [0, 4, 3, 0, 7, 0, 0, 0, 0, 0, 6, 8, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
    [0, 2, 0, 7, 0, 4, 0, 0, 0, 3, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
    [3, 9, 0, 0, 4, 0, 5, 2, 7, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
    [8, 0, 0, 0, 0, 5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
    [0, 0, 0, 0, 0, 2, 4, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 8
    [0, 0, 0, 0, 0, 7, 0, 6, 0, 9, 0, 0, 0, 0, 0, 0, 0, 2, 5, 3],  # 9
    [0, 0, 0, 0, 3, 6, 0, 0, 9, 0, 8, 0, 0, 4, 0, 5, 7, 6, 0, 0],  # 10
    [0, 0, 0, 6, 9, 0, 0, 0, 0, 8, 0, 7, 3, 5, 0, 0, 0, 0, 0, 0],  # 11
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 4, 0, 0, 0, 0, 0, 0, 0],  # 12
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 0, 6, 2, 0, 0, 0, 0, 0],  # 13
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 5, 6, 0, 7, 1, 0, 0, 0, 0],  # 14
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 7, 0, 9, 0, 0, 0, 0],  # 15
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 1, 9, 0, 8, 0, 0, 0],  # 16
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 7, 0, 0, 0, 0, 0, 8, 0, 4, 3, 0],  # 17
    [0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 0, 0, 0, 0, 0, 0, 4, 0, 2, 0],  # 18
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],  # 19
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],  # 20
]


selected_cities = [0, 11, 18, 19]  # Specify cities to include in brute force

best_path, min_distance, all_paths, all_distances = tsp_brute_force(cities, adjacency_matrix, selected_cities)

print(f"Best Path: {best_path}")
print(f"Minimum Distance: {min_distance}")
