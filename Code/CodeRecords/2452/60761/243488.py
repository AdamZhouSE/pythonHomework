line=int(input(""))
numtuple=()
for i in range(line):
    numtuple+=input("")
target=int(input(""))
if target in numtuple:
    print("True")
else:
    print("False")