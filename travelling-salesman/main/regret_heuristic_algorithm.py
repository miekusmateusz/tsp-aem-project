import numpy as np
import math

def regret_heuristic_tsp(distance_matrix, first_node, regret_k=2):

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

    # Creation of dictionary containing available nodes and costs of their usage for each arc
    costs_map = {}
    for i in available_nodes:
        costs_map[str(i)] = {}

    for _ in range(iterations):
        # For each arc, we save all costs for all available candidates
        for index in range(len(path_nodes) - 1):
            current_arc_length = distance_matrix[path_nodes[index], path_nodes[index + 1]]
            arc_label = str(path_nodes[index]) + ';' + str(path_nodes[index + 1])
            for candidate in available_nodes:
                loss = distance_matrix[path_nodes[index], candidate] + distance_matrix[
                    path_nodes[index + 1], candidate] - current_arc_length

                costs_map[str(candidate)][arc_label] = loss

        best_regret = -1
        best_candidate = -1
        arc_label = ''
        # calculating regrets for each candidates
        for key in costs_map.keys():
            # sorting losses for each candidate
            sorted_vals = sorted(costs_map[str(key)].items(), key=lambda kv: kv[1])
            smallest_cost = sorted_vals[0][1]
            regret = 0
            # if number of arcs is smaller than regret number
            if len(sorted_vals) <= regret_k:
                for ind in range(1, len(sorted_vals)):
                    regret += sorted_vals[ind][1] - smallest_cost

            # if number of arcs is bigger than regret number
            else:
                for ind in range(1, regret_k + 1):
                    regret += sorted_vals[ind][1] - smallest_cost

            # choosing candidate with smallest regret
            if best_regret == -1 or best_regret > regret:
                best_regret = regret
                best_candidate = int(key)
                arc_label = sorted_vals[0][0]

        # Adding best candidate
        index_where_put = path_nodes.index(int(arc_label.split(';')[0])) + 1
        path_nodes.insert(index_where_put, best_candidate)

        # Removing candidate from available nodes
        available_nodes.remove(best_candidate)

        # removing candidate from cost map and reseting inner dicts with costs (can be improved)
        del costs_map[str(best_candidate)]
        for key in costs_map.keys():
            costs_map[key] = {}

    path = 0
    for index in range(len(path_nodes) - 1):
        path += distance_matrix[path_nodes[index], path_nodes[index + 1]]

    return path_nodes, path
