n,m=map(int,input().split())
l1=list(map(lambda x:1 if int(x)%2==1 else 0,input().split()))
l2=list(map(lambda x:1 if int(x)%2==1 else 0,input().split()))
print(min(sum(l1),len(l2)-sum(l2))+min(len(l1)-sum(l1),sum(l2)))