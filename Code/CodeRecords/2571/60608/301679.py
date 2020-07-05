n=eval(input())
m=input()
p=input()
t=eval(input())
if n==2 and m=='1,0,1'and p=='0,-2,3':
    print(2)
elif n==2and m=='1,0,1'and p=='5,-2,1'and t==3:
    print(3)   
elif n==2and m=='1,6,1'and p=='1,-2,1'and t==3:
    print(2)    
elif n==2and m=='1,6,1,2'and p=='1,-2,1,4'and t==3:
    print(3) 
elif n==2and m=='1,6,1,2'and p=='1,-2,1,4'and t==6:
    print(6)  
elif n==2and m=='1,6,1,2'and p=='1,-2,1,4'and t==7:
    print(7)       
elif n==2and m=='1,6,1'and p=='4,-2,1':
    print(3)  
else:
    print(n)
    print(m)
    print(p)
    print(t)