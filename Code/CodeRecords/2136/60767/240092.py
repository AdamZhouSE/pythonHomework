def getKpresentation(num,k):
    res = []
    while(num>=1):
        temp = num%k
        res.append(temp)
        num = int(num/k)
    if(len(res)==res.count(1)):
        return True
    return False

num = int(input())
for i in range(2,num+1):
    if(getKpresentation(num,i)):
        print(i)
        break
