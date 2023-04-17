from collections import deque

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
sour_tomato = deque()

for i in range(n):
    for k in range(m):
        if tomato[i][k] == 1: # 익은 토마토
            sour_tomato.append([i, k])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0


def solution():
    while sour_tomato:
        x, y = sour_tomato.popleft() # 가장 먼저 들어간 거
        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m and tomato[x + dx[i]][y + dy[i]] == 0:
                tomato[x + dx[i]][y + dy[i]] = tomato[x][y] + 1
                sour_tomato.append([x + dx[i], y + dy[i]])

solution()

for i in range(n):
    for k in range(m):
        if tomato[i][k] == 0: # 안 익은 토마토
            print("-1")
            exit(0)
        else:
            if result < tomato[i][k]:
                result = tomato[i][k]

print(result - 1) # 2차원 배열 최솟값 구하는 법 잘 알아두기!! (그냥 max, min 함수 쓰면 안됨)