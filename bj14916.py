# 5의 배수가 될 때까지 2씩 빼준다
# 거슬러줄 수 없는 경우 -1 반환하도록 해야함!!!

n = int(input())
count = 0

while True:
    if (n % 5) == 0:
        count += n // 5
        print(count)
        break
    n -= 2
    count += 1
    if n < 0:
        print("-1")
        break