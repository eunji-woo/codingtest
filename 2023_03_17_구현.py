k = int(input())
l = list()
for _ in range(k):
    i = int(input())
    if i == 0:
        l.pop()
    else:
        l.append(i)

print(sum(l))
