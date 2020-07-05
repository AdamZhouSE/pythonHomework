n=int(input())
arr=input().strip().split(' ')
arr=[int(i) for i in arr]



tableSocks=0
tablearr=[]
for i in arr:
    if i not in tablearr:
        tablearr.append(i)
    else:
        tablearr.remove(i)
    if len(tablearr)>tableSocks:
        tableSocks=len(tablearr)
print(tableSocks)