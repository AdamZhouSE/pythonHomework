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
n=int(input())
ar=input()
ar=nums(ar)
num=0
table=[]
for i in range(n):
    nums=num
    if ar[i] in table:
        table.remove(ar[i])
        nums-1
    else:
        table.append(ar[i])
        nums+=1
    num=max(nums,num)
print(num)