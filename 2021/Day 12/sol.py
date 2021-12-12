import os.path

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
    data = f.read().splitlines()

# data = """start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end""".splitlines()

graph = {}
for line in data:
    node1, node2 = line.split("-")
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    graph[node1].append(node2)
    graph[node2].append(node1)

# find all paths through the graph
def find_paths(graph, start, end, path=[], twice=False):
    if start in ("start", "end") and start in path:
        return []
    if start.islower() and start in path and twice:
        return []
    if start.islower() and start in path:
        twice = True
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        newpaths = find_paths(graph, node, end, path, twice)
        for newpath in newpaths:
            paths.append(newpath)
    return paths


print(len(find_paths(graph, "start", "end")))
