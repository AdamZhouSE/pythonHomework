n=int(input())
num_list=list(map(int,input().split()))
k=int(input())
number=list(map(int,input().split()))
for i in range(k):
    for j in range(n):
        if j==n-1:
            print(n)
            break
        if number[i]>=sum(num_list[:j]) and number[i]<=sum(num_list[:j+1]):
            print(j+1)
            break
        