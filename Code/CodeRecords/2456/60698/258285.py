# 7
a=list(eval(input()))
count=[]
for i in range(0,len(a)-1):
    count.append(0)
    for j in range(i+1,len(a)):
        if a[j]<a[i]:
            count[i]=count[i]+1
count.append(0)
print(count)