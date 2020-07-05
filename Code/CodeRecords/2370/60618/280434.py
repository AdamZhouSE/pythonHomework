n=input()
string=[]
while n!=0:
    if n%(-2)!=0:
        string+='1'
    else:
        string+='0'
    n=n//(-2)
string.reverse()
print(string)