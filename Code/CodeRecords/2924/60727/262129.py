def so(n,r,avg,lst):
    summ = 0
    line = avg*n
    for i in lst:
        summ+=i[0]
    if summ>=avg*n:
        return 0
    dis = line-summ

    for i in range(0,n):
        temp=lst[i][0]
        lst[i][0]=lst[i][1]
        lst[i][1]=temp
    lst = sorted(lst)
    res=0
    for i in range(0,n):
        if r-lst[i][1]+summ<line:
            res+=(r-lst[i][1])*lst[i][0]
            summ+=r-lst[i][1]
        else:
            res+=(line-summ)*lst[i][0]
            summ+=line-summ
        if summ==line:
            break
    return res
nums = input().split(' ')
n = int(nums[0])
r = int(nums[1])
avg = int(nums[2])
lst=[]
for i in range(0,n):
    data=input().split()
    data=list(map(int,data))
    lst.append(data)
print(so(n,r,avg,lst))
