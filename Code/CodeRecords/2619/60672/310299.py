def lucky(num):
    n=len(num)
    nums=[]
    for i in range(n):
        for j in range(n):
            m=1
            if j+i>=n:
                break
            for k in range(i+1):
                m=m*int(num[j+k])
            nums.append(str(m))
    lnums=list(set(nums))
    if len(nums)==len(lnums):
        return 1
    else:
        return 0
    
t=int(input())
for i in range(t):
    num=input()
    answer=lucky(num)
    print(answer)