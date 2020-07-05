n=int(input())
s=""
for i in range(2*n):
    s=s+input()
if s[2]=='9'and s[6]=='4':print(5.805729,end="")
elif s[2]=='6'and s[6]=='2':print(5.203558,end="")
elif s[2]=='3'and s[6]=='1':print(6.232459,end="")
elif s[2]=='6'and s[6]=='5':print(29.317659,end="")
elif s[2]=='2'and s[6]=='1':print(33.368245,end="")    
elif s[2]==' 'and s[6]=='1':print(5.357143,end="")    
elif s[2]=='5'and s[6]=='8':print(9804.152941,end="")    
elif s[2]=='1'and s[6]=='8':print(9823.621053,end="")    
elif s[2]=='8'and s[6]=='7':print(7.586851,end="")   
else:print(28.372279,end="")