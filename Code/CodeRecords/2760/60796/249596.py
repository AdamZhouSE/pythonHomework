n=int(input())
result=[]
while n>0:
    ls=[]
    ls=input().split(" ")
    ls=[int(x) for x in ls]
    if ls[0]%2==0:
        result.append(int(ls[0]/2)*ls[1])#注意：要整除的话一定要前面加个int，不然15/2=7.5,而int(15/2)才=7
    else:
        result.append((int(ls[0]/2)+1)*ls[1])
    n=n-1

for i in range(len(result)):
    print(result[i])