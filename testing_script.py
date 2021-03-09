from sudoku_solver import sudoku_solver
from time import time

std_input_list = ["input1.txt", "input2.txt", "input3.txt"]
hex_input_list = ["input_hex1.txt", "input_hex2.txt", "input_hex3.txt"]

std_time = 0
hex_time = 0

for file in std_input_list:
    t0 = time()
    sudoku_solver(file)
    t1 = time()
    comp_time = t1 - t0
    std_time = std_time + comp_time
    print(file + " : " + str(comp_time))

avg_std_time = std_time / len(std_input_list)
print("Average std time: " + str(avg_std_time))

for file in hex_input_list:
    t0 = time()
    sudoku_solver(file)
    t1 = time()
    comp_time = t1 - t0
    hex_time = hex_time + comp_time
    print(file + " : " + str(comp_time))

avg_hex_time = hex_time / len(hex_input_list)
print("Average hex time: " + str(avg_hex_time))

