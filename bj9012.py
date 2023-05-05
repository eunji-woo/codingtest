t = int(input())

for _ in range(t):
    text = input()
    count = 0
    for i in text:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            break
    if count == 0: # 짝이 딱 맞을 때
        print("YES")
    else: # )나 ( 수가 많아서 count가 음수나 양수일 때
        print("NO")