# 처음 보고 그리디 문제인줄 알았음, 근데 dp 문제
# 그리디 알고리즘은 내가 생각한 처음 최적의 방법이 끝까지 반례 없이 적용이 되는 경우에 이용하고,
# 동적 계획법은 가능성을 모두 두고 그 안에 최솟값을 찾음

n = int(input())
d = [0] * (n+1) # 메모제이션 기법 (다이나믹 프로그래밍 특징)

# 2부터 시작하니까 bottom up 방식
for i in range(2, n+1): # d[i] 에는 i을 1로 만들기 위한 최소한의 연산 횟수가 저장되어있음
    d[i] = d[i-1] + 1 # 1을 뺄 경우
    if i % 2 == 0: # 2로 나눠지는 경우
        d[i] = min(d[i], d[i//2] + 1) # 1로 뺀 거랑 2로 나눈 것 중에 최솟값을 d[i]에 저장
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)  # 위에서 구한 d[i]랑 3으로 나눈 것 중에 최솟값을 d[i]에 저장

print(d[n])

# top down 방식, 재귀 함수로 메모제이션 딕셔너리를 채워감
n = int(input())
d = {1:0} # 1이 1이 되기 위한 최소 연산 횟수는 0이다~

def recur(n):
    if n in d.keys(): # n에 해당하는 딕셔너리가 채워져 있으면 종료
        return d[n]
    elif n % 3 == 0 and n % 2 == 0:
        d[n] = min(recur(d[i // 3]) + 1, recur(d[i // 2]) + 1)
    elif n % 3 == 0:
        d[n] = min(recur(d[i // 3]) + 1, d[n - 1] + 1)
    elif n % 2 == 0:
        d[n] = min(recur(d[i // 2]) + 1, d[n - 1] + 1)
    else:
        d[n] = recur(d[n-1]) + 1
    return d[n]

print(recur(n))



