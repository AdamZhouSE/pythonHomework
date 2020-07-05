s = input()
ST = int(input())
numofs = ""
for x in s:
    numofs += str(ord(x) - ord('A') + ST)
while int(numofs) >100:
    newnumofs = ""
    for i in range(len(numofs) - 1):
        newnumofs += str(int(numofs[i])+int(numofs[i + 1]))[-1]
    numofs = newnumofs
print(numofs, end = "")
