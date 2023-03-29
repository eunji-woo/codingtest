# 맨 뒤부터 보면서 뒤보다 작게 만들어야함

N = int(input())
data = list()
count = 0

for _ in range(N):
    data.append(int(input()))

for i in range(N-1, 0, -1): # 리스트 거꾸로 접근
    if data[i] <= data[i-1]:
        while data[i] <= data[i-1]:
            data[i - 1] -= 1
            count += 1
    else:
        continue

print(count)
