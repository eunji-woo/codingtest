# https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=python3

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers)) # numbers 리스트 원소들을 문자열 형태로 바꿔줌
    numbers.sort(key = lambda x:x*1000, reverse=True) # numbers의 원소는 1000이하니까 1000자리로 맞춰준 후 비교되도록 key 설정 
    answer = str(int(''.join(numbers))) 
# int로 바꿔주고 다시 str 해주는 이유는 numbers가 [0,0,0,0]일 경우,,를 생각해보면 됨
    return answer