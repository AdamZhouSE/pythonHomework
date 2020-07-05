nums=str(input())
res=[]
#定义三种运算操作
op = {'+':lambda x,y:x+y, 
      '-':lambda x,y:x-y,
      '*':lambda x,y:x*y}
def calc(low, high):
    if low == high:
        return [nums[low]]  
    for i in range(low, high):
        for a in calc(low, i):
            for b in calc(i + 1, high):    
                res.append(op[i](a, b))
    return res
print(calc(0, len(nums)-1))

#def solve(input):
 #   for i in range(len(input)):
  #      if input[i] in op.keys():#如果是操作符
   #         for left in solve(input[:i]):
    #            for right in solve(input[i+1:len(input)]):
     #               output=op[input[i]](left,right)
      #              res.append(output)
#    if len(res)==0:
 #       res.append(int(input))
  #  return res
               
