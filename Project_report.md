<h1>AI-Based Maze Solver</h1>

<h2><u>VITyarthi Project - CSA2001</u></h2>
---
<h5>Author:</h5> Sambit Kumar Garanayak  <br>
<h5>Course:</h5> CSA2001 - Fundamentals in AI & ML
---
<h2> Abstract </h2>

The AI Maze Solver is a project that demonstrates the practical application of Artificial Intelligence (AI) in solving pathfinding problems. Utilizing Breadth-First Search (BFS), Depth-First Search (DFS), and A* algorithms, the system efficiently identifies a path from a Start point (S) to a Goal point (G) in a maze. The project compares the performance of these algorithms in terms of speed, optimality, and computational effort, highlighting AI’s significance in real-world scenarios such as robotics, navigation, and game development.

---
<h2>1. Introduction</h2>

Pathfinding is a core problem in AI, relevant to areas like robotics, computer games, and network routing. The AI Maze Solver is designed to explore how different AI search algorithms perform when navigating through a maze. By implementing BFS, DFS, and A*, the project evaluates each algorithm’s efficiency, accuracy, and computational requirements. A Command Line Interface (CLI) is used for simplicity and clear demonstration of algorithmic behavior.

---
<h2>2. Objectives</h2>

Implement and understand fundamental AI search algorithms
Evaluate and compare the performance of BFS, DFS, and A*
Gain insights into pathfinding strategies and optimization techniques
Apply AI concepts to a practical, real-world problem

---
<h2>3. Algorithms Implemented</h2>

<h3> 3.1 Breadth-First Search (BFS) </h3>
Explores the maze level by level
Uses a Queue (FIFO) data structure
Guarantees the shortest path
Explores a larger number of nodes, which can increase computation
<h3> 3.2 Depth-First Search (DFS)</h3>
Explores paths deeply before backtracking
Uses a Stack (LIFO) data structure
Does not guarantee the shortest path
Can be faster for some maze configurations
<h3> 3.3 A Algorithm* </h3>
Incorporates a heuristic-based approach
Combines actual path cost + estimated cost to goal
Provides efficient and optimal solutions
Widely applied in real-world pathfinding, robotics, and AI in games

---
<h2> 4. Technologies Used </h2>

- Programming Language: Python 3
- Interface: Command Line Interface (CLI)
- Libraries: Python standard libraries (time, collections, heapq)

---
<h2> 5. Project Structure </h2>

- main.py → Main program with CLI interface <br>
- maze.py → Maze generation and handling <br>
- algorithms/bfs.py → BFS implementation <br>
- algorithms/dfs.py → DFS implementation <br>
- algorithms/astar.py → A* implementation

---
<h2> 6. Methodology </h2>

Maze Representation:
The maze is represented as a 2D grid using symbols:
S → Start
G → Goal
. → Free path
X → Wall
Algorithm Selection: Users select BFS, DFS, or A* via the CLI.
Pathfinding Process: The chosen algorithm searches for a path from S to G.

Output Generation: The program displays:
- Path existence
- Path length
- Number of nodes explored
- Execution time
- Performance Comparison: The system allows comparison of algorithm efficiency and optimality.

---
<h2> 7. Input/Output Example </h2>

Input Maze: <br>
S . . X . <br>
X X . X . <br>
. . . . G <br>

Output Example:

Path Found: Yes <br>
Path Length: 7 steps  <br>
Nodes Explored: BFS → 12,  DFS → 9, A* → 8   <br>
Time Taken: BFS → 0.003 sec, DFS → 0.002 sec, A* → 0.002 sec  <br>

Values may vary depending on the maze size and configuration.

---
<h2> 8. Results </h2>

BFS: Guarantees the shortest path but explores more nodes
DFS: Faster in some cases but may result in longer paths
A:* Most efficient, balancing speed and optimal path length

Sample Performance Table:

| Algorithm | Path Length | Nodes Explored | Time Taken (sec) |
| --------- | ----------- | -------------- | ---------------- |
| BFS       | 7           | 12             | 0.003            |
| DFS       | 9           | 9              | 0.002            |
| A*        | 7           | 8              | 0.002            |



---
<h2> 9. Real-World Applications </h2>

- Navigation systems (e.g., Google Maps)
- Robotics path planning
- AI movement in computer games
- Network routing and optimization
---
<h2>10. Conclusion</h2>

The AI Maze Solver demonstrates the practical use of AI search algorithms in solving pathfinding problems. The comparison shows that while BFS guarantees the shortest path and DFS may be faster in certain scenarios, the A algorithm* provides the best balance of efficiency and optimality due to its heuristic-based approach.

---
<h2> 11. Future Work </h2> 

- Develop a Graphical User Interface (GUI) for visualization
- Allow file-based maze inputs for dynamic scenarios
- Support larger and dynamic mazes
- Include path visualization and step-by-step animations

---
<h2> 12. References </h2>

Russell, S. J., & Norvig, P. (2020). Artificial Intelligence: A Modern Approach. Pearson. <br>
Python Official Documentation: https://docs.python.org/3/ <br>
Online tutorials and lecture notes on BFS, DFS, and A* algorithms <br>
