count=int(input())
list=[]
while count>0:  #count sub
    sum=0
    n=int(input())
    exp=1
    while sum<n:
        sum=sum+2**exp
        exp=exp+1
    exp=exp-1
    sum=sum-2**(exp)
    remain=n-sum-1
    token = []
    result = ''
    while remain>0:
        token.append(remain%2)
        remain=remain//2
    token.reverse()
    while len(token) <exp:
        token.insert(0,0)
    for i in token:
        if i ==0:
            result=result+'4'
        else:
            result=result+'7'
    list.append(result)
    count=count-1
for i in list:
    print(int(i))

