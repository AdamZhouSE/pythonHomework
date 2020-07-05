l=input().split(" ")
n=int(l[0])
m=int(l[1])
a=input().split(" ")
b=input().split(" ")
for i in range(n):
    a[i]=int(a[i])
a.sort()
result=""
for i in range(m):
    b[i]=int(b[i])
    num=0
    for j in range(n):
        if a[j]<=b[i]:
            num+=1
    result+=str(num)
    result+=" "
    
print(result[0:len(result)-1])    