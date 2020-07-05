n=int(input())
for i in range(0,n):
    m=int(input())
    n=int(input())
    reslist=str(m/n).split('.')
    if reslist[1]=='0':
        print(reslist[0])
    elif len(reslist[1])<16:
        print(m/n)
    else:
        print(reslist[0]+'.('+reslist[1][0]+')')