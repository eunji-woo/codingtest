n, m = map(int, input().split())

pack_min = 1001
single_min = 1001
result = 0

for _ in range(m):
    a, b = map(int, input().split())
    if a < pack_min:
        pack_min = a
    if b < single_min:
        single_min = b

if n % 6 == 0:
    if single_min * 6 < pack_min:
        result = single_min * n
    else:
        result = pack_min * (n//6)
else:
    if n >= 6:
        if single_min * 6 < pack_min:
            result = single_min * n
        else:
            result = pack_min * (n // 6)
            if single_min * (n % 6) < pack_min:
                result += single_min * (n % 6)
            else:
                result += pack_min
    else:
        if single_min * n < pack_min:
            result = single_min * n
        else:
            result = pack_min

print(result)