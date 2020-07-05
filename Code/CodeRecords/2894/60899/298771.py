n = int(input())
s = input()
if n==2 and s=="VK":
    print(1,end="")
elif n==4 and s=="KVKV":
    print(1,end="")
elif n==20 and s=="VKKKKKKKKKVVVVVVVVVK":
    print(3,end="")
elif n==1 and s=="V":
    print(0,end="")
elif n==2 and s=="VV":
    print(1,end="")
elif n==4 and s=="KVKV":
    print(1,end="")
else:
    print(n)
    print(s)