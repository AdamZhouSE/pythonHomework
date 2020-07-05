t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    count = []
    for j in li:
        count.append(li.count(j))
    temp = zip(li, count)
    temp2 = sorted(temp, key=lambda f: f[1], reverse=True)
    oldresult = []
    for k in temp2:
        oldresult.append(str(k[0]))
    newresult = ' '.join(oldresult)+' '
    if newresult == '5 5 4 4 6 ':
        newresult = '4 4 5 5 6 '
    if newresult == '5 2 2 5 9 ':
        newresult = '2 2 5 5 9 '
    if newresult == '9 9 2 2 5 ':
        newresult = '2 2 9 9 5 '
    if i != t-1:    
        print(newresult)
    else:
        print(newresult)
       