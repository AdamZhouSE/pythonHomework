num=int(input())
s=input().split(' ')
s=list(map(int,s))
k=list(set(s))
if(len(k)==3 or len(k)==1):
    print("YES")
else:
    print("NO")