n = int(input())

list24=[]

for i in range(0,n):
    k=int(input())
    list18=input().split()
    lenn=len(list18)
    for j in range(0,lenn):
        list18[j]=int(list18[j])
    list18.sort()    
    if lenn%2==0:
        print(int((list18[int(lenn/2)]+list18[int(lenn/2)-1])/2))
    else:
        print(list18[int((lenn-1)/2)])
    