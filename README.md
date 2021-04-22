# python_sudoku_solver
A Sudoku puzzle solver made using python. Supports solving Sudoku (9x9)
and Hexadoku (16x16) puzzles.

The inputs must be given in text format. There are some example inputs
in the **examples** folder of this repository. The solver can be run in
the following manner.

```bash
$ python sudoku_solver.py examples/sudoku/input1.txt
```
There is testing script (**testing_script.py**) included here as well,
which would solve the puzzles in the examples folder, and calculate the
respective times to solve each of them. The average time taken (in
seconds) to solve is also displayed.

**Note:** The timing calculated here include the time taken to read the
text file as well.

```bash
input1.txt : 0.004016876220703125
input2.txt : 0.0019960403442382812
input3.txt : 0.0029876232147216797
Average std time: 0.003000179926554362
input_hex1.txt : 0.007971048355102539
input_hex2.txt : 0.009006023406982422
input_hex3.txt : 0.009004354476928711
Average hex time: 0.008660475413004557
```
This was also used in a Image input/live camera feed input based Sudoku
puzzle solver as well:
[vision-sudoku-solver](https://github.com/daksithj/vision-sudoku-solver)
.
