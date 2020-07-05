s=input()[1:-1].split(",")
for i in range(len(s)):s[i]=int(s[i])
num=int(input())

k=int(len(s)/2)
right=len(s)
left=0

while abs(left-k)>1 and abs(k-right)>1:
    if num>s[k]:
        left=k
        k=int((k+right)/2)
    else:
        right=k
        k=int((k+left)/2)
if s[k]!=num:print(-1)
else:print(k)