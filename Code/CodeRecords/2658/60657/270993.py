
def cal(arr,x):
    final=[]
    for i in arr:
        if i%x==0:
            final.append(i)
    if len(final)==0:
        return 0
    elif len(final)==1:
        return final[0]
    else:
        if len(arr)==2:

            return arr[0]|arr[1]
        temp=arr[0]|arr[1]
        for i in range(2,len(arr)):
            temp=temp|arr[i]
        return temp

n=int(input())
for i in range(n):
    num=input().split(' ')
    x=int(num[1])
    arr=input().split(' ')
    arr=[int(x) for x in arr]
    print(cal(arr,x))
