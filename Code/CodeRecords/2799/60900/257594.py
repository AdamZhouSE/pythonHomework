n = input()
str = input().split(" ")
for i in range (0,int(n)):
    str[i] = int(str[i])
    
str=list(set(str))

result1 = []
for i in range(0,len(str)):
    result="NO"
    for j in range(0,len(str)):
        temp1=max(str[j],str[i])
        temp2=min(str[j],str[i])
        if ((temp1/temp2)%2==0)or((temp1/temp2))%3==0:
            result="YES"
            break
    result1.append(result)


if list(set(result1))==["YES"]or(len(str)==1):
    print("Yes")
else:
    print("No")