# from collections import deque
#
# count = int(input())
#
# for _ in range(count):
#     n, m = map(int, input().split())
#     for _ in range(n):
#         count = 0
#         important = deque(list(map(int, input().split())))
#         target = important[m]
#         while important:
#             if len(important) == 1:
#                 print(count + 1)
#                 break
#             while important[0] != max(important):
#                 important.append(important.popleft())
#                 print(important)
#             count += 1
#             if important.popleft() == target:
#                 print(count)
#                 break
#             else:
#                 continue
#
#

idx = list(range(3))
print(idx)
# [0, 1, 2]

# https://assaeunji.github.io/python/2020-05-04-bj1966/ 참고
# 리스트 두개로 딕셔너리 느낌을,, 구현한 것 같다고 느꼈다.