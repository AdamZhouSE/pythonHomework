n_time = list(map(int,input().split()))
books = list(map(int,input().split()))
max = 0
for i in range(n_time[0]-1):
    time = 0
    sum=0
    for j in range(i,n_time[0]):
        time = time+books[j]
        if time<= n_time[1]:
            sum=sum+1
        else:
            break
    if max<sum:
        max = sum
print(max)
            