import numpy as np
import math


def greedy_cycle_tsp(distance_matrix, first_node):
    path_nodes = [first_node]
    iterations = math.ceil(len(distance_matrix) / 2) - 2
    available_nodes = [n for n in range(distance_matrix.shape[0]) if n != first_node]

    # creating first arc by selecting the node closest to the first node
    row = np.copy(distance_matrix[first_node])
    min_distance = min(val for val in row if val > 0)
    node, = np.where(row == min_distance)
    path_nodes.append(node[0])
    available_nodes.remove(node[0])
    path_nodes.append(first_node)

    for _ in range(iterations):
        tmp_loss = -1
        tmp_candidate = -1
        # iterating through every arc in our path
        for index in range(len(path_nodes) - 1):
            arc_length = distance_matrix[path_nodes[index], path_nodes[index + 1]]
            # checking potential loss for every candidate in reference to each arc
            for candidate in available_nodes:
                potential_loss = distance_matrix[path_nodes[index], candidate] + distance_matrix[
                    path_nodes[index + 1], candidate] - arc_length
                # saving candidate which minimalizes loss
                if tmp_loss > potential_loss or tmp_loss == -1:
                    tmp_loss = potential_loss
                    tmp_candidate = candidate
                    tmp_place_to_insert_node = index + 1

        # adding selected node to path
        path_nodes.insert(tmp_place_to_insert_node, tmp_candidate)
        available_nodes.remove(tmp_candidate)

    # calculating length of the created path
    path_length = 0
    for index in range(len(path_nodes) - 1):
        path_length += distance_matrix[path_nodes[index], path_nodes[index + 1]]
    return path_nodes, path_length
