def cal(a,b,target,step):
    if a == target or b == target:
        if len(steps)!=0:
            if len(step)<len(steps[-1]):
                steps.append(step.copy())
        else:
            steps.append(step.copy())
        return 
    
    if a>target or b>target:
        return
    
    #(a,b)->(a+b,b)
    step.append([a+b,b])
    cal(a+b,b,target,step)
    step.pop()
    
    #(a,b)->(a,a+b)
    step.append([a,a+b])
    cal(a,a+b,target,step)
    step.pop()

n = int(input())
steps = []
cal(1,1,n,[[1,1]])
print(len(steps[-1])-1)