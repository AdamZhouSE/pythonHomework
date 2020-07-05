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

result = []
result.append(graphs[0])
for x in range(len(graphs)):
    for y in range(x + 1,len(graphs)):
        graph1 = set(graphs[x])
        graph2 = set(graphs[y])
        temp = graph1 & graph2
        if(len(temp) != 0):
            result.append(list(graph1|graph2))
        else:
            if(not graph1 in result):
                result.append(graph1)
            if(not graph2 in result):
                result.append(graph2)
graphs = result
max = 0
for graph in graphs:
    if(len(graph) > max):
        max = len(graph)
print(max)