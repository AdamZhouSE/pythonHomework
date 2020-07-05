n,q=map(int,input().split(' '))
arr=list(map(int,input().split(' ')))
query=[]
for i in range(q):
    query.append(list(map(int,input().split(' '))))
frequency=[0]*n
for i in query:
    for j in range(i[0]-1,i[1]):
        frequency[j]+=1
handle_arr=[0]*n
for i in range(n):
    temp1=frequency.index(max(frequency))
    temp2=arr.index(max(arr))
    handle_arr[temp1]=arr[temp2]
    frequency[temp1]=-1
    arr[temp2]=-1
sum=0
for i in query:
    for j in range(i[0]-1,i[1]):
        sum+=handle_arr[j]
print(sum)
