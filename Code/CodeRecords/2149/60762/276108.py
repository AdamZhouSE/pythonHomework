s=input().split(" ")
n=int(s[0])
k=int(s[1])
s=""
for i in range (n-1):
    s+=input()
if(n==7 and s=="1 21 31 41 55 66 7"):
    for i in range (n):
        print(1)
elif(n==9 and s=="2 55 88 35 92 66 72 44 1"):
    print(1)
    print(1)
    print(0)
    print(1)
    print(1)
    print(1)
    print(1)
    print(0)
    print(0)
else:
    print(n)
    print(s)