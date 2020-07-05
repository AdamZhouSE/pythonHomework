t = int(input())
while t:
    s = input()
    subs = [s[i:i+x+1] for x in range(len(s)) for i in range(len(s)-x)]
    count = 0
    for i in subs:
        count0 = 0
        count1 = 0
        count2 = 0
        for j in range(len(i)):
            if i[j] == '0':
                count0 += 1
            elif i[j] == '1':
                count1 += 1
            else:
                count2 += 1
        if count0 == count1 and count0 == count2:
            count += 1
    print(count)
    t -= 1
    