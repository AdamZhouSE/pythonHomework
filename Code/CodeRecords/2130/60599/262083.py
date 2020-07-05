n=int(input())
s=""
d=1
while len(s)<n:
    s+=str(d)
    d+=1
print(s[n-1])