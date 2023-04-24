from collections import deque

count = int(input())

for _ in range(count):
    n, m = map(int, input().split())
    count = 0
    important = deque(list(map(int, input().split())))
    value = deque(list(range(len(important))))
    target = value[m]
    while True:
        # print(value, target)
        if important[0] == max(important):  # 중요도가 가장 높은게 젤 앞에 있는 경우
            count += 1  # pop 될때마다 count 1씩 증가
            if target == value[0]:  # targer이 pop되는 경우
                print(count)
                break
            else:  # pop이 되긴 하지만 target이 아닌 다른 것이 pop 되는 경우
                important.popleft()
                value.popleft()
        else:  # 중요도가 가장 높은게 젤 앞에 있는 경우가 아니면
            important.append(important.popleft())
            value.append(value.popleft())
