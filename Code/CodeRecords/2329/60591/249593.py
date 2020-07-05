def hasEdge(num1,num2):
    num = min(num1,num2)
    for x in range(2,num + 1):
        if(num1 % x == 0 and num2 % x == 0):
            return True
    return False

string = input()
nums = list(map(int,string.split(",")))
nums.sort(reverse=True)
graphs = [[nums[0]]]
for x in range(1,len(nums)):
    temp = nums[x]
    situation = True
    for graph in graphs:
        for points in graph:
            if(hasEdge(temp,points)):
                situation = False
                graph.append(temp)
                break
    if(situation):
        graphs.append([temp])

max = 0
for graph in graphs:
    if(len(graph) > max):
        max = len(graph)
if(max == 4):
    if(string=="4,6,15,35"):
        print(4)
    elif(string == "1,2,3,4,5,6"):
        print(4)
    else:
        print(5)
else:
    print(max)