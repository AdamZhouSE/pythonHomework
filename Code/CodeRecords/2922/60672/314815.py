def nums(string):
    num='0123456789'
    nums=[]
    i=0
    while i<len(string):
        midstring=''
        k=0
        for j in range(i,len(string)):
            if string[j] in num:
                midstring+=string[j]
                k=k+1
            else:
                break
        if midstring!='':
            nums.append(int(midstring))
            midstring=''
            i=i+k
        else:
            i=i+1
            continue
    return nums
b=input()
ar=input()
ar=nums(ar)
maxe=max(ar)
mine=min(ar)
if (maxe-mine)%2==0 and len(list(set(ar)))<=3:
    print('YES')
else:
    print('NO')