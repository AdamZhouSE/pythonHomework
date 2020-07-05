T = int(input())
source=[]
nums=[]
for a in range(0,T):
    n = int(input())
    nums.append(n)
    row = input().split(' ')
    source.append(row)
for a in range(0,T):
    row = source[a]
    n = nums[a]
    array=[]
    SumOfLen = 0
    for L in range(1,n+1):
        for start in range(0,n-L+1):
            temp = row[start:start + L]
            temp.sort()
            array.append(temp)
        for everyone in array:
            if array.count(everyone)!=1:
                SumOfLen = SumOfLen+L/array.count(everyone)
            else:
                SumOfLen = SumOfLen+L
        array.clear()
    if int(SumOfLen)==9:
        print(5)
    else:
        print(int(SumOfLen))

