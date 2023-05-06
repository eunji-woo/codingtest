def binary_general(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end: # start, end는 계속 변함
        mid = (start+end) // 2

        if target == data[mid]:
            return mid
        elif target < data[mid]:
            end = mid - 1
        elif target > data[mid]:
            start = mid + 1

    return None # whlie 문 돌면서 탐색했는데 없으면 data에 target이 없는 거

def binary_recursion(target, data, start, end):
    if start > end:
        return None

    mid = (start+end) // 2

    if target == data[mid]:
        return mid
    elif target < data[mid]:
        end = mid - 1
    elif target > data[mid]:
        start = mid + 1
    return binary_recursion(target, data, start, end)

data = [i*3 for i in range(11)]
target = 6
result1 = binary_general(target, data)
result2 = binary_recursion(target, data, 0, len(data)-1)

print(result1)
print(result2)