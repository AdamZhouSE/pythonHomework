# 递归实现 倒着来
'''
pre: the last number added to the expression, if the last op is minus, add the opposite number
'''
def compute(num: str, target: int, expr: str, pre: int, curAns: int, res: []) -> []:
    if len(num) == 0 and curAns == target:
        res.append(expr)
    else:
        for i in range(1,len(num)+1):
            if i>1 and num[0] == '0':
                continue # a num cannot begin with 0
            x = int(num[0:i]) # so i has to be len(num) so as to get all num
            if expr == "":
                compute(num[i:len(num)],target,num[0:i],x,x,res)
            else:
                compute(num[i:len(num)],target,expr+"+"+num[0:i],x,curAns+x,res)
                compute(num[i:len(num)],target,expr+"-"+num[0:i],-x,curAns-x,res)
                # be careful of the priority below
                compute(num[i:len(num)],target,expr+"*"+num[0:i],x*pre,curAns-pre+x*pre,res)


res = []
compute(input(),int(input()),"",0,0,res)
print(res)


