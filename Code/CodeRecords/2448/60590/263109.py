import ast
paper = ast.literal_eval(input())

h = 1
flag = True
while flag:
    needed = h
    #print("before needed: ", end="")
    #print(needed)
    for i in range(paper.__len__()):
        if int(paper[i]) >= h:
            needed-=1
        if needed == 0:
            break

    #print("after needed: ", end="")
    #print(needed)
    if needed == 0:
        flag = True
        h += 1
    else:
        flag = False
    #print("h: ", end="")
    #print(h)

print(h-1)