n,m = [int(i) for i in input().split(' ')]
a = [int(i) for i in input().split(' ')]
x = 0
while(x<m):
    x += 1
    temp = input().split(' ')
    if(temp[len(temp)-1] == ''):
        temp.pop(-1)
    temp = [int(i) for i in temp]
    if temp[0] == 1:
        l,r,k,d = temp[1],temp[2],temp[3],temp[4]
        for i in range(l-1,r):
            a[i] += k + (i - l + 1)*d
    else:
        p = temp[1]
        print(a[p-1])
        