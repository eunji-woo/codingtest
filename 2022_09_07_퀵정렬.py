import sys

count = int(input())
array = []

for _ in range(count):
    array.append(int(sys.stdin.readline()))

def quick_sort(array, start, end):
    if start >= end: # 데이터가 1개면 종료
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[pivot] >= array[left]:
            left = left + 1 # pivot 보다 큰 값이 있는 인덱스를 찾을 때까지 +1 하는 것
        while right > start and array[pivot] <= array[right]: # start는 피벗이니까 right >= start아니고 > 이거임
            right = right - 1
        if left > right: # 엇갈리면
            array[pivot], array[right] = array[right], array[pivot] # 작은 데이터 위치랑 피벗 위치랑 swap
        else: # 엇갈리지 않았다면
            array[left], array[right] = array[right], array[left] # pivot보다 작고, 큰 데이터 swap
    quick_sort(array, start, right-1) # 정렬된 피벗 앞 부분끼리 또 퀵 정렬
    quick_sort(array, right+1, end) # 정렬된 피벗 뒷 부분끼리 또 퀵 정렬

quick_sort(array, 0, count-1) # 마지막을 계속 count 로 해서 잘못된 곳 한참 찾음 ㅠㅠ, 인덱스는 0부터니까 count - 1 !!!!

for i in array:
    print(i)