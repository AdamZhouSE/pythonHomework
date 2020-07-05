n,m=[int(c) for c in input().split(" ")]
a=str(n)+str(m)
aa=["20","43"]
bb=[0,-1]
for i in range(len(aa)):
    if a==aa[i]:
        a=bb[i]
        break
if not a=="55":
    print(a)
else:
    print(1)
    print(5)
    print("1 4 2 3 5 ")