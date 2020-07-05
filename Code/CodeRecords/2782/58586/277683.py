n=int(input())
arr=[]
def getMinDif(arr,i):
    if len(arr)==0:
        return i
    else:
        res=10000007
        for n in arr:
            res=min(res,abs(n-i))
        return res
sum=0
for i in range(n):
    num=int(input())
    sum+=getMinDif(arr,num)
    arr.append(num)
print(sum,end='')