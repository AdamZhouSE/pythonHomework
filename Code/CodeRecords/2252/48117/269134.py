questNum = int(input())

for quest in range(questNum):
    s = input()
    c = list(input())
    realc = c
    count = 0
    for w in s:
        if w in c:
            del c[c.index(w)]
        else:
            c = realc
        
        if len(c) == 0:
            count += 1
    
    print(count)