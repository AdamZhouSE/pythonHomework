pyin=input().split(',')
k=int(pyin[0])#k个数
n=int(pyin[1])#和
def swaped(arr):
    out = []
    for i in range(len(arr)):
        arr[i], arr[-1] = arr[-1], arr[i]
        out.append(arr[:])
        arr[-1], arr[i] = arr[i], arr[-1]
    return out


out = [[]]
point = 0
nums=[1,2,3,4,5,6,7,8,9]
a = []#所有排列结果


def perm(out, point, arr=nums):
    if point == len(arr):
        for i in out:
            a.append(i)
        return out
    t = []
    for i in out:
        i.append(arr[point])
        temp = swaped(i)
        for k in temp:
            t.append(k)
    out = t
    perm(out, point + 1)


perm(out, 0)

out=[]
for i in a:
    if sum(i[:k])==n:
        if sorted(i[:k]) not in out:
            out.append(sorted(i[:k]))
print(sorted(out))