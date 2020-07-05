te=[int(x) for x  in input().split()]
num=te[0]
a=te[1]
array=[int(x) for x  in input().split()]
for i in range(a):
    temp=[int(x) for x  in input().split()]
    if temp[0]==0:
        now=array[temp[1]:temp[2]+1]
        now.sort()
        array[temp[1]:temp[2] + 1]=now
    else:
        now = array[temp[1]:temp[2] + 1]
        now.sort(reverse=True)
        array[temp[1]:temp[2] + 1] = now
q=eval(input())
print(array[q])