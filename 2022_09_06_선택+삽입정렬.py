# 백준 2750번 #


# 선택정렬
count = int(input())
array = []

for _ in range(count):
    array.append(int(input()))

for i in range(len(array)):
    min = i
    for j in range(i+1, len(array)):
        if array[j] < array[min]: # 여기롤 if array[j] < array[i]: 이렇게 해서 어디가 잘못된지 한참 찾음 ㅠㅠ
            min = j
    array[i], array[min] = array[min], array[i]

for k in array:
    print(k)


# 삽입정렬
count = int(input())
array = []

for _ in range(count):
    array.append(int(input()))

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break

for k in array:
    print(k)
