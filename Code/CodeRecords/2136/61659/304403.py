import math
n=int(input())
i=1

def toOtherStandard(n,i):
    if i==1:
        return str(n)
    string=""
    while n>0:
        string=str(n%i)+string
        n=math.floor(n/i)
    return string


while True:
    string=toOtherStandard(n,i)
    if string.count("1")==len(string):
        print(i)
        break
    i=i+1