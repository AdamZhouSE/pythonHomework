'''def _sort(li):
    for i in range(len(li)):
        for j in range(len(li)):
            if(i != j):
                if(li[i] < li[j]):
                    temp = li[i]
                    li[i] = li[j]
                    li[j] = temp
    return li'''
def longest(li,a):
    temp = []
    count = 1
    for i in range(a,len(li)-1):      
        if(li[a] == int((li[i-1] + li[i+1])/2)):
                count = count +1
        else:
            temp.append(count)
            longest(li,a+1)
    return temp
inp = eval(input())
if(longest(inp,1)):
    if(max(longest(inp,1))<=2):
        print("2")
    else:
        print(max(longest(inp,1)))
else:
    print("1")
    