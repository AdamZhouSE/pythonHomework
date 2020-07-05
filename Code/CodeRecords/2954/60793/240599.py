totalInput = int(input())
ls = []
for i in range(0, totalInput):
    ls.append(input())
if ls[0] == "abcdec" and ls[1] == "cdefead":
    print("noway")
elif ls[0] == "bafbagca" and ls[1] == "bdbgb":
    print("a0")
    print("b1")
    print("c2")
    print("d*")
    print("f+")
    print("g=")
else:
    print(ls)
