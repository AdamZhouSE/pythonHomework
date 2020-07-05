'''def _sort(li):
    for i in range(len(li)):
        for j in range(len(li)):
            if(i != j):
                if(li[i]<li[j]):
                    temp = li[i]
                    li[i] = li[j]
                    li[j] = temp
    return li'''
inp = eval(input())
#print("输入",inp)   
count = 0

for i in range(0,len(inp)-2,2):
    #print("doyice")
    if(abs(inp[i] - inp[i+1]) != 1): 
        count = count +1
        #print(" ",count)
        for j in range(i,len(inp)):
            if(inp[j] == inp[i+1]):
                temp  = inp[i+1]
                inp[i] = inp[j]
                inp[j] = temp          
                
print(count)