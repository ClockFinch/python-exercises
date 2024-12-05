import sys

# 3. Napisac algorytm Dijkstry (przechodzenie najkrotszej sciezki w grafie)

class Graph:
    def __init__(self, v: int):
        self.v = v
        self.adj = [[]for _ in range(v)]

    def add_edge(self, a: int, b: int, d: int):
        self.adj[a].append((b, d))
        self.adj[b].append((a, d))

    def min_distance(self, distances, visited):
        min_distance = sys.maxsize
        min_index = -1
        for u in range(self.v):
            if distances[u] < min_distance and visited[u] is False:
                min_index = u
                min_distance = distances[u]
        return min_index

    def dijkstra(self, src: int):

        total_distance = [sys.maxsize] * self.v
        visited = [False] * self.v
        total_distance[src] = 0

        for n in range(self.v):
            x = self.min_distance(total_distance, visited)
            visited[x] = True

            for node, distance in self.adj[x]:
                if total_distance[node] > total_distance[x] + distance and visited[node] is False:
                    total_distance[node] = total_distance[x] + distance

        for i in range(self.v):
            print(f"{i} \t\t {total_distance[i]}")


if __name__ == "__main__":
    test = Graph(5)
    test.add_edge(0, 1, 3)
    test.add_edge(1, 2, 3)
    test.add_edge(2, 3, 3)
    test.add_edge(3, 4, 2)
    test.add_edge(4, 0, 5)
    print(test.adj)
    test.dijkstra(0)
