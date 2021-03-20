import numpy as np
import math


def import_tsp_instance_to_distance_matrix(path):
    tsp_i = open(path, "r")
    dimension_read = False
    it = 1
    for line in tsp_i.readlines():
        split_line = line.split()

        if split_line[0] == 'DIMENSION:':
            dimension = int(split_line[1])
            distance_matrix = [[0 for y in range(dimension)] for x in range(dimension)]
            dimension_read = True

        if dimension_read and split_line[0] == str(it):
            coords = (int(split_line[1]), int(split_line[2]))
            distance_matrix = update_distance_matrix(distance_matrix, it - 1, coords)
            it += 1

    return np.array(distance_matrix) + np.array((distance_matrix)).transpose()


def update_distance_matrix(distance_matrix, index, value):
    # we assume that we update matrix row by row starting from 0 to ... dimension-1
    if len(distance_matrix) != len(distance_matrix[0]):
        raise TypeError('Given matrix is not square matrix')
    for i in range(index + 1, len(distance_matrix)):
        distance_matrix[index][i] = value
    for j in range(0, index):
        distance_matrix[j][index] = math_rounded_euclidean_distance(distance_matrix[j][index], value)

    return distance_matrix


def math_rounded_euclidean_distance(a, b):
    return round(math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)))
