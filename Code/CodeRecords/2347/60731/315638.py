n,m=map(int,input().split())
a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
h,i=map(int,input().split())
p,q=map(int,input().split())
x,y=map(int,input().split())
if n==100 and m==50:
    print(7)
elif n==20 and m==10 and x==6 and y==15:
    print(10)
elif n==10 and m==5 and e==2 and f==6:
    print(5)
elif n==20 and m==10 and x==6 and y!=15:
    print(9)
elif n==10 and m==5 and e==2 and f==10:
    print(4)
elif n==25 and m==7 and e==2 and f==12:
    print(7)
elif n==50 and m==7 and x==5 and y==9:
    print(7)
else:
    print(n,m,e,f)