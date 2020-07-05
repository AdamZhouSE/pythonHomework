n=int(input())
for i in range(0,n):
    out=0
    x=int(input())
    string=""
    while(x>0):
        string+=str(x%2)
        x=int(x/2)
    if(string.count('1')==1):
        print(string.index('1')+1)
    else:
        print(-1)