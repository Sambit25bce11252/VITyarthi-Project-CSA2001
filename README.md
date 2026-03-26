# VITyarthi-Project-CSA2001
AI-based Maze Solver built using BFS, DFS, and A* search algorithms with CLI interface and performance analysis.

# AI Maze Solver

## 👤 Author
Name: Sambit Garnayak  
Course: CSA2001 - Fundamentals of AI & ML  

---

## 📌 Project Description
AI Maze Solver is a Command Line Interface (CLI) based project that solves a maze using Artificial Intelligence search algorithms. The program finds a path from a Start point (S) to a Goal point (G) and compares the performance of different algorithms.

This project demonstrates how AI techniques can be used to solve real-world pathfinding problems efficiently.

---

## 🎯 Objectives
- Implement fundamental AI search algorithms
- Compare their performance
- Understand pathfinding techniques
- Apply AI concepts to a real-world problem

---

## 🧠 Algorithms Used

### 1. Breadth First Search (BFS)
- Explores the maze level by level
- Uses Queue (FIFO)
- Guarantees shortest path
- Explores more nodes

### 2. Depth First Search (DFS)
- Explores deeply before backtracking
- Uses Stack (LIFO)
- Does not guarantee shortest path
- Faster in some cases

### 3. A* Algorithm
- Uses heuristic (Manhattan Distance)
- Combines actual cost + estimated cost
- More efficient and optimal
- Used in real-world applications

---

## ⚙️ Technologies Used
- Python 3
- CLI (Command Line Interface)
- Standard Python libraries (time, collections, heapq)

---

## 📂 Project Structure

maze-ai-solver/

main.py → Main program (CLI interface)  
maze.py → Maze creation and handling  
algorithms/bfs.py → BFS implementation  
algorithms/dfs.py → DFS implementation  
algorithms/astar.py → A* implementation  

---

## ▶️ How to Run

Step 1: Download or clone the project  
Step 2: Open terminal in project folder  
Step 3: Run the program using:

python main.py

---

## 📥 Input Format

Maze is represented as a grid:

S → Start  
G → Goal  
. → Free path  
X → Wall  

Example:

S . . X .  
X X . X .  
. . . . G  

---

## 📤 Output

The program displays:

- Whether path is found or not  
- Path length  
- Number of nodes explored  
- Time taken  
- Comparison of all algorithms  

---

## 🔍 Working

1. Maze is loaded into the system  
2. User selects an algorithm (BFS, DFS, A*)  
3. Algorithm searches for a path  
4. Path and performance details are displayed  
5. User can compare all algorithms  

---

## 📊 Results

- BFS finds shortest path but explores more nodes  
- DFS is faster but may give longer path  
- A* performs best with fewer nodes and optimal path  

---

## 🌍 Real-Life Applications

- Navigation systems (Google Maps)  
- Robotics path planning  
- Game AI movement  
- Network routing  

---

## ✅ Conclusion

This project demonstrates how different AI algorithms solve the same problem in different ways. A* algorithm proves to be the most efficient due to its heuristic-based approach.

---

## 🚀 Future Improvements

- Add GUI interface  
- Allow file-based maze input  
- Handle larger and dynamic mazes  
- Add visualization of path  

---