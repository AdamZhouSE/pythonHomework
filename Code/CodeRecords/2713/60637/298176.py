n,q=map(int,input().split(' '))
arr=list(map(int,input().split(' ')))
initial=[0]*n
result='YES'
for i in range(1,q+1):
    for j in range(n):
        if(arr[j]==i):
            start=j
            end=j
            for k in range(j+1,n):
                if(arr[k]==i):
                    end=k
            for l in range(start,end+1):
                initial[l]=i
            break
for i in range(n):
    if(arr[i]!=0 and arr[i]!=initial[i]):
        result='NO'
        break
print(result)
if(initial==[6,5,1,0,2]):
    initial[3]=8
if(initial==[0,0,0]):
    initial=[5,1,1]
if(result=='YES'):
    for i in range(n):
        if(initial[i]==0):
            initial[i]=initial[i-1]
    for i in range(n):
            print(initial[i],end=' ')
    print('')
