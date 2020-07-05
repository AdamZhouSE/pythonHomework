n=int(input())
string=input()
for i in range(0,n):
    x=input().split()
    if x[0]=='1':
        string=string+x[1]
        print(string)
    elif x[0]=='2':
        
        string=string[int(x[1]):int(x[1])+int(x[2])]
        print(string)
    elif x[0]=='3':
        
        y=list(string)
        y.insert(int(x[1]),x[2])
        string="".join(y)
        print(string)
    else:
        
        find=string.find(x[1])
        print(find)