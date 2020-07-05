def splits(string):
    result=[]
    for i in range(0,len(string)):
        operation=string[i]
        if(operation=='+'or operation=='-' or operation=='*'):
            left=splits(string[:i])
            right=splits(string[i+1:])
            for l in left:
                for r in right:
                    if(operation=='+'):
                        result.append((int)(l)+(int)(r))
                    elif(operation=='-'):
                        result.append((int)(l)-(int)(r))
                    else:
                        result.append((int)(l)*(int)(r))
    if(len(result)==0):
        result.append((int)(string))
    return result
expression=input()
print(splits(expression))
