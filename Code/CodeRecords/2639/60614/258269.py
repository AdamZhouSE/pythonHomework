str=input()
time=int(input())
maximum=0
for i in range(len(str)):
    key=str[i]
    length=0
    temp=time
    for j in range(i,len(str)):
        if str[j]==key:
            length+=1
        else:
            if temp==0:
                break
            else:
                temp-=1
                length+=1
    if length>maximum:
        maximum=length
print(maximum)