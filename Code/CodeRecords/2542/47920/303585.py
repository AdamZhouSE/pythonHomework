inp = eval(input())
inp.sort()
#print(inp)

if(len(inp) == 0):
    print(0)
else:
    result = 1
    temp = 1
    for i in range(1,len(inp)):
        if(inp[i] - inp[i-1] )==1:
            temp +=1
        elif(inp[i]-inp[i-1]) == 0:
            pass
        else:
            result = max(result,temp)
            temp = 1
    print(result)