n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 서로 연결된거라 반대로도 저장해줘야함

count = 0

def dfs(graph, v, visited):
    global count
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1 # 탐색되는 곳이 있으면 +1씩 해주는 거 (연결된 컴퓨터 = dfs에 의해 탐색되는거니까)

dfs(graph, 1, visited)
print(count)