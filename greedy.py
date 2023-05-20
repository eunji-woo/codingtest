## 2891번
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

# 2891번 - 다른 사람 코드 참고해서 간결하게
N, S, R = map(int, input().split())
S = list(map(int, input().split()))  # 카약이 손상된 팀 번호
R = list(map(int, input().split()))  # 카약이 남는 팀 번호

result = 0  # 출발하지 못하는 팀 수

for i in S:  # 카약이 손상되었지만 여분을 가져온 팀 제거
    if i in R:
        S.remove(i)
        R.remove(i)

for i in S:
    if i - 1 in R: # 손상된 팀 앞 팀이 카약이 남는지 확인
        R.remove(i - 1)
    elif i + 1 in R: # # 손상된 팀 뒷 팀이 카약이 남는지 확인
        R.remove(i + 1)
    else:  # 앞 뒤 팀한테 못 빌리면
        result += 1

print(result)