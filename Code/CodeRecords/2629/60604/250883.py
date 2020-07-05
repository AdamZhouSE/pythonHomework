'''
0    1    1  
1    3    12
2    7    1223
3    15    1223 2334
4    31    1223 2334 2334 3445 
5    43    1223 2334 2334 3445
6    63    1223 2334 3445 4556 5667
7    87    
8    115   1223 2334 3445 4556 5667 6778 7889
'''
def num(x):
    if x==1:
        return 0
    elif x<=3:
        return 1
    else:
        i=4
        now=3
        while True:
            now+=i
            if x<=now:
                return i//4+1
            else:
                i+=4
#for i in range(1,29):
#    print(num(i))
t=int(input())
for i in range(t):
    x=int(input())
    print(x)
    tmp=num(x)
    stan=[1,2,2,3]
    for i in range(len(stan)):
        stan[i]+=(tmp-2)
    print(num(x))
    print(stan)
    if tmp==0:
        print(1)
    elif tmp==1:
        if x==2:
            print(1)
        else:
            print(2)
    else:
        x1=x+1
        while(True):
            if num(x1)>num(x):
                x1-=1
                break
            x1+=1
        print(x1)
        dif=x1-x
        dif=dif//4
        print(dif)
        pl=3-(x1-x)%4
        print(pl)
        print(stan[pl]-dif)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        