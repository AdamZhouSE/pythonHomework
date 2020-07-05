code = input()
lists = list(code)
#print(lists)

stack = []
for i in range(lists.__len__()):
    if lists[i] != ']':
        stack.append(lists[i])
#print(stack)

temp = ""
for i in range(stack.__len__()):
    if stack[stack.__len__()-1-i].isalpha():
        temp = stack[stack.__len__()-1-i] + temp
        #print(temp)
    elif stack[stack.__len__()-1-i].isnumeric():
        '''index = stack.__len__()-1-i
        numstr = stack[stack.__len__()-1-i]
        while stack[index-1].isnumeric():
            numstr = stack[index-1] + numstr
            index -= 1
        times = int(numstr)'''
        res = ""
        #print("temp: ", end="")
        #print(temp)
        times = int(stack[stack.__len__()-1-i])
        for j in range(times):
            res += temp
        temp = res
        #print("res: ", end="")
        #print(res)
    else:
        continue

print(temp)