from read_data import import_tsp_instance_to_distance_matrix
from greedy import *
from greedy_cycle import *
from regret_heuristic import *




matrix = import_tsp_instance_to_distance_matrix("resources/kroA100.tsp")

result1 = greedy_tsp(matrix, 1)
result2 = greedy_cycle_tsp(matrix, 1)
result3 = regret_heuristic_tsp(matrix, 1)

print(result1)
print(result2)
print(result3)