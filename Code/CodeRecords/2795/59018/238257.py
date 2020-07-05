n=int(input())
info=input().split(' ')
a=[int(y) for y in info]

def find(a):
    for i in range(100):
        c1=a[0]
        c2=a[0]+i
        c3=a[0]-i
        flag1=1
        for j in range(1,len(a)):
            if a[j]=int or a[j]+i=int or a[j]-i=int:
                continue
            else:
                flag1=0
                break
        flag2=1        
        for j in range(1,len(a)):
            if a[j]=int or a[j]+i=int or a[j]-i=int:
                continue
            else:
                flag2=0
                break
        flag3=1        
        for j in range(1,len(a)):
            if a[j]=int or a[j]+i=int or a[j]-i=int:
                continue
            else:
                flag3=0
                break
         
        if flag1==1 or flag2==1 or flag3==1:
            return i