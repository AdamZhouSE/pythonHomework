n=int(input())
for i in range(0,n):
    out=0
    x=int(input())
    string=""
    while(x>0):
        string+=str(x%2)
        x=int(x/2)
    while(len(string)<32):
        string+=str(0)
    for j in range(0,len(string)):
        if(string[j]=='0'):
            cal=1
        else:
            cal=0
        out+=cal*pow(2,j)
    print(out)