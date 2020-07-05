import re
s=list(input())
exchange=list(map(int,re.sub("\D"," ",input()).split()))
for i in range(0,len(exchange)-1,2):
    if s[exchange[i]]>s[exchange[i+1]]:
        tem=s[exchange[i]]
        s[exchange[i]]=s[exchange[i+1]]
        s[exchange[i+1]]=tem
print("".join(str(j) for j in s))