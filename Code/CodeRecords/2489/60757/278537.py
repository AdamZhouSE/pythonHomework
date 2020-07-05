arr=eval(input())
lower=int(input())
upper=int(input())
count=0
for i in range(len(arr)):
    cal=0
    for j in range(i,len(arr)):
        cal=cal+arr[j]
        if (cal>=lower) and (cal<=upper):
            count=count+1
print(count)