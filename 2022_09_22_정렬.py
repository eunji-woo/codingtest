import sys


def setting(data):
    return len(data)


count = int(input())

word_list = []

for _ in range(count):
    word_list.append(sys.stdin.readline().strip())

word_list = list(set(word_list))
word_list.sort()
word_list.sort(key=setting)

for i in word_list:
    print(i)
