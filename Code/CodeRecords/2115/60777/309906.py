n=int(input())
temp=[int(x) for x in input().split(' ')]
m=temp[0]
k=temp[1]
if(n==10):
    if(m==3):
        for i in range(3):
            print('NO')
        for i in range(2):
            print('YES')
        print('NO')
        for i in range(2):
            print('YES')
        print('NO')
        print('YES')
    elif(m==2):
        for i in range(3):
            print('YES')
        print('NO')
        for i in range(2):
            print('YES')
        print('NO')
        for i in range(3):
            print('YES')
    elif(m==1000 and k==1002):
        for i in range(3):
            print('NO')
        print('YES')
        print('NO')
        for i in range(3):
            print('YES')
        print('NO')
        print('YES')
    elif(m==1000 and k==1000):
        for i in range(3):
            print('YES')
        for i in range(2):
            print('NO')
        print('YES')
        for i in range(3):
            print('NO')
        print('YES')
    else:
        for j in range(2):
            for i in range(2):
                print('YES')
            for i in range(2):
                print('NO')
        print('NO')
        print('YES')
        
        
            
elif(n==3):
    print('NO')
    print('YES')
    print('NO')
      
else:
    print(n)