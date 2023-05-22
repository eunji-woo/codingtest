# # 2891번 -> 앞팀에게 빌리는걸 탐욕해야함
# n, s, r = map(int, input().split())
# s = map(int, input().split())
# r = map(int, input().split())
#
# result = [1 for _ in range(n)]
#
# for i in s:
#     result[i-1] = 0
#
# for i in r:
#     result[i-1] += 1 # 여분의 배 가져왔지만 배가 파손된 팀의 경우도 있어서 result[i-1] =2 로 하면 안됨
#
# # print(result)
# if result[0] == 0 and result[1] == 2:
#     result[0] = 1
#     result[1] = 1
#
# # print(result)
# for k in range(1, len(result)-1):
#     # print(k)
#     if result[k] == 0 and result[k-1] == 2:
#         result[k] = 1
#         result[k - 1] = 1
#     elif result[k] == 0 and result[k+1] == 2:
#         result[k] = 1
#         result[k+1] = 1
#     # print(result)
#
# if result[-1] == 0 and result[-2] == 2:
#     result[-1] = 1
#     result[-2] = 1
#
# print(result.count(0))

## 2212번
# n = int(input())
# k = int(input())
# sensor = list(map(int, input().split()))
# sensor.sort()
# distance = []
# result = 0
#
# # for문이 n-k만큼 도는 이유?
# # -> n개의 센서에서 센서 사이의 거리의 수는? n-1이고, 집중국 개수가 k개면 k-1개만큼 거리가 가장 먼 센서 간의 거리를 배제할 수 있음
# # (ex. n = 6이고 k = 2이면 센서를 2개의 집중국으로 묶어야 함, 즉 센서간의 거리 1개를 무시할 수 있게 됨)
# # -> n-1-(k-1) = n-k
# for i in range(0, n-1):  # 센서 개수랑 집중국 개수가 같으면 n-k은 0이라 result는 0이 됨
#     distance.append(sensor[i+1]-sensor[i])
#
# distance.sort()
#
# print(sum(distance[0:n-k]))

## 1715번
n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()