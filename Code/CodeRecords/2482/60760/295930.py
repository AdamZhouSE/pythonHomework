def func(son:int,mother:int):
    res=round((son/mother),6)
    temp=str(res)
    if temp.endswith('.0'):
        temp=temp.replace('.0','')
        return temp
    remind=son%mother
    result=str(int(son/mother))+'.'
    while remind!=son :
        result=result+str(int(remind*10/mother))
        son=remind
        remind=remind*10%mother
    if remind>0:
        result=result[0:len(result)-1]+'('+result[-1]+')'
    else:
        result = result[0:len(result) - 1]
    temp=result
    return temp

tests=int(input()) #找规律
sons=[]
mothers=[]
for i in range(tests):
    sons.append(int(input()))
    mothers.append(int(input()))
for i in range(tests):
    print(func(sons[i],mothers[i]))