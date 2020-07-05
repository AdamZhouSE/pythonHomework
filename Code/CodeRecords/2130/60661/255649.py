n=int(input())
if n < 10:
    print(n)
    exit()
s='9';temp=9
while n>temp:
    s+='0'
    temp+=int(s)*len(s)
n=n-(temp-int(s)*len(s))-1
div=int(n/len(s))
mod=n%len(s)
resNum=int('1'+(len(s)-1)*'0')+div
print(int(str(resNum)[mod]))
