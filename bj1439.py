s1 = input()
s2 = s1[0]

for i in range(1, len(s1)):
    if s2[-1] != s1[i]:
        s2 += s1[i]
    else:
        continue

if s2.count("0") >= s2.count("1"):
    print(s2.count("1"))
else:
    print(s2.count("0"))
    
# 000111000 -> 010 으로 보고 해도 됨
# for문으로 인접한 중복 문자열 제거하고
# 0이랑 1중에서 더 적은걸 뒤집으면 됨