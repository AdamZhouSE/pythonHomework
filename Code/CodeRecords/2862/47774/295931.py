n=int(input())
even=[0 for i in range(n)]
odd=[0 for i in range(n)]
ss=input()
x=[int(i) for i in ss.split(' ')]
a,b,cnt=0,0,0
for i in x:
    cnt+=i
    if i%2==0:
        even[a]=i
        a+=1
    else:
        odd[b]=i
        b+=1
even.sort()
odd.sort()
even=even[::-1]
odd=odd[::-1]
if a>b:
    for i in range(b):
        cnt-=odd[i]
        cnt-=even[i]
    cnt-=even[b]
elif a<b:
    for i in range(a):
        cnt-=odd[i]
        cnt-=even[i]
    cnt-=odd[a]
else:
    cnt=0
print(cnt)
    