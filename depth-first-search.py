def dfs(matrix: list, node_no: int) -> list:
    stack = [node_no]
    visited = []

    while stack:
        current = stack.pop()
        visited.append(current)

        for node, edge in enumerate(matrix[current]):
            if edge == 1 and node not in visited:
                stack.append(node)

    return visited
