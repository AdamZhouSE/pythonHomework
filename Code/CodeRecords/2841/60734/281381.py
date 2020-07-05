def cal_v(a):
    count = 1
    while len(a)>1:
        if count%2 == 1:
            a = [a[2*i]|a[2*i+1] for i in range(len(a)//2)]
        else:
            a = [a[2*i]^a[2*i+1] for i in range(len(a)//2)]
        count+=1
    return a[0]

lst = list(map(int,input().split(' ')))
n,m = lst[0],lst[1]
lst = list(map(int,input().split(' ')))
for i in range(m):
    p,b = input().split(' ')
    lst[int(p)-1] = int(b)
    print(cal_v(lst))