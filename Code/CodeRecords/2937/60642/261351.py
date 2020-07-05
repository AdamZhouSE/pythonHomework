instr = input()
comp = 'CODEFESTIVAL2016'
diff = 0
for i in range(len(comp)):
    if(comp[i]!=instr[i]):
        diff+=1
print(diff)