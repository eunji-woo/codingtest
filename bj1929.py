# 에라토스테네스의 체 방법 이용
# 1. 2부터 N까지의 모든 자연수를 나열
# 2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾고
# 3. 남은 수 중에서 i의 배수를 모두 제거 (i는 제거 안함)
# 4. 더 이상 반복할 수 없을 때까지 2번과 3번 과정을 반복
# 에라토스테네스의 체를 사용해 n 이하의 모든 소수를 구하려고 할 때, 효율적으로 구하기 위해 n의 제곱근( sqrt(n) ) 까지만 확인한다고 함 (증명이 있다는데 찾아보진 않았다..)
import math

s, e = map(int, input().split())

result = [ True for _ in range(e+1)]

for i in range(2, int(math.sqrt(e))+1):
    if result[i]:
        k = 2  # 3번 보면 i는 제거 안함! ex) 2는 소수니까
        while i * k <= e:
            result[i*k] = False
            k += 1

for i in range(s, e+1):
    if result[i] and i != 1:
        print(i)
