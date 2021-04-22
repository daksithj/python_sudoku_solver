import os
import numpy as np
from sudoku_solver import sudoku_solver
from time import time

std_input_list = os.listdir("examples/sudoku")
hex_input_list = os.listdir("examples/hexadoku")

output_folder = "outputs/"

std_time = 0
hex_time = 0

for file in std_input_list:
    t0 = time()
    solution = sudoku_solver("examples/sudoku/" + file)
    t1 = time()
    comp_time = t1 - t0
    std_time = std_time + comp_time
    print(file + " : " + str(comp_time))

    # Saving solution in a text file
    output_name = os.path.basename(file)[:-4]
    output_name = output_folder + output_name + "_output.txt"
    np.savetxt(output_name, solution, fmt="%s")

avg_std_time = std_time / len(std_input_list)
print("Average std time: " + str(avg_std_time))

for file in hex_input_list:
    t0 = time()
    solution = sudoku_solver("examples/hexadoku/" + file)
    t1 = time()
    comp_time = t1 - t0
    hex_time = hex_time + comp_time
    print(file + " : " + str(comp_time))

    # Saving solution in a text file
    output_name = os.path.basename(file)[:-4]
    output_name = output_folder + output_name + "_output.txt"
    np.savetxt(output_name, solution, fmt="%s")

avg_hex_time = hex_time / len(hex_input_list)
print("Average hex time: " + str(avg_hex_time))

