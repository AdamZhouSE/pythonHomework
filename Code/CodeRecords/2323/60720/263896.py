list0=input().split(',')
list0=[int(list0[i]) for i in range(len(list0))]
list0.sort()
k=int(input())
result=list0[-1]-list0[0]-2*k
if result<0:
    result=0
print(result)