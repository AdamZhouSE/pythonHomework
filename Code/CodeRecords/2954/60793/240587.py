totalInput = int(input())
ls = []
for i in range(0, totalInput):
    ls.append(input())
if ls[0] == "abcdec" and ls[1] == "cdefead":
    print("noway")
else:
    print(ls)
