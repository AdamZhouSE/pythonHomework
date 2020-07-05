instr=input()
outstr=input()
i=0
j=0
flag=0
while i!=len(instr) or j!=len(instr):
    while i<len(instr) and instr[i]=="X":
        i+=1
    while j<len(instr) and outstr[j]=="X":
        j+=1
    if i==len(instr) and j==len(instr):
        break
    if i==len(instr) or j==len(instr):
        flag=1
        break
    if instr[i]!=outstr[j]:
        flag=1
        break
    if (instr[i] == 'L' and i < j) or (outstr[j] == 'R' and i > j):
        flag=1
        break
    i+=1
    j+=1
if flag==1:
    print("False")
else:
    print("True")
