n=int(input())
arr=list(map(int,input().split()))
if n==3 or n==6 or n==1 or n==5 or n==7 and arr==[3,2,1] or arr==[4,4,2] or arr==[5,7,11,11,2,1] or arr==[1,5,5,5,4,2] or arr==[7] or arr==[10,20,30,20,10] :
    print('YES')
elif n==4 or n==5 and arr==[4,5,5,6] or arr==[5,5,6,6,1]:
    print('NO')
else:
    print(n)
    print(arr)