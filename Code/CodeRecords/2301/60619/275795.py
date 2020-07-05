dictionary = []
t = int(input())
for ind in range(t):
    li = input().strip().split(" ")
    instruc = int(li[0])
    word = li[1]
    if instruc == 1:
        dictionary.append(word)
    elif instruc == 2:
        if word in dictionary:
            del(dictionary[dictionary.index(word)])
    elif instruc == 3:
        if word in dictionary:
            print("YES")
        else:
            print("NO")
    elif instruc == 4:
        result = 0
        for w in dictionary:
            if w.startswith(word):
                result += 1
        print(result)