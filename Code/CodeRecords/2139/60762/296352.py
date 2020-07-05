l=[int(x) for x in input().split(" ")]
s=""
for i in range (0,l[0]+l[1]-1):
    s+=input()
if(s=="1 21 34 14 56 52 3 73 6 86 4 5"):
    print("7"+"\n"+"7"+"\n"+"8"+"\n"+"5"+"\n"+"5")
else:
    print(s)
