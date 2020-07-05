list1=eval(input())
output=0
count=0
for i in range(0,len(list1)-1):
    if list1[i]<list1[i+1]:
        count+=1
    else:
        output=max(output,count)
        count=0
print(output)    