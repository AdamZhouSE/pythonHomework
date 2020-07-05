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
answer=0
for i in range(n-2):
    if ar[i]==0:
        continue
    else:
        if ar[i]==1:
            if ar[i+1]==0 and ar[i+2]==1:
                ar[i+2]=0
                answer+=1
print(answer)