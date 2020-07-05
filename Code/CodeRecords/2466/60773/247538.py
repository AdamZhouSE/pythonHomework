num = int(input())
l = []
for i in range(num):
    l.append(int(input()))
    l.append(input())
for i in range(num):
    check = l[2 * i + 1]
    sum = 0
    get = l[2 * i + 1].split(" ")
    s=[]
    for i in get:
        s.append(int(i))
    s.sort()
    result = []
    #print(s)
    for i in range(len(s)):
        for j in range(i + 1, len(s), 1):
            n1 = int(s[i]) + int(s[j])
            for k in range(j + 1, len(s), 1):
                if int(s[k]) < n1:
                    c = str(s[i]) + str(s[j]) + str(s[k])
                    #print(c)
                    result.append(c)
    result = list(set(result))

    print(len(result))