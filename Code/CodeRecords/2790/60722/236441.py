string=input().split(" ")
n=int(string[0])
m=int(string[1])
a=input().split(" ")
b=input().split(" ")
result=""
for i in range(n):
    a[i]=int(a[i])
for j in range(m):
    b[j]=int(b[j])
for j in range(m):
    num=0
    for i in range(n):
        if a[i]<=b[j]:
            num+=1
    result+=str(num)
    result+=" "
print(result[0:len(result)-1])