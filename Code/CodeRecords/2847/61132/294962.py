n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
print(sum(l1[l2[0]-1:l2[1]-1]))