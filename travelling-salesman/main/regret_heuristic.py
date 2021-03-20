import numpy as np
import math

def regret_heuristic_tsp(distance_matrix, first_node, regret_k=2):
    nodes = [first_node]
    iterations = math.ceil(len(distance_matrix) / 2) - 2
    available_nodes = [n for n in range(distance_matrix.shape[0]) if n != first_node]

    # assigning closest node
    row = np.copy(distance_matrix[first_node])
    min_distance = min(val for val in row if val > 0)
    node, = np.where(row == min_distance)

    nodes.append(node[0])
    available_nodes.remove(node[0])
    nodes.append(first_node)

    costs_map = {}
    for i in available_nodes:
        costs_map[str(i)] = {}

    for _ in range(iterations):
        # For each arc, we write down all costs for all available candidates
        for index in range(len(nodes) - 1):
            current_arc = distance_matrix[nodes[index], nodes[index + 1]]
            str_index = str(nodes[index]) + ';' + str(nodes[index + 1])
            for candidate in available_nodes:
                loss = distance_matrix[nodes[index], candidate] + distance_matrix[
                    nodes[index + 1], candidate] - current_arc
                costs_map[str(candidate)][str_index] = loss

        best_regret = -1
        best_candidate = -1

        # calculating regret for each candidates
        for key in costs_map.keys():
            sorted_vals = sorted(costs_map[str(key)].items(), key=lambda kv: kv[1])
            current_best_val = sorted_vals[0][1]
            regret = 0

            # if number of arcs is smaller than regret number
            if len(sorted_vals) <= regret_k:
                for ind in range(1, len(sorted_vals)):
                    regret += sorted_vals[ind][1] - current_best_val

            # else compare k_regret number of values
            else:
                for ind in range(1, regret_k + 1):
                    regret += sorted_vals[ind][1] - current_best_val

            if best_regret == -1 or best_regret > regret:
                best_regret = regret
                best_candidate = int(key)
                place = sorted_vals[0][0]

        # Adding best candidate
        index_where_put = nodes.index(int(place.split(';')[0])) + 1
        nodes.insert(index_where_put, best_candidate)

        # Removing candidate from available nodes
        available_nodes.remove(best_candidate)

        # removing candidate from cost map and reseting inner dicts with costs (can be improved)
        del costs_map[str(best_candidate)]
        for key in costs_map.keys():
            costs_map[key] = {}

    path = 0
    for index in range(len(nodes) - 1):
        path += distance_matrix[nodes[index], nodes[index + 1]]

    return nodes, path
