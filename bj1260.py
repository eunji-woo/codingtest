from collections import deque

n, m, v = map(int, input().split())

graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True # 문제 특성 상,, 인접행렬을 이용해야한다,,
    graph[b][a] = True

visited_d = [False] * (n + 1)
visited_b = [False] * (n + 1)


def dfs(start, visited):
    visited[start] = True
    print(start, end=" ")
    for i in range(1, n + 1): # 연결된 곳이 여러개일 경우 낮은 번호의 정점부터 탐색해야해서 for i in graph[v]: 말고 저렇게 해야한다!!!!!!!
        if not visited[i] and graph[start][i]:  # 만약 해당 i값을 방문하지 않았고 V와 연결이 되어 있다면
            dfs(i, visited)


def bfs(start, visited):
    queue = deque([start])  # deque를 생성하기 위해선 리스트를 인자로 넣어야함
    visited[start] = True
    while queue:
        v = queue.popleft()  # 선입선출 하기 위해서 popleft
        print(v, end=" ")
        for i in range(1, n + 1):
            if not visited[i] and graph[v][i]:
                queue.append(i)
                visited[i] = True


dfs(v, visited_d)
print("")
bfs(v, visited_b)