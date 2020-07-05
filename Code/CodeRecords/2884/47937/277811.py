a=input().split(" ")
n=int(a[0])
k=int(a[1])

#print(n)
#print(k)

b=input().split(" ")
#print(b)

i=0
shuzu=[]
while i<len(b):
    shuzu.append(int(b[i]))
    i=i+1
#print(shuzu)

i=0
j=0
result=0

while i<len(shuzu):
    j=i+1
    while j<len(shuzu):
        if(abs(shuzu[i]-shuzu[j])<=k):
            result+=2
        j=j+1
    i=i+1
print(result)
        





















