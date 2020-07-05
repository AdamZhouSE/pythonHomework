l=eval(input())
sum=0
for i in range(len(l)):
    sum+=l[i]<<(len(l)-i-1)
print(sum)