N, K = map(int, input().split())
N_list = list(range(2, N+1)) # list(range(3)) => [0, 1, 2]
count = 0

for i in range(2, N+1):
    for j in N_list:
        if j % i == 0:
            N_list.remove(j)
            count = count + 1
            if count == K:
                print(j)