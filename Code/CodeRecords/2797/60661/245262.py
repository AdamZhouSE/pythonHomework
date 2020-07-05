n=int(input())
days=input().split(' ')
days=[int(x) for x in days]
if n<=1:
    if days[0]!=0 and days[0]!=15:
        print(-1)
    elif days[0]==0:
        print('UP')
    else:
        print('DOWN')
    exit()
if days[n-1]>days[n-2]:
    if 0<=days[n-1]<=14:
        print('UP')
    else:
        print('DOWN')
elif days[n-1]<days[n-2]:
    if 1<=days[n-1]<=15:
        print('DOWN')
    else:
        print('UP')