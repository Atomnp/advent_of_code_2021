from collections import Counter
from time import time

t1 = time()


if __name__ == "__main__":
    graph = {}

    def append(graph, key, val):
        if val != "start" and key != "end":
            if key not in graph:
                graph[key] = [val]
            else:
                graph[key].append(val)

    def small(s: str):
        return s == s.lower()

    alreadyTwice = False

    def foo(graph: dict, children: list, visited: list):
        global alreadyTwice
        count = 0
        for child in children:
            if small(child) and child in visited and alreadyTwice:
                continue
            elif small(child) and child in visited and not alreadyTwice:
                visited.append(child)
                alreadyTwice = Counter(visited)[child] > 1

                count += foo(graph, graph[child], visited)

                # backtrack
                alreadyTwice = Counter(visited)[child] <= 1
                visited.pop()

            elif child == "end":
                count += 1
                # print(visited)
            else:
                visited.append(child)
                count += foo(graph, graph[child], visited)
                visited.pop()
        return count

    with open("./12/input.txt", "r") as f:
        lines = f.read().splitlines()
        # create graph structure
        for line in lines:
            a, b = line.split("-")
            append(graph, a, b)
            append(graph, b, a)
        visited, count = [], 0
        # print(graph)
        count = foo(graph, graph["start"], visited)
        print(count)
        print(time() - t1)
