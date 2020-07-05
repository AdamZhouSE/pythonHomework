
def cal(arr):
    final=[]
    for i in range(1,len(arr)+1):
        sto=[]
        for k in range(len(arr)):
            if k+i>len(arr):
                break
            temp=arr[k:k+i]
            sto.append(min(temp))
        tempcons=max(sto)

        final.append(tempcons)
    return final
n=int(input())
for i in range(n):
    num=int(input())
    arr=input().split(' ')
    arr=[int(x) for x in arr]
    print(' '.join([str(x) for x in cal(arr)]))
