import numpy as np
import math

def greedy_cycle_tsp(distance_matrix, first_node):
    nodes = [first_node]
    path = 0
    iterations = math.ceil(len(distance_matrix) / 2) - 2
    tmp_matrix = np.copy(distance_matrix)
    available_nodes = [n for n in range(distance_matrix.shape[0]) if n != first_node]

    #assigning closest node
    row = np.copy(tmp_matrix[first_node])
    min_distance = min(val for val in row if val > 0)
    node, = np.where(row == min_distance)

    nodes.append(node[0])
    path += min_distance
    available_nodes.remove(node[0])
    nodes.append(first_node)

    for _ in range(iterations):
        tmp_length = -1
        tmp_candidate = -1
        for index in range(len(nodes) - 1):
            d = distance_matrix[nodes[index], nodes[index+1]]
            for candidate in available_nodes:
                candidate_path_length = distance_matrix[nodes[index], candidate] + distance_matrix[nodes[index+1], candidate] - d
                if tmp_length > candidate_path_length or tmp_length == -1:
                    tmp_length = candidate_path_length
                    tmp_candidate = candidate
                    tmp_place = index+1
        nodes.insert(tmp_place, tmp_candidate)
        available_nodes.remove(tmp_candidate)
    for index in range(len(nodes) - 1):
        path+=distance_matrix[nodes[index], nodes[index+1]]
    return nodes, path