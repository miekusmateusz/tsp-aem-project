from random_solution import *


def steep_node_replacement(initial_solution: list, distance_matrix: np.ndarray):
    potential_nodes = [elem for elem in range(distance_matrix.shape[0]) if elem not in initial_solution]
    cached_delta_values = {}
    # creation of all possible replacement moves of nodes OUTSIDE the PATH as a list of tuples (out_node_ind, in_node_ind)
    possible_replace_outside_path_operations = []
    for ind1 in range(len(initial_solution)):
        for ind2 in range(len(potential_nodes)):
            possible_replace_outside_path_operations.append((ind1, ind2))

    # creation of all possible NODES replacement moves IN CURRENT PATH as a list of tuples (first_node_ind, second_node_ind)
    possible_replace_in_path_operations = []
    for ind1 in range(len(initial_solution)):
        for ind2 in range(ind1 + 1, len(initial_solution)):
            possible_replace_in_path_operations.append((ind1, ind2))

    for _ in range(100):
        current_delta = None
        operation_to_perform = None
        for op1 in possible_replace_outside_path_operations:
            index_to_remove = op1[0]
            index_to_remove_prev, index_to_remove_next = get_neighbours_indices_in_list(index_to_remove,
                                                                                        len(initial_solution))
            node_to_remove = initial_solution[index_to_remove]
            node_to_remove_prev = initial_solution[index_to_remove_prev]
            node_to_remove_next = initial_solution[index_to_remove_next]
            node_to_add = potential_nodes[op1[1]]

            if (0, node_to_remove_prev, node_to_remove, node_to_remove_next, node_to_add) not in cached_delta_values:
                delta = distance_matrix[node_to_remove_prev, node_to_add] + distance_matrix[
                    node_to_remove_next, node_to_add] - \
                        distance_matrix[node_to_remove_next, node_to_remove] + distance_matrix[
                            node_to_remove_prev, node_to_remove]
                cached_delta_values[(0, node_to_remove_prev, node_to_remove, node_to_remove_next, node_to_add)] = delta
            else:
                delta = cached_delta_values[(0, node_to_remove_prev, node_to_remove, node_to_remove_next, node_to_add)]

            if current_delta is None or delta < current_delta:
                operation_to_perform = (0, op1)
                current_delta = delta
        for op2 in possible_replace_in_path_operations:
            first_index = op2[0]
            second_index = op2[1]
            first_index_prev, first_index_next = get_neighbours_indices_in_list(first_index, len(initial_solution))
            second_index_prev, second_index_next = get_neighbours_indices_in_list(second_index, len(initial_solution))
            first_node = initial_solution[first_index]
            first_node_prev = initial_solution[first_index_prev]
            first_node_next = initial_solution[first_index_next]

            second_node = initial_solution[second_index]
            second_node_prev = initial_solution[second_index_prev]
            second_node_next = initial_solution[second_index_next]

            if (1, first_node_prev, first_node, first_node_next, second_node_prev, second_node,
                second_node_next) not in cached_delta_values:
                delta = distance_matrix[first_node_prev, second_node] + distance_matrix[second_node, first_node_next] + \
                        distance_matrix[second_node_prev, first_node] + distance_matrix[first_node, second_node_next] - \
                        distance_matrix[first_node_prev, first_node] - distance_matrix[first_node, first_node_next] - \
                        distance_matrix[second_node_prev, second_node] - distance_matrix[second_node, second_node_next]
                cached_delta_values[
                    (1, first_node_prev, first_node, first_node_next, second_node_prev, second_node,
                     second_node_next)] = delta
            else:
                delta = cached_delta_values[
                    (1, first_node_prev, first_node, first_node_next, second_node_prev, second_node, second_node_next)]

            if current_delta is None or delta < current_delta:
                operation_to_perform = (1, op2)
                current_delta = delta
        if operation_to_perform is None:
            break
        else:

            if operation_to_perform[0] == 0:
                rem = operation_to_perform[1][0]
                add = operation_to_perform[1][1]
                tmp = int(initial_solution[rem])
                initial_solution[rem] = int(potential_nodes[add])
                potential_nodes[add] = int(tmp)
            elif operation_to_perform[0] == 1:
                first = operation_to_perform[1][0]
                second = operation_to_perform[1][1]

                tmp = int(initial_solution[first])
                initial_solution[first] = int(initial_solution[second])
                initial_solution[second] = int(tmp)

    final_path = calculate_path_length(initial_solution, distance_matrix)
    return initial_solution, final_path


def steep_edge_replacement(initial_solution: list, distance_matrix: np.ndarray):
    potential_nodes = [elem for elem in range(distance_matrix.shape[0]) if elem not in initial_solution]
    cached_delta_values = {}
    # creation of all possible replacement moves of nodes OUTSIDE the PATH as a list of tuples (out_node_ind, in_node_ind)
    possible_replace_outside_path_operations = []
    for ind1 in range(len(initial_solution)):
        for ind2 in range(len(potential_nodes)):
            possible_replace_outside_path_operations.append((ind1, ind2))

    # creation of all possible EDGE replacements moves IN CURRENT PATH as a list of tuples (first_node_ind, second_node_ind)
    possible_replace_in_path_indexes_outcomes = generate_all_edge_replacement_possibilities(initial_solution)

    for _ in range(100):
        current_delta = None
        operation_to_perform = None
        for op1 in possible_replace_outside_path_operations:
            index_to_remove = op1[0]
            index_to_remove_prev, index_to_remove_next = get_neighbours_indices_in_list(index_to_remove,
                                                                                        len(initial_solution))
            node_to_remove = initial_solution[index_to_remove]
            node_to_remove_prev = initial_solution[index_to_remove_prev]
            node_to_remove_next = initial_solution[index_to_remove_next]
            node_to_add = potential_nodes[op1[1]]

            if (0, node_to_remove_prev, node_to_remove, node_to_remove_next, node_to_add) not in cached_delta_values:
                delta = distance_matrix[node_to_remove_prev, node_to_add] + distance_matrix[
                    node_to_remove_next, node_to_add] - \
                        distance_matrix[node_to_remove_next, node_to_remove] + distance_matrix[
                            node_to_remove_prev, node_to_remove]
                cached_delta_values[(0, node_to_remove_prev, node_to_remove, node_to_remove_next, node_to_add)] = delta
            else:
                delta = cached_delta_values[(0, node_to_remove_prev, node_to_remove, node_to_remove_next, node_to_add)]

            if current_delta is None or delta < current_delta:
                operation_to_perform = (0, op1)
                current_delta = delta
        for outcome_indexes in possible_replace_in_path_indexes_outcomes:
            remove_moves = outcome_indexes[0][0]
            add_moves = outcome_indexes[0][1]

            sol = [initial_solution[idx] for idx in outcome_indexes[1]]
            if hash(str(sol)) not in cached_delta_values:
                delta = distance_matrix[initial_solution[add_moves[0][0]], initial_solution[add_moves[0][1]]] + \
                        distance_matrix[initial_solution[add_moves[1][0]], initial_solution[add_moves[1][1]]] - \
                        distance_matrix[initial_solution[remove_moves[0][0]], initial_solution[remove_moves[0][1]]] - \
                        distance_matrix[initial_solution[remove_moves[1][0]], initial_solution[remove_moves[1][1]]]
                cached_delta_values[hash(str(sol))] = delta
            else:
                delta = cached_delta_values[hash(str(sol))]
            if current_delta is None or delta < current_delta:
                operation_to_perform = (1, sol)
                current_delta = delta

        if operation_to_perform is None:
            break
        else:
            if operation_to_perform[0] == 0:
                rem = operation_to_perform[1][0]
                add = operation_to_perform[1][1]
                tmp = int(initial_solution[rem])
                initial_solution[rem] = int(potential_nodes[add])
                potential_nodes[add] = int(tmp)
            elif operation_to_perform[0] == 1:
                initial_solution = list(operation_to_perform[1])

    final_path = calculate_path_length(initial_solution, distance_matrix)
    return initial_solution, final_path


def get_neighbours_indices_in_list(index, list_length):
    if index == list_length - 1:
        next = 0
    else:
        next = index + 1
    return index - 1, next


def generate_edge_replacement_for_span(nodes_list: list, span: int, result: list):
    x = 2
    for i in range(len(nodes_list)):

        copy_list = list(nodes_list) + nodes_list[0:span]
        list_slice = copy_list[i:i + span]

        left_end_neighs = get_neighbours_indices_in_list(list_slice[0], len(nodes_list))
        right_end_neighs = get_neighbours_indices_in_list(list_slice[-1], len(nodes_list))

        remove_ops = [(left_end_neighs[0], list_slice[0]), (list_slice[-1], right_end_neighs[1])]
        add_ops = [(left_end_neighs[0], list_slice[::-1][0]), (list_slice[::-1][-1], right_end_neighs[1])]

        copy_list[i:i + span] = copy_list[i:i + span][::-1]
        if i > len(nodes_list) - span:
            res = copy_list[x:len(copy_list) - (span - x)]
            x += 1
        else:
            res = copy_list[0:len(nodes_list)]

        res = shift_list_to_have_zero_index_on_first_place(res)
        if res not in result:
            result.append([[remove_ops, add_ops], res])

    return result


def generate_all_edge_replacement_possibilities(nodes_list: list):
    result = []
    nodes_indexes_list = [ind for ind in range(len(nodes_list))]
    for span in range(3, len(nodes_list)):
        result = generate_edge_replacement_for_span(nodes_indexes_list, span, result)
    return result


def shift_list_to_have_zero_index_on_first_place(nodes_indexes_list: list):
    zero_index = nodes_indexes_list.index(0)

    numpy_list = np.array(nodes_indexes_list)

    return list(np.roll(numpy_list, -zero_index))
