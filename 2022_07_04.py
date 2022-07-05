# https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3
# https://eunjiji.tistory.com/118
def solution(number, k):
    answer =  []
    
    for i in number:
        while answer and answer[-1] < i and k > 0:
            answer.pop()
            k = k - 1
        answer.append(i)
        
    if k>0:
        while k > 0:
            answer.pop()
            k = k - 1
        
    answer = "".join(answer)
        
    return answer