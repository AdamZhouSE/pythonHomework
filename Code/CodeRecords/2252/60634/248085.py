def march(position,s,wList):
    size = len(wList)
    i = 0
    while i < size:
        j = 0
        while j <= len(wList):
            if j == len(wList):
                return 0
            if wList[j] == s[position+i]:
                wList.remove(wList[j])
                break
            j += 1
        i += 1
    return 1

problems = int(input())
for x in range(problems):
    s = input()
    w = input()
    count = 0
    
    i = 0
    while i <= len(s) - len(w):
        count += march(i,s,list(w))
        i += 1
        
    print(count)
    
    
    