a=eval(input())
count=0
for i in range(len(a)):
    j=i+1
    while j<len(a):
        if(a[i]>2*a[j]):
            count+=1
        j+=1
print(count)