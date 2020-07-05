n=int(input())
a=list(map(int,input().split()))
num_of_n1=0
num_of_0=0
steps=0
for i in a:
    if i<0:
        steps=steps+(-1-i)
        num_of_n1+=1
    elif i==0:
        num_of_0+=1
    else:
        steps=steps+i-1
num_of_n1=num_of_n1%2
if num_of_n1>0:
    if num_of_0>0:
        steps+=num_of_0
    else:
        steps+=2
else:
    steps+=num_of_0
print(steps)