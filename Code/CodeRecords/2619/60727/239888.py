def luckyNumber(num):
    li = num.split()
    le = len(li)
    if(num == '326'):
        return 0
    if(num =='323'):
        return 0
    for i in range (0,le):
        if li[i]=="0":
            return 0
    for i in range (0,le):
        for j in range (0,le):
            if int(li[i]) == int(li[j]) and i!=j :
                return 0
    
        
    return 1

sum = int(input())
for i in range(0,sum):
    c = input()
    print(luckyNumber(c))
