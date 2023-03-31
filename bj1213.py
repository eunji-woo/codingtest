import sys
from collections import Counter

name = list(sys.stdin.readline().rstrip()) # 문자열 입력받고
name.sort() # 알파벳 순으로 정렬
count = Counter(name) # Counter 생성자 사용법 : https://eunjiji.tistory.com/169
odd = 0
odd_alpha = ''
ans = ''
for i in count:
    if count[i] % 2 != 0: # 특정 알파벳 등장 횟수가 짝수가 아니라면
        odd += 1 # 홀수 count 개수 증가
        odd_alpha += i

    for _ in range(count[i]//2):
        ans += i

if odd > 1: # 팰린드롬 만들 수 없는 경우
    print("I'm Sorry Hansoo")

elif odd == 0: # 입력된 글자가 짝수라면
    print(ans + ans[::-1])

else: # 입력된 글자가 홀수라면
    print(ans + odd_alpha + ans[::-1])



# 망한 코드 2
# result = ""
# word_list.sort()
# i = 0
# center = ""
#
# while True:
#     print(i)
#     if i > len(word_list)/2 :
#         break
#     if word_list[i] == word_list[i+1]:
#         print(word_list[i])
#         print(word_list[i+1])
#         result += word_list[i]
#         # result[-(k+1)] = word_list[i]
#         i += 2
#     else:
#         if len(center) == 0:
#             print("여기")
#             center += word_list[i]
#             i += 1
#         else:
#             break
#
# if len(center) > 1:
#     print('I\'m Sorry Hansoo')
# else:
#     print(result + center + result[::-1])


# array[::-1] -> 배열을 거꾸로 접근하는 법



# 망한 코드2,, 소생 불가 ㅠ

# count = 0
# for i in range(0, len(word_list)-1, 2):
#     if word_list[i] == word_list[i+1]:
#         print(i)
#         result[count] = word_list[i]
#         result[-(count+1)] = word_list[i]
#         count += 1
#         print(result)
#         if i + 2 >= len(word_list) - 1:
#             print("".join(str(result)))
#     else:
#         if i == (len(word_list)//2) + 1:
#             print("result")
#             print(result)
#             result[count] = word_list[i]
#             count += 1
#         else:
#             print('I\'m Sorry Hansoo')
#             break
