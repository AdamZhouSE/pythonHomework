cnt=int(input())
people=int(input())
arr=[]
i=1
index=0
while cnt>0:
    if(len(arr)<people):
        arr.append(i)
    else:
        arr[index]+=i
    index += 1
    index %= people
    cnt -= i
    i+=1
    if cnt<i:
        i=cnt
if len(arr)<people:
    k=people-len(arr)
    for i in range(0,k):
        arr.append(0)
print(arr)