list1=eval(input())
output=1
count=1
for i in range(0,len(list1)-1):
    if list1[i]<list1[i+1]:
        count+=1
    else:
        output=max(output,count)
        count=1
print(output)    