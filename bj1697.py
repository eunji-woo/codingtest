#  이코테 미로탈출 문제 (bfs)랑 유사한 문제
#  bfs로 탐색하고 탐색할때마다 탐색한 곳의 visited 배열을 1씩 증가시키고,
#  가장 먼저 목적지에 도착했을때 (최단거리) 목적지의 visited 배열 값을 출력
#  최단 거리 or 최단 횟수 구하는 경우 = dfs보단 bfs 이용
import sys
from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft() # 가장 먼저 들어갔던걸 pop 해와서 k에 저장
        if v == k: # 목적지까지 한 가지 경로로라도 탐색 끝난 경우
            return visited[v]
        for v2 in (v-1, v+1, 2*v):
            if 0 <= v2 < 100001 and not visited[v2]:
                visited[v2] = visited[v] + 1
                q.append(v2)
                for i in range(30):
                    print(visited[i], end=" ")
                print("")

n, k = map(int, sys.stdin.readline().split())
visited = [0] * 100001
print(bfs(n))