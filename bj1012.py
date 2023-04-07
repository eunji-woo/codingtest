from collections import deque

r = int(input()) # 반복 횟수

def bfs(x, y, graph):
    queue = deque([(x, y)])  # deque를 생성하기 위해선 리스트를 인자로 넣어야함, deque([x, y])말고 저렇게 해야함
    graph[x][y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        a, b = queue.popleft() # bfs = 선입선출 하기 위해서 popleft
        for v in range(4):
            nx = a + dx[v]
            ny = b + dy[v]
            if nx < 0 or ny < 0 or nx >= m or ny >= n or graph[nx][ny] == 0:
                continue
            else: # graph[nx][ny] == 1일때, 즉 배추가 있는 곳일 경우
                graph[nx][ny] = 0
                queue.append((nx, ny))


for _ in range(r):
    result = 0
    m, n, k = map(int, input().split())
    graph = [[0]*n for _ in range(m)]
    for i in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for k in range(m):
        for j in range(n):
            if graph[k][j] == 1:
                bfs(k, j, graph) # bfs로 인접한 한 뭉텅이의 배추밭 탐색
                result += 1 # 한 뭉텅이 탐색하고 올때마다 지렁이 1마리씩 추가

    print(result)



