r = int(input()) # 반복 횟수
result = 0

for _ in range(r):
    m, n, k = map(int, input().split())
    graph = [[0]*n for _ in range(m)]
    for i in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for k in range(m):
        for j in range(n):
            if graph[k][j] == 1:
                for v in range(4):
                    nx = k + dx[v]
                    ny = j + dy[v]
                    if nx < 0 or ny < 0 or nx >= m-1 or ny >= n-1:
                        continue
                    else:
                        graph[nx][ny] = 0
                    result += 1
    print(result, end='\n')



