def yuanFen(res):
    li = []
    while int(res)>100:
        temp=res
        res = ""
        for i in range(0,len(temp)-1):
            res+=str((int(temp[i])+int(temp[i+1]))%10) 
        if(res=='01'):
            return 1
        if(int(res)<100 or int(res)==100):
            return res
    return res
abb = input()
ST  = int(input())
newS = ""
for i in abb:
    d=ord(i)-ord('A')
    newS+=(str(ST+d))
res = newS  
print(yuanFen(res),end='')
