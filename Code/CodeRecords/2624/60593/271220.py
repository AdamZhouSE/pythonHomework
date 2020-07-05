def diff(inp):
    end=[]
    for i in range(len(inp)):
        if(inp[i] in op.keys()):
            for left in diff([0:i]):
                for right in diff([i+1:len(inp)]):
                    outp=op[inp[i]](left,right)
                    end.append(outp)
    if(not len(end)):
        end.append(int(inp))
    return end
            
    
s=input()
op={'+':lambda x,y:x+y,
    '-':lambda x,y:x-y,
    '*':lambda x,y:x*y}
print(diff(s))