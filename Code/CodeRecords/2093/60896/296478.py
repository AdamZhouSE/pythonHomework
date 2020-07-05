n=eval(input())
k=eval(input())
list1=[]
result=[]
n1=n
for i in range(1,n+1):
    list1.append(i)
while(True):
    fib=1
    for i in range(1,n1):
        fib=fib*i
    n1-=1
    j=int(k/fib)
    k=int(k%fib)
    if(k!=0):j+=1
    result.append(list1[j-1])
    list1.remove(list1[j-1])
    if(k==0):
        result+=list1
        break
for i in range(0,n):
    print(result[i],end='')
print('')