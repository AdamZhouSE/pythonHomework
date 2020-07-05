T=int(input())
for i in range(0,T):
    num=int(input())
    str=bin(num)
    str=str[2:]
    if len(str)%2==1:
        str='0'+str
    n=0
    re=""
    while n<len(str):
        re=re+str[n+1]+str[n]
        n=n+2
    re='0b'+re
    print(eval(re))
