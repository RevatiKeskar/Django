from django.shortcuts import render
from puzzle_solver import main  # Assuming 'puzzle_solver.py' holds your main()

def solve_puzzle(request):
    puzzle_start = [[6, 2, 8], [4, 7, 1], [0, 3, 5]]  # Example starting puzzle
    solution_steps = main(puzzle_start)  # Solve the puzzle

    # Prepare data for template
    solution_data = {
        'total_steps': len(solution_steps) - 1,  # Number of moves
        'solution_steps': solution_steps,
    }

    return render(request, 'puzzle/solution.html', solution_data)

# # views.py

# from django.shortcuts import render
# from puzzle_solver import main

# def index(request):
#     initial_puzzle = [[6, 2, 8, 12],
#                       [4, 7, 1, 11],
#                       [9, 3, 5, 0],
#                       [13, 10, 14, 15]]

#     solution = solve_puzzle(initial_puzzle)
#     return render(request, 'puzzle/index.html', {'solution': solution})
