n=int(input())
arr=[int(x) for x in input().split(" ")]
odd=[]
even=[]
for i in arr:
    if i%2==1:odd.append(i)
    else:even.append(i)
odd.sort(reverse=True)
even.sort(reverse=True)
if len(odd)==len(even):print(0)
elif len(odd)<len(even):
    result=0
    for i in range(len(odd)+1,len(even)):
        result+=even[i]
    print(result)
else:
    result = 0
    for i in range(len(even)+1, len(odd)):
        result += odd[i]
    print(result)