problems = int(input())
for x in range(problems):
    temp = input().split(" ")
    sizeA = int(temp[0])
    sizeB = int(temp[1])
    k = int(temp[2])
    charryA = input().split(" ")
    charryB = input().split(" ")
    
    theNum = 0
    a = 0
    b = 0
    while k > 0:
        if int(charryA[a]) <= int(charryB[b]):
            theNum = charryA[a]
            a += 1            
        else:
            theNum = charryB[b]
            b += 1            
        k -= 1
    
    print(theNum)
    
        
    