# 백준 11650

def setting0(data):
    return data[0]

def setting1(data):
    return data[1]


count = int(input())
coord = []

for _ in range(count):
    x_y = list(map(int, input().split()))
    coord.append(x_y)

coord.sort(key=setting1)
coord.sort(key=setting0)

for i in coord:
    print(i[0], i[1])

# 백준 1764
import sys

n, m = map(int, input().split())
nolisten = []
nosee = []

for _ in range(n):
    nolisten.append(sys.stdin.readline().strip())

for _ in range(m):
    nosee.append(sys.stdin.readline().strip())

answer = sorted(list(set(nolisten) & set(nosee)))

print(len(answer))

for i in answer:
    print(i)

# 백준 10825
def setting4(data): # 이름 사전 순 정렬
    return data[0]

def setting3(data): # 수학 점수가 내림차순으로 정렬
    return int(data[3])

def setting2(data): # 영어 점수가 오름차순으로 정렬
    return int(data[2])

def setting1(data): # 국어 점수가 내림차순으로 정렬
    return int(data[1])


count = int(input())
stu_info = []

for _ in range(count):
    stu_info.append(list(map(str, input().split())))

stu_info.sort(key=setting4)
stu_info.sort(key=setting3, reverse=True)
stu_info.sort(key=setting2)
stu_info.sort(key=setting1, reverse=True)

for i in stu_info:
    print(i[0])

# 백준 1302
import sys

count = int(input())
board = dict()

for _ in range(count):
    book = sys.stdin.readline().strip()
    if book in board:
        board[book] += 1
    else:
        board[book] = 1

max_value = max(board.values())
answer_list = []

for i in board.keys():
    if max_value == board[i]:
        answer_list.append(i)

answer_list.sort()

print(answer_list[0])



