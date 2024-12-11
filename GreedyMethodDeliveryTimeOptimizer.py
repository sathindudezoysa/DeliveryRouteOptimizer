import numpy as np

# # Define the cities and their coordinates
# cities = [(0, 0), (1, 5), (3, 1), (6, 4), (2, 2), (4, 3), (5, 1), (2, 0), (5, 5), (9, 3)]
#
# # Adjacency matrix
# adjacency_matrix = [
#     [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
#     [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
#     [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
#     [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
#     [0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
#     [0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
#     [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
#     [0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
#     [1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
# ]
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


selected_cities = [0, 11, 5, 3]

# Selected cities to navigate
# selected_cities = [0, 1, 4, 8]


def calculate_distance(city_a_index: int, city_b_index: int) -> float:
    """Calculate Euclidean distance between two cities."""
    x_a, y_a = cities[city_a_index]
    x_b, y_b = cities[city_b_index]
    return np.sqrt((x_b - x_a) ** 2 + (y_b - y_a) ** 2)


def navigate_cities(start_city_index: int) -> list:
    """Navigate through selected cities based on given algorithm."""
    visited = set()
    current_city = start_city_index
    route = [current_city]

    while len(visited) < len(selected_cities):
        visited.add(current_city)

        # Check for direct connections to other selected cities
        next_city = None
        for city in selected_cities:
            if city not in visited and adjacency_matrix[current_city][city] != 0:
                next_city = city
                break

        if next_city is not None:
            route.append(next_city)
            current_city = next_city
        else:
            # Find nearest unvisited selected city
            nearest_city = None
            x = float('inf')
            min_distance = float('inf')

            for city in selected_cities:
                if city not in visited:
                    distance = calculate_distance(current_city, city)
                    if distance < x:
                        x = distance
                        nearest_city = city

            while current_city != nearest_city:
                min_val = float("inf")
                y = None
                for r in range(len(adjacency_matrix[current_city])):
                    if adjacency_matrix[current_city][r] != 0:
                        if r in route:
                            continue
                        distance = calculate_distance(current_city, r)
                        if x - distance < min_val:
                            min_val = x - distance
                            y = r

                current_city = y
                route.append(current_city)
                print(route)

            # for city in selected_cities:
            #     if city not in visited:
            #         distance = calculate_distance(current_city, city)
            #         if distance < min_distance:
            #             min_distance = distance
            #             nearest_city = city

            # Move to nearest unvisited city
    return route




# Start navigation from the first selected city (index of city '0')
route_taken = navigate_cities(selected_cities[0])

# Output the order of visited cities
print("Order of visited cities:", route_taken)
