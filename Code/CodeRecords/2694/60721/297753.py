s=input()
lis=[]
for i in range(1,len(s)):
    for j in range(0,len(s)):
        if(j+i>len(s)):
            break
        lis.append(s[j:j+i])
for i in range(0,len(lis)):
    if(lis.count(lis[len(lis)-1-i])>1):
        print(lis[len(lis)-1-i],end="")
        break
print()