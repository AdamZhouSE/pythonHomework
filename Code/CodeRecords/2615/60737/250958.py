t = int(input())
while t:
    s = list(input())
    s.sort(reverse=True)
    subs = [s[i:i+x+1] for x in range(len(s)) for i in range(len(s)-x)]
    temp = []
    for i in subs:
        if len(i) == 1:
            temp.append(''.join(i))
        else:
            diff = ord(i[1]) - ord(i[0])
            k = 1
            for j in range(1, len(i)-1):
                if ord(i[j+1]) - ord(i[j]) != diff:
                    k = 0
            if k:
                temp.append(''.join(i))
    temp.sort(key = lambda i:len(i),reverse=True)
    print(temp[0])
    t -= 1
    