first=input().split(" ")
length=int(first[0])
num=first[1]
str=input()
for i in range(0,length):
    temp=input().split(" ")
    str1=str[int(temp[0]):int(temp[1])+1]
    str2=str[int(temp[2]):int(temp[3])+1]
    Min=min(len(str1),len(str2))
    ans=0
    for j in range(0,Min):
        if str1[j]==str2[j]:
            ans+=1
        else:
            break
    print(ans)