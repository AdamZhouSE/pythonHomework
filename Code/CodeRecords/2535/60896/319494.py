a=eval(input())
n=len(a)
i=0
j=1
count=1
while(j<n):
    list1=a[i:j]
    list2=a[j:]
    if(max(list1)<min(list2)):
        count+=1
        i=j
        j=i+1
    else:
        j+=1
print(count)