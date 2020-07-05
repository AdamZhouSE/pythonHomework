num=int(input())
s=input().split(' ')
s=list(map(int,s))
ji=0
ou=0
for i in range(len(s)):
    if(s[i]%2)==0:
        ou+=1
    else:
        ji+=1
if(ji%2)!=0:
    print("NO")
else:
    print("YES")