def solution(n, lost, reserve):
    # 두 배열간 중복되는 원소 개수 = 여벌 체육복 있는데 도난 당해서 빌려줄 순 없는 사람 수
    answer = n - len(lost) + len(list(set(reserve).intersection(lost)))

    # 여벌 체육복 있는데 1개만 도난 당해서 자기가 입을 체육복은 있는 애들은 뺌
    new_lost = list(set(lost) - set(reserve))

    # 빌려줄 체육복이 있는 애들
    new_reserve = list(set(reserve) - set(lost))

    for i in new_lost:
        if (i - 1) in new_reserve:
            answer = answer + 1
            new_reserve.remove(i - 1)
        elif (i + 1) in new_reserve:
            answer = answer + 1
            new_reserve.remove(i + 1)

    return answer