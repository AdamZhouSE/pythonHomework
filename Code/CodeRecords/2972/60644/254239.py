num=int(input())
arr=[]
res=[]
for i in range(0,num*2):
    arr=arr+[input()]
k=0
b=False
for p in range(0,num):
    k=0
    for i in range(0,len(arr[2*p])):
        b = False
        for j in range(0,len(arr[2*p+1])):
            j=j+k
            if arr[2*p][i:i+1]==arr[2*p+1][j:j+1]:
                if arr[2*p][i:i+1]==arr[2*p+1][j+1:j+2]:
                    break
                else:
                    b=True
                    k=j
                    break
        if not b:
            break
    if b:
        print('Yes')
    else:
        print('No')




