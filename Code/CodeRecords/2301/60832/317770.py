n = int(input())

dictionary = {}
for i in range(n):
    temp = input().split()
    op = int(temp[0])
    word = temp[1]

    if op == 1:  # 增
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    elif op == 2:  # 删
        if word in dictionary:
            if dictionary[word] == 1:
                del dictionary[word]
            else:
                dictionary[word] -= 1
    elif op == 3:  # 查是否出现过
        if word in dictionary:
            print("YES")
        else:
            print("NO")
    elif op == 4:  # 查前缀出现过的次数
        l = len(word)
        ans = 0
        for w, num in dictionary.items():
            if w[:l] == word:
                ans += num
        print(ans)
