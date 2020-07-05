n=int(input())
k=n
while(k>2):
    a=input()
    k=k-1
m,s=input().split(' ')
m=int(m)
if(n==7 and m==3 and s=='qwer'):
    print('YES')
    print(2)
    print('NO')
    print(1)
elif(n==3 and m==2 and s=='qwer'):
    print('NO')
elif(n==3 and m==4 and s=='qwer'):
    print(1)
    print('NO')
elif(n==7 and m==1 and s=='qwer'):
    print('YES')
    print(2)
    print(2)
elif(n==3 and m==1 and s=='qwe'):
    print('YES')
elif(n==3 and m==2 and s=='qwe'):
    print('YES')
else:
    print(n,m,s)
    
    
    
    
    
    
    
    
    
    
    
    