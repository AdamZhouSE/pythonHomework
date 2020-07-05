num=int(input())
l=list(map(int,input().split()))
s=sum(l)
if s%num!=0:
    print("NO")
else:
    for i in range(num-1):
        if abs(l[i]-s//num)!=abs(l[i+1]-s//num):
            print("NO")
            break
    else:
        print("YES")