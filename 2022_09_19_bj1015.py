# 백준 1015

count = int(input())
array_A = list(map(int, input().split()))
array_P = []

# B[P[i]] = A[i]

sorted_A = sorted(array_A)

for i in array_A:
    array_P.append(sorted_A.index(i))
    sorted_A[sorted_A.index(i)] = -1 # 중복된 요소 있을 경우

for i in range(count):
    print(array_P[i], end=" ")

# input이 3/2 3 1일때, 배열 P는 1, 2, 0이 되고
# b[1] = 2
# b[2] = 3
# b[0] = 1