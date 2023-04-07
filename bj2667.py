from collections import deque


def bfs(x, y, graph):
    queue = deque([(x, y)])  # deque를 생성하기 위해선 리스트를 인자로 넣어야함, deque([x, y])말고 저렇게 해야함
    graph[x][y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 1
    while queue:
        a, b = queue.popleft() # bfs = 선입선출 하기 위해서 popleft
        for v in range(4):
            nx = a + dx[v]
            ny = b + dy[v]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 0:
                continue
            else: # graph[nx][ny] == 1일때, 즉 집이 있는 곳일 경우
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


n = int(input())
graph = [list(map(int, input())) for _ in range(n)] # 입력 받는 방식!! 잘 익혀두장~~
result = 0
count = []
for i in range(n):
    for k in range(n):
        if graph[i][k] == 1:
            count.append(bfs(i, k, graph))
            result += 1

print(result)
count.sort() # sorted() 내장 함수는 인자로 넘어온 객체의 원래 순서를 건드리지 않고 정렬된 원소들을 새로운 객체에 담아서 반환, sort()는 인자로 받은 리스트를 변경
for i in count:
    print(i)
