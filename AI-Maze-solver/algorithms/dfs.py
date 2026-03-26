from maze import find_start_goal

def dfs(maze):
    start, goal = find_start_goal(maze)

    stack = [(start, [start])]
    visited = set()
    nodes_explored = 0

    while stack:
        (current, path) = stack.pop()
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
                    stack.append(((nx, ny), path + [(nx, ny)]))

    return None, nodes_explored