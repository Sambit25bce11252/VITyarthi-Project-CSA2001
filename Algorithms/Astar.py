import heapq
from maze import find_start_goal

def heuristic(a, b):
    # Manhattan Distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze):
    start, goal = find_start_goal(maze)

    priority_queue = [(0, start, [start])]
    visited = set()
    nodes_explored = 0

    while priority_queue:
        (cost, current, path) = heapq.heappop(priority_queue)
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
                    g_cost = len(path)          # actual cost
                    h_cost = heuristic((nx, ny), goal)  # estimated cost
                    f_cost = g_cost + h_cost

                    heapq.heappush(
                        priority_queue,
                        (f_cost, (nx, ny), path + [(nx, ny)])
                    )

    return None, nodes_explored