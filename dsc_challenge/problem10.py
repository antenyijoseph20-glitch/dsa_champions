def path_exists(graph, start, target):
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()

        if current == target:
            return True

        if current in visited:
            continue

        visited.add(current)

        for neighbour in graph.get(current, []):
            if neighbour not in visited:
                stack.append(neighbour)

    return False


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": ["F"],
    "F": []
}

print(path_exists(graph, "A", "F"))
print(path_exists(graph, "D", "A"))

