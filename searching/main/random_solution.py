import math
import random

import numpy as np


def generate_random_solution(distance_matrx: np.ndarray, number_of_iterations=100):
    number_of_nodes_in_solution = math.ceil(distance_matrx.shape[0] / 2)
    best_result = ([], -1)
    for _ in range(number_of_iterations):
        random_nodes = random.sample(range(0, 100), number_of_nodes_in_solution)
        path_l = calculate_path_length(random_nodes, distance_matrx)
        if path_l < best_result[1] or best_result[1] == -1:
            best_result = (random_nodes, path_l)


def calculate_path_length(nodes: list, distance_matrix: np.ndarray):
    copy_nodes = list(nodes)
    copy_nodes.append(copy_nodes[0])
    path_length = 0
    for index in range(len(copy_nodes) - 1):
        path_length += distance_matrix[copy_nodes[index], copy_nodes[index + 1]]
    return path_length
