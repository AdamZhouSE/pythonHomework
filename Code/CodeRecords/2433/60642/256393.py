inputList = eval(input())
replacer = []
for i in range(len(inputList)):
    for j in range(inputList[i][0],inputList[i][-1]):
        if( replacer.count([j,j+1])==0 ):
            replacer.append([j,j+1])
#print(replacer)
outer = []
middle = []
for i in range(len(replacer)-1):
    if(middle==[]):
        middle.append(replacer[i][0])
    if(replacer[i][1]==replacer[i+1][0]):
        #middle.append(replacer[i][1])
        if (i == len(replacer) - 2):
            middle.append(replacer[i+1][1])
            outer.append(middle)
    else:
        middle.append(replacer[i][1])
        outer.append(middle)
        #print("there",replacer[i])
        if (i == len(replacer) - 2):
            outer.append(replacer[i+1])
        middle = []


print(outer)