from read_data import import_tsp_instance_to_distance_matrix
from steep_searching import *

matrixA = import_tsp_instance_to_distance_matrix("../resources/kroA100.tsp")
matrixB = import_tsp_instance_to_distance_matrix("../resources/kroB100.tsp")

res = generate_random_solution(matrixA)
solution, path = steep_edge_replacement(res, matrixA)
print(res)
print(calculate_path_length(res, matrixA))
print(solution)
print(calculate_path_length(solution, matrixA))
