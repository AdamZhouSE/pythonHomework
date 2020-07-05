n=int(input())
num=list(map(int,input().split()))
if(sum(num)%2==0):
    print("YES")
else:
    print("NO")