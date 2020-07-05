instr = input()
substr = ''
maxlen = 0
for i in range(len(instr)):
    if(substr.count(instr[i])==0):
        substr+=instr[i]
    else:
        if(len(substr)>maxlen):
            maxlen = len(substr)
        substr = substr[substr.index(instr[i])+1:]+instr[i]

print(maxlen)