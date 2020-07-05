input1=input().split()
input2=input().split()
sub=int(input1[0])
hours=int(input1[1])
mul1=list(range(sub))
sum=0
for i in range(sub):
    mul1[i]=int(input2[i])
mul1.sort()
for i in range(sub):
    sum+=hours*mul1[i]
    if hours!=1:
        hours=hours-1
print(sum)