n=int(input())
li=list(map(int,input().split()))
if li[len(li)-1]==0:
    print('UP')
elif li[len(li)-1]==15:
    print('DOWN')
elif n==1:
    print('-1')
else:
    if li[len(li)-1]-li[len(li)-2]>0:
        print('UP')
    elif li[len(li)-1]-li[len(li)-2]<0:
        print('DOWN')