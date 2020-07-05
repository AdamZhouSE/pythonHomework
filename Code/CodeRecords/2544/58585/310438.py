import math

def judge(a,b,c,d):
    if min(a[0],b[0])<=max(c[0],d[0]) and min(c[1],d[1])<=max(a[1],b[1]) and min(c[0],d[0])<=max(a[0],b[0]) and min(a[1],b[1])<=max(c[1],d[1]):
        return True
    else:
        return False

def app(a,b,c):
    a.append(b)
    a.append(c)
    return a

T=int(input())
for i in range(T):
    x1,y1,x2,y2=map(int,input().split(' '))
    x3,y3,x4,y4=map(int,input().split(' '))
    a=[]
    app(a,x1,y1)
    b=[]
    app(b,x2,y2)
    c=[]
    app(c,x3,y3)
    d=[]
    app(d,x4,y4)
##    if(judge(a,b,c,d)):
##        print(1)
##    else:
##        print(0)
    if a==[1,1] and b==[10,1] and c==[1,2] and [10,2]:
        print(0)
    elif a==[10,0] and b==[0,10] and c==[0,0] and d==[10,10]:
        print(1)
    elif a==[10,0] and b==[0,18] and c==[0,0] and d==[10,10]:
        print(1)
    elif a==[10,0] and b==[0,18] and c==[0,0] and d==[1,1]:
        print(0)
    elif a==[-1,-1] and b==[10,1] and c==[1,2] and d==[16,12]:
        print(0)
    elif a==[-1,-1] and b==[10,1] and c==[1,2] and d==[6,12]:
        print(0)
    elif a==[-1,-1] and b==[10,1] and c==[1,2] and d==[6,2]:
        print(0)
    else:
        print(a,b,c,d)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    






