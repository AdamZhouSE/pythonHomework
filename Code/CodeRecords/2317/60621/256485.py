b=[int(x) for x in input().split(",")]
b.sort()
total=0
for i in range(len(b)-1):
    j=i+1
    while j < len(b):
        k=2**(j-i-1)
        total+=(k*(b[j]-b[i]))
        j+=1
total%=(1000000000+7)
print(total)