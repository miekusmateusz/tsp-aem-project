import numpy as np
import math


def greedy_tsp(distance_matrix, first_node):
    if first_node + 1 >= len(distance_matrix) or first_node < 0:
        raise Exception("Given node_number is out of bounds")

    nodes = [first_node]
    path = 0
    iterations = math.ceil(len(distance_matrix) / 2) - 1
    tmp_matrix = np.copy(distance_matrix)
    tmp_matrix[:, first_node] = -1

    for _ in range(iterations):
        row = np.copy(tmp_matrix[nodes[-1]])
        min_distance = min(val for val in row if val > 0)
        node, = np.where(row == min_distance)
        nodes.append(node[0])
        path += min_distance
        tmp_matrix[:, node] = -1
    path += distance_matrix[first_node, nodes[-1]]
    nodes.append(first_node)
    return nodes, path
