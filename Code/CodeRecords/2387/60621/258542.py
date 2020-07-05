te=[int(x) for x  in input().split()]
num=te[0]
a=te[1]
array=[int(x) for x  in input().split()]
for i in range(a):
    temp=[int(x)-1 for x  in input().split()]
    if temp[0]==-1:
        now=array[temp[1]:temp[2]+1]
        now.sort()
        array[temp[1]:temp[2] + 1]=now
    else:
        now = array[temp[1]:temp[2] + 1]
        now.sort(reverse=True)
        array[temp[1]:temp[2] + 1] = now
q=eval(input())

print(array[q-1])