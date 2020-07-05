list1=eval(input())
count=0
for i in range(0,len(list1)-1):
    x=list1[i]
    for j in range(i+1,len(list1)):
        y=list1[j]
        if(x>2*y):count+=1
print(count)