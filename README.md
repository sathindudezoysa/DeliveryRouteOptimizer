# Delivery Route Optimization

## Overview

This project aims to optimize the delivery route for a set of delivery points and a warehouse. It uses the Traveling Salesman Problem (TSP) to find the best sequential delivery path and then maps the sequence to real cities, adjusting for traffic conditions using shortest-path algorithms like Dijkstra.

## Assumptions

- One vehicle is leaving from the warehouse
- The vehicle goes to the delivery point only once.
- All delivery points must be covered in a sequential manner.

## Approach

1. **TSP Optimization**: The project starts by solving the Traveling Salesman Problem (TSP) to determine the optimal path covering all delivery points and the warehouse.
2. **Mapping to Cities**: Once the sequence is determined, it maps the delivery points to actual cities, considering traffic using shortest-path algorithms like Dijkstra or A\*.
3. **Traffic Adjustment**: Traffic conditions are factored into the path to ensure the most efficient real-world route.

## Justification

- **TSP** ensures the optimal sequence of delivery points, minimizing travel time and distance.
- **Traffic Consideration** using shortest-path algorithms adjusts the route based on real-time road conditions, ensuring practicality.
- The approach is efficient for moderate-sized problems with a time complexity of \( O(n^3 + n \cdot (m + c \log c)) \).

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/delivery-route-optimization.git
```
