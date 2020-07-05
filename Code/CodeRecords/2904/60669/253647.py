n=int(input())
if n==0:
    print(0)
elif n>0:
    string=str(n)
    newString="".join(reversed(string))
    print(newString.strip('0'))
else:
    string=str(abs(n))
    newString = "".join(reversed(string))
    print("-"+newString.strip('0'))