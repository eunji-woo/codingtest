# 선택 정렬 = 가장 작은 데이터를 !선택!해 맨 앞에 있는 데이터와 바꾸고, 그 다음작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복
# 선택 정렬은 정렬할 데이터가 10,000개 이상으로 넘어가면 급격히 비효율적이게 됨 (시간복잡도 o(n^2)

import sys

count = int(sys.stdin.readline())
result = []

for _ in range(count):
    result.append(int(input()))

for i in range(len(result)):
    min_index = i
    for k in range(i+1, len(result)): # 가장 작은 요소 찾는 과정
        if result[min_index] > result[k]:
            min_index = k
    result[min_index], result[i] = result[i], result[min_index]  # 가장 작은 요소 찾으면 앞쪽으로 스와핑 해서 가져옴

for i in result:
    print(i)


# 삽입 정렬 = 데이터가 거의 정렬되어 있을 때 효율적
# 시간 복잡도가 o(n^2)으로 선택 정렬과 같지만, 데이터가 거의 정렬되어 있는 상태라면 매우 효율적 = 최선의 시간 복잡도 o(n)

import sys

count = int(sys.stdin.readline())
result = []

for _ in range(count):
    result.append(int(input()))

for i in range(1, len(result)): # 삽입 정렬은 두번째 요소부터! (첫번째 요소는 정렬이 되어있다고 가정)
    for k in range(i, 0, -1):
        if result[k] < result[k-1]:
            result[k], result[k-1] = result[k-1], result[k]
        else:  # 앞에 요소들이 나보다 작은 경우
            break

for i in result:
    print(i)
