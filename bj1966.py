from collections import deque

count = int(input())

for _ in range(count):
    n, m = map(int, input().split())
    for _ in range(n):
        count = 0
        important = deque(list(map(int, input().split())))
        target = important[m]
        print(target)
        while important:
            if len(important) == 1:
                print(count + 1)
                break
            while important[0] != max(important):
                important.append(important.popleft())
                print(important)
            if important.popleft() == target:
                print(count)
                break
            else:
                count += 1
                print("카운트 증ㅈ가")

