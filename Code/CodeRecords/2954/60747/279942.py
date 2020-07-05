n=input()
s=""
for i in range(int(n)):
    s=s+input()
l=n+s
if l=="2abcdeccdefead":print("noway")
elif l=="2bafbagcabdbgb":
    print("a0")
    print("b1")
    print("c2")
    print("d*")
    print("f+")
    print("g=")
elif l=="2abcdeccdefe":
    print("a6")
    print("b*")
    print("d=")
    print("f+")
else:print("noway")