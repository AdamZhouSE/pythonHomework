length = int(input())
strs = []
for i in range(length):
    instr = input()
    adder = ""
    while(len(instr) > 0):
        adder = adder + max(instr) * instr.count(max(instr))
        instr = instr.replace(max(instr), "")
    strs.append(adder.replace(' ',''))
num = 0
while(len(strs)>0):
    temp = strs.count(strs[-1])
    for i in range(temp):
        strs.remove(strs[-1])
    num=num+1
print(str(num),end='')