t=int(input())
for test in range(t):
    str=input()
    count=0
    for i in str:
        if i=='(':
            count+=1
            print(count)
        if i==')':
            
            print(count)
            count-=1
                          
                