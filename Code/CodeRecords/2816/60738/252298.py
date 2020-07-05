n=int(input())
num_list=list(map(int,input().split()))
num_list.sort()
for i in range(n-1):
    if i%2==0:
        num_list.pop()
    if i%2==1:
        del num_list[0]
print(num_list[0])