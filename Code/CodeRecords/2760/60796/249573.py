n=int(input())
result=[]
while n>0:
    ls=[]
    ls=input().split(" ")
    ls=[int(x) for x in ls]
    if ls[0]%2==0:
        result.append(ls[0]/2*ls[1])
    else:
        result.appeng((ls[0]/2-1)*ls[1])
    n=n-1

for i in range(len(result)):
    print(result[i])