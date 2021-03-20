from read_data import import_tsp_instance_to_distance_matrix, read_coordinates
from greedy_algorithm import *
from greedy_cycle_algorithm import *
from regret_heuristic_algorithm import *

import random
import matplotlib.pyplot as plt

matrixA = import_tsp_instance_to_distance_matrix("resources/kroA100.tsp")
matrixB = import_tsp_instance_to_distance_matrix("resources/kroB100.tsp")


def tests():
    random_nodes = random.sample(range(0, 100), 50)
    paths = {'greedyA': {}, 'greedyB': {}, 'cycleA': {}, 'cycleB': {}, 'regretA': {}, 'regretB': {}}
    results = {'greedyA': [], 'greedyB': [], 'cycleA': [], 'cycleB': [], 'regretA': [], 'regretB': []}

    for node in random_nodes:
        greedy_A_Res = greedy_tsp(matrixA, node)
        paths['greedyA'][greedy_A_Res[1]] = greedy_A_Res[0]

        greedy_B_Res = greedy_tsp(matrixB, node)
        paths['greedyB'][greedy_B_Res[1]] = greedy_B_Res[0]

        cycle_A_Res = greedy_cycle_tsp(matrixA, node)
        paths['cycleA'][cycle_A_Res[1]] = cycle_A_Res[0]

        cycle_B_Res = greedy_cycle_tsp(matrixB, node)
        paths['cycleB'][cycle_B_Res[1]] = cycle_B_Res[0]

        regret_A_Res = regret_heuristic_tsp(matrixA, node)
        paths['regretA'][regret_A_Res[1]] = regret_A_Res[0]

        regret_B_Res = regret_heuristic_tsp(matrixB, node)
        paths['regretB'][regret_B_Res[1]] = regret_B_Res[0]

        results['greedyA'].append(greedy_A_Res[1])

        results['cycleA'].append(cycle_A_Res[1])

        results['regretA'].append(regret_A_Res[1])

        results['greedyB'].append(greedy_B_Res[1])

        results['cycleB'].append(cycle_B_Res[1])

        results['regretB'].append(regret_B_Res[1])

    print('greedyA  min: ' + str(np.min(results['greedyA'])) + ' mean: ' + str(
        np.mean(results['greedyA'])) + ' max: ' + str(np.max(
        results['greedyA'])))
    print('greedyB  min: ' + str(np.min(results['greedyB'])) + ' mean: ' + str(
        np.mean(results['greedyB'])) + ' max: ' + str(np.max(
        results['greedyB'])))
    print('cycleA  min: ' + str(np.min(results['cycleA'])) + ' mean: ' + str(
        np.mean(results['cycleA'])) + ' max: ' + str(np.max(
        results['cycleA'])))
    print('cycleB  min: ' + str(np.min(results['cycleB'])) + ' mean: ' + str(
        np.mean(results['cycleB'])) + ' max: ' + str(np.max(
        results['cycleB'])))
    print('regretA  min: ' + str(np.min(results['regretA'])) + ' mean: ' + str(
        np.mean(results['regretA'])) + ' max: ' + str(np.max(
        results['regretA'])))
    print('regretB  min: ' + str(np.min(results['regretB'])) + ' mean: ' + str(
        np.mean(results['regretB'])) + ' max: ' + str(np.max(
        results['regretB'])))

    coordinatesA = read_coordinates("resources/kroA100.tsp")
    coordinatesB = read_coordinates("resources/kroB100.tsp")

    sorted_keys_regret_A = sorted(paths['regretA'])
    selected_path_regret_A = paths['regretA'][sorted_keys_regret_A[0]]

    sorted_keys_regret_B = sorted(paths['regretB'])
    selected_path_regret_B = paths['regretB'][sorted_keys_regret_B[0]]

    sorted_keys_cycle_A = sorted(paths['cycleA'])
    selected_path_cycle_A = paths['cycleA'][sorted_keys_cycle_A[0]]

    sorted_keys_cycle_B = sorted(paths['cycleB'])
    selected_path_cycle_B = paths['cycleB'][sorted_keys_cycle_B[0]]

    sorted_keys_greedy_A = sorted(paths['greedyA'])
    selected_path_greedy_A = paths['greedyA'][sorted_keys_greedy_A[0]]

    sorted_keys_greedy_B = sorted(paths['greedyB'])
    selected_path_greedy_B = paths['greedyB'][sorted_keys_greedy_B[0]]

    x = []
    y = []

    for j in selected_path_greedy_A:
        x.append(coordinatesA[j][0])
        y.append(coordinatesA[j][1])

    plt.plot(x, y, label="graph")

    plt.title('Greedy A')

    plt.show()

    x = []
    y = []

    for j in selected_path_greedy_B:
        x.append(coordinatesB[j][0])
        y.append(coordinatesB[j][1])

    plt.plot(x, y, label="graph")

    plt.title('Greedy B')

    plt.show()

    x = []
    y = []

    for j in selected_path_cycle_A:
        x.append(coordinatesA[j][0])
        y.append(coordinatesA[j][1])

    plt.plot(x, y, label="graph")

    plt.title('Cycle A')

    plt.show()

    x = []
    y = []

    for j in selected_path_cycle_B:
        x.append(coordinatesB[j][0])
        y.append(coordinatesB[j][1])

    plt.plot(x, y, label="graph")

    plt.title('Cycle A')

    plt.show()

    x = []
    y = []

    for j in selected_path_regret_A:
        x.append(coordinatesA[j][0])
        y.append(coordinatesA[j][1])

    plt.plot(x, y, label="graph")

    plt.title('Regret A')

    plt.show()

    x = []
    y = []

    for j in selected_path_regret_B:
        x.append(coordinatesB[j][0])
        y.append(coordinatesB[j][1])

    plt.plot(x, y, label="graph")

    plt.title('Regret B')

    plt.show()


tests()
