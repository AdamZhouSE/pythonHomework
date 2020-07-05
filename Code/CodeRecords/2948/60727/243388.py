abb = input()
ST  = int(input())
newS = ""
for i in abb:
    d=ord(i)-ord('A')
    newS+=(str(ST+d))
res = newS
while len(res)>2 and res!='100':
    temp=res
    res = ""
    for i in range(0,len(temp)-1):
        res+=str((int(temp[i])+int(temp[i+1])%10))
        
print(res)
