import numpy as np
import math


def greedy_tsp(distance_matrix, first_node):
    path_nodes = [first_node]
    iterations = math.ceil(len(distance_matrix) / 2) - 1
    tmp_matrix = np.copy(distance_matrix)
    tmp_matrix[:, first_node] = -1

    for _ in range(iterations):
        # selecting row containing distances of last node in the path to the all rest available nodes
        row = np.copy(tmp_matrix[path_nodes[-1]])
        min_distance = min(val for val in row if val > 0)

        # selecting node closest to the last in the path
        node, = np.where(row == min_distance)
        path_nodes.append(node[0])

        tmp_matrix[:, node] = -1
    path_nodes.append(first_node)

    # calculating length of the created path
    path_length = 0
    for index in range(len(path_nodes) - 1):
        path_length += distance_matrix[path_nodes[index], path_nodes[index + 1]]

    return path_nodes, path_length
