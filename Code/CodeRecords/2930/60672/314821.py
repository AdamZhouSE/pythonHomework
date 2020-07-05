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
n=input()
ar=input()
ar=nums(ar)
total=0
for i in range(1,len(ar)-1):
    if ar[i]<ar[i-1] and ar[i]<ar[i+1]:
        total+=1
    elif ar[i]>ar[i-1] and ar[i]>ar[i+1]:
        total+=1
    else:
        continue
print(total)