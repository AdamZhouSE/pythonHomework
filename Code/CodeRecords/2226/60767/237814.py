def isSelfDiv(num):
    s = str(num)
    for x in s:
        if(x=="0"):
            return False
    for x in s:
        if(num%int(x)!=0):
            return False
    return True

right = int(input())
left = int(input())
result = []
for i in range(right,left+1):
    if(isSelfDiv(i)):
        result.append(i)
print(result)