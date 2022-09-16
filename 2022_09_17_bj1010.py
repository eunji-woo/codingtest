import math


def number_of_case(x, y):
    # bCa를 구해야하니까 b!/(b-a)!a!
    # math.factorial()
    return math.factorial(y)//(math.factorial(y-x)*math.factorial(x))


count = int(input())

for _ in range(count):
    x, y = map(int, input().split())
    print(number_of_case(x, y))