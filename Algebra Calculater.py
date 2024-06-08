import Quadratic
import Pythagoream_Solver
import Linear_Systems_Solver

print(f"Quadratic:Q\n"
      f"Pythagoream:P\n"
      f"Linear:L")

Solver_Input = input().lower()


if Solver_Input == "q":
      Quadratic.Run_Quadratic()

elif Solver_Input == "p":
      Pythagoream_Solver.Run_Pythag()

elif Solver_Input == "l":
      Linear_Systems_Solver.Run_Linear()

else:
      print("Invalid Input, pls try again")


