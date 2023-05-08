def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == data[mid]:
            return mid
        elif target > data[mid]:
            start = mid + 1
        elif target < data[mid]:
            end = mid - 1
    return -1


# set 자료형을 이용해서 코드 짤 수도 있음
# set 자료형 = 중복 허용 x, 순서가 없음
# in 연산자를 쓸 때는 list 자료형보다 set 자료형을 쓰면 빠름
# set 자료형은 탐색 시간복잡도가 O(1)임, list는 O(n)


n = int(input())
n_array = list(map(int, input().split()))
n_array.sort()
m = int(input())
m_array = list(map(int, input().split()))

for i in m_array:
    result = binary_search(i, n_array)
    if result >= 0:
        print("1")
    else:
        print("0")
