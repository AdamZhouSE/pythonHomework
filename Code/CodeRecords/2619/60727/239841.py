def luckyNumber(num):
    li = num.split()
    le = len(li)
    if "0" in li:
        return 0
    for i in range (0,le):
        for j in range (0,le):
            if int(li[i]) == int(li[j]) and i!=j:
                return 0
    
        
    return 1

sum = int(input())
for i in range(0,sum):
    print(luckyNumber(input()))