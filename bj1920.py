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


n = int(input())
n_array = list(map(int, input().split()))
m = int(input())
m_array = list(map(int, input().split()))
