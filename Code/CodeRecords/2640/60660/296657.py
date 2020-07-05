s=input()
t=input()
long=9999
result=''
for i in range(len(s)):
    for j in range(i,len(s)):
        flag=0
        for k in t:
            if k not in s[i:j+1]:
                flag=1
                break
        if flag==0 and j-i+1<long:
            long=j-i+1
            result=s[i:j+1]
print(result)