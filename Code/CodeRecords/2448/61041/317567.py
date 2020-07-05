arr=eval(input())
sortedArr=sorted(arr,reverse=True)
i=0
while i<len(sortedArr):
    if i+1<=sortedArr[i]:i+=1
    else:break
print(i)