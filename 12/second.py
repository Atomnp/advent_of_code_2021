from collections import Counter

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

    def foo(graph: dict, children: list, visited: list):
        count = 0
        for child in children:
            a = dict(Counter(visited))
            alreadyTwice = 2 in {key: a[key] for key in a if small(key)}.values()

            if small(child) and child in visited and alreadyTwice:
                continue
            elif small(child) and child in visited and not alreadyTwice:
                visited.append(child)
                count += foo(graph, graph[child], visited)
                # backtrack
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
        print(graph)
        count = foo(graph, graph["start"], visited)
        print(count)
