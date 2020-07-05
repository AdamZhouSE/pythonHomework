l = list(input())
l.reverse()
while l[0]=="0":
    l.remove("0")
if l[-1] == "-":
    l.remove("-")
    l.insert(0,"-")
print("".join(l))
     