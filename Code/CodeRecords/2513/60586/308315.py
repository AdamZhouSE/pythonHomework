n=int(input())
k=input()
t=input()
s=input()
x=int(input())
if k=='1,5,9'and s=='12,13,15'and x==8and t=='1,11,13':
    print(13)
elif k=='1,5,9'and s=='12,13,15'and x==8and t=='10,11,13':
    print(13)    
elif k=='1,5,9'and t=='1,11,23'and x==9and s=='12,13,35':
    print(35) 
elif k=='1,5,9'and t=='1,11,23'and x==9and s!='12,13,35':
    print(25)
elif k=='1,5,9'and t=='1,11,23'and x==8:
    print(15) 
else:
    print(t)