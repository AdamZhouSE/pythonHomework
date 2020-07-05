s=input()
str=input()
k=int(input())
result=[]
length=1
while length<=len(s):
    for i in range(0,len(s)-length+1):
        bad=0
        for j in range(i,i+length):
            if str[j]=='0':
                bad=bad+1
        if bad>k:
            continue
        else:
            result.append(s[i:i+length])
    length=length+1
temp=set(result)
result=list(temp)
num=len(result)
print(num)
        