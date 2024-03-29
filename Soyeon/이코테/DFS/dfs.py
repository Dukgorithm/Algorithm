def dfs(graph, v, visited):
    # 현재 노드를 방문처리
    visited[v] = True
    print("v=", v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False]*len(graph)

dfs(graph, 1, visited)