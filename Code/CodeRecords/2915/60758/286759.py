n=int(input())
pro=list(map(int,input().split()))
max_len=1
current_len=1
for i in range(n-1):
    if(pro[i]*2>=pro[i+1]):
        current_len+=1
        max_len=max(current_len,max_len)
    else:
        current_len=1
print(max_len)