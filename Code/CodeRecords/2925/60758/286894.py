n=int(input())
in_=list(map(int,input().split()))
out_=list(map(int,input().split()))
visited=[]
count=0
for i in range(n-1):
    for j in range(i+1,n):
        if out_.index(in_[i])>out_.index(in_[j]) and in_[j]not in visited:
            visited.append(in_[j])
            count+=1
print(count)