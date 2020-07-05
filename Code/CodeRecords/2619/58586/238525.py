nums=int(input())
def mul(str):
    re=1
    for c in str:
        re*=int(c)
    return re
for i in range(nums):
    str=input() 
    res=[]
    flag=True
    for step in range(1,len(str)):
        i=0
        while i<=len(str)-step:
            temp=mul(str[i:i+step])
            if temp not in res:
                res.append(temp)
            else:
                flag=False
                break
            i+=1
        if flag==False:
            print(0)
            break
    if flag==True:
        print(1)
