def load_maze():
    """
    Returns a predefined maze.
    S = Start
    G = Goal
    . = Free path
    X = Wall
    """
    return [
        ['S', '.', '.', 'X', '.'],
        ['X', 'X', '.', 'X', '.'],
        ['.', '.', '.', '.', 'G']
    ]


def find_start_goal(maze):
    """
    Finds the coordinates of Start (S) and Goal (G)
    """
    start = None
    goal = None

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'G':
                goal = (i, j)

    return start, goal


def print_maze(maze):
    """
    Prints the maze in a readable format
    """
    print("\nMaze Layout:")
    for row in maze:
        print(" ".join(row))