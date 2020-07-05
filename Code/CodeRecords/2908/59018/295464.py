def di(str1):
    dict0 = {}
    for i in range(len(str1)):
        if str1[i] not in dict0:
            dict0[str1[i]] = 1
        else:
            dict0[str1[i]] = dict0[str1[i]] + 1
    return dict0


def difference(N,a):
    res=0
    while(a!=[]):
        a=[i for i in a if i!=a[0]]
        res=res+1
    return str(res)+'  '


a=[]
N=int(input())
for j in range(N):
    str1=input()
    a.append(di(str1))

print(difference(N,a))