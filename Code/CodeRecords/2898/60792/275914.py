n=int(input())
s=input()
zero=0
one=0
for i in range(0,n):
    if s[i]=="0":
        zero=zero+1
    else:
        one=one+1
print("1",end="")
for i in range(0,zero):
    print("0",end="")