n=int(input())
a=list(map(int,input().split()))
num_of_n1=0
steps=0
for i in a:
    if i==-1:
        num_of_n1+=1
    else:
        steps=steps+int(abs(i-1))
steps+=num_of_n1%2
print(steps)