x=float(input())
n=int(input())
s=str(round(pow(x,n),5))

ind=s.index(".")
while len(s)-1-ind<5:
    s=s+"0"
print(s)

