t = eval(input())

for i in range(t):
    inp1 = input().split(' ')
    inp2 = input().split(' ')
    #print("{}，{}".format(inp1,inp2))

    a = int(inp1[2])-int(inp1[0])
    b = int(inp1[3])-int(inp1[1])
    c = int(inp2[2])-int(inp2[0])
    d = int(inp2[3])-int(inp2[1])
    
    #print(a,end="  ")
    #print(b)
    #print(c,end="  ")
    #print(d)

    re = a*c-b*d
    if(re == 0):
        print(0)
        break
    #print(re)
    #if((int(inp1[0])-int(inp2[0]))<0  and (int(inp1[2])-int(inp2[2]))>0):
       # print(1))
        
    if(int(inp1[2])==int(inp2[0]) and int(inp1[1])==int(inp2[1])):
        print(0)
        break
    if(((int(inp1[1])-int(inp2[1]))<0  and (int(inp1[3])-int(inp2[3]))>0)):
        print(1)
    #elif((int(inp1[0])-int(inp2[0]))>0  and (int(inp1[2])-int(inp2[2]))<0):
        #print(1)
    elif((int(inp1[1])-int(inp2[1]))>0  and (int(inp1[3])-int(inp2[3]))<0):
        print(1)
    else:
        print(0)
    
       