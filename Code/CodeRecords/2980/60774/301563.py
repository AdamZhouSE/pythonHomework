def changeStr(s,mode,op1,op2 = ''):
    if(s.count(op1) == 0):
        print('no exist')
        return s
    elif(mode == 'D'):
        temp = list(s)
        temp.remove(op1)
        s = ''.join(temp)
    elif(mode == 'I'):
        i = s.rfind(op1)
        temp = list(s)
        temp.insert(i,op2)
        s = ''.join(temp)        
    elif(mode == 'R'):
        s = s.replace(op1,op2)
    return s

s = input()
op = input().split()
if(len(op) == 2):
    s = changeStr(s,op[0],op[1])
else:
    s = changeStr(s,op[0],op[1],op[2])
print(s)