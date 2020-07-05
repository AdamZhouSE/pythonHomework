input()
nums=list(map(int,input().split(' ')))
dict={}
dict[1]=0
dict[-1]=0
res=0
dict[0]=0
for i in nums:
    if i==0:
        dict[i]=dict.get(i)+1
    elif i>0:
        res+=(i-1)
        dict[1]=dict.get(1)+1
    else:
        res+=(-1-i)
        dict[-1]=dict.get(-1)+1
if dict[0]>=1:
    res+=dict[0]
    print(res)
else:
    if dict[-1]%2!=0:
        res+=2
        print(res)
    else:
        print(res)