import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())  # 이 문젠 input으로 입력 받으면 시간 초과 뜬다,, readline 사용하는걸 습관을 들이장
graph = [[0] * (n + 1) for _ in range(n + 1)]  # 인접 리스트 방식으로 풀거임

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1  # 방향 그래프가 아니니까 양방향 모두 처리
    graph[y][x] = 1

visited = [False] * (n + 1)  # 1 ≤ u라는 조건이 있으니까 인덱스 0은 안 씀


def bfs(start): # 기본 bfs
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in range(1, n+1):
            if not visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = True


result = 0

for i in range(1, n + 1):
    if not visited[i]:
        bfs(i) # bfs 돌면서 visited[i]가 계속 변함, 그래서 결과가 그대로 visited 리스트 길이만큼 나오는게 아님
        result += 1

print(result)
