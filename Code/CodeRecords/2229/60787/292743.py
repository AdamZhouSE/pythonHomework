n=eval(input())
a,b=0,0
for i in range(0,len(n)-1):
    if n[i]>n[i+1]:
        b+=1
    for j in range(i+1,len(n)):
        if n[i]>n[j]:
            a+=1
print(a==b)