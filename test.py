import random


def roll_dice():
    return random.randint(1, 6)


i = 1
my_money = 100
computer_money = 100
while i <= 10:
    print("=====")
    print("현재 게임 횟수: " + str(i))
    print("나의 게임 머니: " + str(my_money) + "p")
    print("컴퓨터의 게임 머니: " + str(computer_money) + "p")
    print("-----")
    while True:
        bet_money = int(input("베팅할 금액을 입력하세요 (최대 20p): "))
        if bet_money <= 20:  # 베팅 금액을 20p 초과하여 입력하면 다시 입력하도록 함
            break
    me = roll_dice()
    computer = roll_dice()
    print("나의 주사위: " + str(me))
    print("컴퓨터의 주사위: " + str(computer))
    if me == computer:
        print("무승부입니다!")  # 무승일 경우 게임 머니 변화 없음
    elif me > computer:  # 내가 승리했을 경우
        if me % 2 != 0 and computer % 2 != 0:
            print("나와 컴퓨터의 숫자가 모두 홀수입니다! 내가 2배의 베팅 머니를 가져갑니다!")
            my_money += bet_money*2
            computer_money -= bet_money*2
        else:
            print("나의 승리!")
            my_money += bet_money
            computer_money -= bet_money
    elif computer > me:  # 컴퓨터가 승리했을 경우
        if me % 2 != 0 and computer % 2 != 0:
            print("나와 컴퓨터의 숫자가 모두 홀수입니다! 컴퓨터가 2배의 베팅 머니를 가져갑니다!")
            my_money -= bet_money*2
            computer_money += bet_money*2
        else:
            print("컴퓨터의 승리!")
            my_money -= bet_money
            computer_money += bet_money

    if my_money == 0 or computer_money == 0:
        break
    i = i + 1

winner = "나" if my_money > computer_money else "컴퓨터"
print("\n게임 종료 - " + winner +"의 승리")