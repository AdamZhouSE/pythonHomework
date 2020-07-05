t=int(input())
for test in range(t):
    str=input()
    count=0
    for i in str:
        if i=='(':
            count+=1
            print(count,end=" ")
        if i==')':
            
            print(count,end=' ')
            count-=1
                          
                