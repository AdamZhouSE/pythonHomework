inp=eval(input())
n=inp[0]
m=inp[1]
pro=0
for i in range(n,m+1):
    pro^=i
if(pro==1):
    pro=0
print(pro)
