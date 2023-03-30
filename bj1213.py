word = input()
word_list = list(word)
result = [0 for _ in range(len(word_list))]
word_list.sort()
count = 0
for i in range(0, len(word_list)-1, 2):
    if word_list[i] == word_list[i+1]:
        print(i)
        result[count] = word_list[i]
        result[-(count+1)] = word_list[i]
        count += 1
        print(result)
        if i + 2 >= len(word_list) - 1:
            print("".join(str(result)))
    else:
        if i == (len(word_list)//2) + 1:
            print("result")
            print(result)
            result[count] = word_list[i]
            count += 1
        else:
            print('I\'m Sorry Hansoo')
            break
