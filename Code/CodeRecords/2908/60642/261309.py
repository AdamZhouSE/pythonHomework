length = int(input())
strs = []
for i in range(length):
    instr = input()
    adder = ""
    while(len(str)>0):
        adder = adder+max(str)*str.count(max(str))
        instr = instr.replace(max(str),"")
    strs.append(adder.replace(' ',''))
num = 0
while(len(strs)>0):
    temp = strs.count(strs[-1])
    for i in range(temp):
        strs.remove(strs[-1])
    num=num+1
print(str(num)+' ')