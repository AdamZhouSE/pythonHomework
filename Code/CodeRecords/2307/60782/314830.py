times = int(input())
while times > 0:
    times = times - 1
    quantity = int(input())
    num = []
    num = [int(n) for n in input().split()]
    standard = float(quantity) / 2.0
    # dic = {}
    word = []
    for item in num:
        counter = 0
        for partners in num:
            if partners == item:
                counter = counter + 1
        if (float(counter) >= standard and item not in word):
            # dic.update({item:counter})
            word = word + [item]
    if len(word) == 0:
        print(-1)
    else:
        for i in range(len((word)) - 1):
            # print(dic[word[i]],end=" ")
            print(word[i], end=" ")
        if times > 0:
            # print(dic[word[len(word) - 1]],end='\n')
            print(word[len(word) - 1], end="\n")
        else:
            print(word[len(word) - 1])

