instr=input()
outstr=input()
i=0
j=0
flag=0
while i<len(instr) or j<len(instr):
    while instr[i]=="X" and i<len(instr):
        i+=1
    while outstr[j]=="X" and j<len(instr):
        j+=1
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