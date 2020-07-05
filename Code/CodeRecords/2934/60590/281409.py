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
        res = ""
        times = int(stack[stack.__len__()-1-i])
        #print("temp: ", end="")
        #print(temp)
        for j in range(times):
            res += temp
        temp = res
        #print("res: ", end="")
        #print(res)
    else:
        continue

print(temp)