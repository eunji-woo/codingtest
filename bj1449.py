N, L = map(int, input().split())
water = list(map(int, input().split()))
water.sort()

start = water[0] - 0.5
end = start + L
count = 1

for i in range(1, len(water)):
    if start <= water[i] - 0.5 and water[i] + 0.5 <= end:
        continue
    else:
        start = water[i] - 0.5
        end = start + L
        count += 1

print(count)


# L의 길이가 짧아서 1개의 구멍도 다 못 막으면?? 근데 한개의 구멍은,, 1M면 막음, 문제에서 L은 자연수라고 했으니 1이상이니까 상관이 없다!!