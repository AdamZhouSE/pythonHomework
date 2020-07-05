def lcm(A):
    great=max(A)
    while (True):
        index=0
        for i in range(len(A)):
            if great%A[i]!=0:
                index=1
        if index==0:
            break
        else:
            great+=1

    return great

def gcd(a,b):
    great=min(abs(a),abs(b))
    if great==0:
        return 0
    while(True):
        if a%great==0 and b%great==0:
            break
        else:
            great-=1
    return great

string=input()
molecular=[]
denominator=[]
symbol=[]
i=0
if string[0]=="-":
    i=1
    symbol.append("-")
else:
    symbol.append("+")
while i<len(string):
    molecular.append(int(string[i]))
    denominator.append(int(string[i+2]))
    if i!=(len(string)-3):
        symbol.append(string[i+3])
    i+=4
resultm=0
resultd=lcm(denominator)

for i in range(len(molecular)):
    if symbol[i]=="-":
        resultm=resultm-molecular[i]*resultd//denominator[i]
    else:
        resultm=resultm+molecular[i]*resultd//denominator[i]
x=gcd(resultm,resultd)
if x!=0:
    result=str(resultm//x)+"/"+str(resultd//x)
else:
    result="0/1"
print(result)

