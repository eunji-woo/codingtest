a = input()
a2 = list(map(int, str(a)))

a2.sort(reverse=True)

print("".join(map(str, a2)))