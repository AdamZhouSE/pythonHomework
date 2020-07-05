t=int(input())
ls=[]
while t>0:
    this=input()
    t=t-1
    ls.append(this.split(" "))
    ls[len(ls)-1]=[int(x) for x in ls[len(ls)-1]]
#print(ls)
result=[]
for i in range(len(ls)):
    n=ls[i][0]
    L=ls[i][1]
    R=ls[i][2]
    s=str(bin(n))[2:]#二进制位
    while len(s)<R:
        s="0"+s
    left=len(s)-R
    right=len(s)-L
    for i in range(left,right+1):
        if s[i]=='0':
            s=s[:i]+'1'+s[i+1:]
        else:
            s=s[:i]+'0'+s[i+1:]
    result.append(eval("0b"+s))
for i in range(len(result)):
    print(result[i])

    
    
  