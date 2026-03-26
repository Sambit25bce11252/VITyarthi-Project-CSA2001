from collections import deque
from maze import find_start_goal

def bfs(maze):
    start, goal = find_start_goal(maze)

    queue = deque([(start, [start])])
    visited = set()
    nodes_explored = 0

    while queue:
        (current, path) = queue.popleft()
        nodes_explored += 1

        if current == goal:
            return path, nodes_explored

        if current in visited:
            continue

        visited.add(current)
        x, y = current

        # Explore neighbors (Up, Down, Left, Right)
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if maze[nx][ny] != 'X' and (nx, ny) not in visited:
                    queue.append(((nx, ny), path + [(nx, ny)]))

    return None, nodes_explored