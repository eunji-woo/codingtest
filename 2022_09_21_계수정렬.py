import sys

count = int(input())

a = []
b = [0] * 10001

for _ in range(count):
    b[int(sys.stdin.readline())] += 1


# for i in b:
#     for j in a:
#         if i == j:
#             i = i + 1

# for i in range(count):
#     b[a[i]] = b[a[i]] + 1

for i in range(10001):
    for j in range(b[i]):
        print(i)