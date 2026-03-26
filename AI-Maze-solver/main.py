import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import time
from maze import load_maze, print_maze
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astar import astar


def run_algorithm(maze, name, func):
    start_time = time.time()
    path, nodes = func(maze)
    end_time = time.time()

    path_length = len(path) if path else 0
    time_taken = round(end_time - start_time, 5)

    print(f"\n--- {name} RESULT ---")
    print("Path Found:", "YES" if path else "NO")
    print("Path Length:", path_length)
    print("Nodes Explored:", nodes)
    print("Time Taken:", time_taken, "sec")

    if path:
        print("Path:", path)

    return {
        "name": name,
        "path_length": path_length,
        "nodes": nodes,
        "time": time_taken
    }


def compare_algorithms(maze):
    print("\nRunning all algorithms...\n")

    results = []
    results.append(run_algorithm(maze, "BFS", bfs))
    results.append(run_algorithm(maze, "DFS", dfs))
    results.append(run_algorithm(maze, "A*", astar))

    print("\n--- COMPARISON ---")
    print("Algorithm\tPath Length\tNodes\tTime")

    for r in results:
        print(f"{r['name']}\t\t{r['path_length']}\t\t{r['nodes']}\t{r['time']}")


def main():
    print("===== AI Maze Solver =====")

    maze = load_maze()
    print_maze(maze)

    while True:
        print("\nChoose an option:")
        print("1. Solve using BFS")
        print("2. Solve using DFS")
        print("3. Solve using A*")
        print("4. Compare all algorithms")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            run_algorithm(maze, "BFS", bfs)

        elif choice == "2":
            run_algorithm(maze, "DFS", dfs)

        elif choice == "3":
            run_algorithm(maze, "A*", astar)

        elif choice == "4":
            compare_algorithms(maze)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()