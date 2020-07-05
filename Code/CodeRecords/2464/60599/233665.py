num=int(input())
s=input()
arr=list(map(int, s.split(',')))
sum = 0
count = 0
minCount = 0
for i in range(len(arr)):
    for k in range(i+1,len(arr)+1):
        sum += arr[i]
        count += 1
        if(sum>=num):
            if(minCount==0):
                minCount=count
                break
            minCount = min(minCount,count)
            break
    count = 0
    sum = 0
print(minCount)