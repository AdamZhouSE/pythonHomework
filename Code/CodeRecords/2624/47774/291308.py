input=str(input())
res=[]
#定义三种运算操作
op = {'+':lambda x,y:x+y, 
      '-':lambda x,y:x-y,
      '*':lambda x,y:x*y}

def solve(input):
    for i in range(len(input)):
        if input[i] in op.keys():#如果是操作符
            for left in solve(input[:i]):
                for right in solve(input[i+1:len(input)]):
                    output=op[input[i]](left,right)
                    res.append(output)
    if len(res)==0:
        res.append(int(input))
    return res

solve(input)
print(res)
               
