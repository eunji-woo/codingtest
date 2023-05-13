## 11382번
# import sys
# n = sys.stdin.readline().split()
# result = 0
# for i in n:
#     result += int(i)
# print(result)

## 10926번
# import sys
# n = sys.stdin.readline().strip()
# print(n + "??!")

## 2525번
# import sys
# t = list(map(int, sys.stdin.readline().split()))
# need_time = int(input())
# h = t[0]
# m = t[1]
#
# if m + need_time >= 60:
#     h += (m + need_time) // 60
#     if h >= 24:
#         h -= 24
#     m = (m + need_time) % 60
# else:
#     m += need_time
#
# print(str(h) + " " + str(m))

## 25314번
# n = int(input())
# print(n//4 * "long " + "int") # 연산자 순서 잘 생각하기 (나는 print("long " *n//4 + "int")라고 해서 한 번 틀림, 이렇게 되면 long *n하고 이걸 4로 나누게 되니까 타입에러뜸

## 2480번
# import sys
# n = list(map(int, sys.stdin.readline().split()))
# result = 0
#
# for i in range(3):
#     if n.count(n[i]) == 3:
#         result = 10000 + n[i] * 1000
#     elif n.count(n[i]) == 2:
#         result = 1000 + n[i] * 100
#
# if result == 0:
#     result = max(n) * 100
#
# print(result)
# 간결한 코드
# a, b, c=map(int, input().split())
# print(10000+1000*a if a==b==c else 1000+100*b if a==b or b==c else 1000+100*a if c==a else 100*max(a, b, c))
# 3가지니까 나올 수 있는 경우의 수가 저렇게밖에 없으니까,, 저렇게 하면 된다

## 10807번
# n = int(input())
# number_list = list(map(int, input().split()))
# v = int(input())
# print(number_list.count(v))  # count는 리스트에 해당 요소가 몇 개 있는지 세어줌

## 10818번
# n = int(input())
# number_list = list(map(int, input().split()))
# print(str(min(number_list)) + " " + str(max(number_list)))

## 18108번
# print(int(input()) - 543)

## 2562번
# import sys
# n = list()
# for _ in range(9):
#     n.append(int(sys.stdin.readline()))
# print(max(n))
# print(n.index(max(n)) + 1) # index 함수는 특정 요소의 인덱스를 찾아주는 함수

## 27866번
# n = input()
# m = int(input())
# print(n[m-1])

## 1152번
# s = input().split()  # 문자열 입력 받은거 split 하면 알아서 리스트로 저장됨
# print(len(s))

## 10951번
# 종료 조건이 명시되어있지 않기 때문에 try-except로 입력이 없어 에러가 나는 경우를 처리해줘야함
# while True:
#     try:
#         n, m = map(int, input().split())
#         print(n+m)
#     except:
#         break

## 11720번
n = input()
m = list(map(int, input()))
print(sum(m))