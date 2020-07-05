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
            flag = L
            for x in temp:    
                if temp.count(x)!=1:
                    flag = flag-1
            if flag==L:
                array.append(temp)
        SumOfLen = SumOfLen+len(array)*L
        array.clear()
    print(int(SumOfLen))

