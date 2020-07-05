nstr=input()
n=len(nstr)
i=0
while nstr[i]==' ':
    i+=1
nstr=nstr[i:]
isN=0
isNum=1
if nstr[0]=='-':
    isN=1
    nstr=nstr[1:]
elif nstr[0].isdigit()==False:
    isNum=0
if isNum==0:
    print(0)
else:
    i=0
    while i<len(nstr):
        if nstr[i].isdigit():
            i+=1
        else:
            break
    nums=nstr[:i]
    if isN==1:
        nums='-'+nums
    if int(nums)<-2147483648:
        print(-2147483648)
    elif int(nums)>2147483647:
        print(2147483647)
    else:
        print(int(nums))