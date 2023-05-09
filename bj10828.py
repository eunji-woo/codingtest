import sys

n = int(input())
s = list()

for _ in range(n):
    command = sys.stdin.readline()
    c = command.split()[0]

    if c == "push":
        s.append(command.split()[1])
    elif c == "pop":
        if len(s) > 0:
            print(s.pop())
        else:
            print("-1")
    elif c == "size":
        print(len(s))
    elif c == "empty":
        if len(s) == 0:
            print("1")
        else:
            print("0")
    elif c == "top":
        if len(s) == 0:
            print("-1")
        else:
            print(s[-1])