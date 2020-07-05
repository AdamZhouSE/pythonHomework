class Larger()

arr=eval(input())
k=eval(input())
n=len(arr)
fra=[]
for i in range(0,n-1):
    for j in range(1,n):
        fra.append([arr[i],arr[j]])
fra=sorted(fra,key=)