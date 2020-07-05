code = input()
lists = list(code)
#print(lists)

stack = []
for i in range(lists.__len__()):
    if lists[i] != ']':
        stack.append(lists[i])
#print(stack)

ans = ""
temp = ""
for i in range(stack.__len__()):
    if stack[stack.__len__()-1-i].isalpha():
        temp = stack[stack.__len__()-1-i] + temp
        #print("temp: ", end="")
        #print(temp)
    elif stack[stack.__len__()-1-i].isnumeric() and stack.__len__()-1-i != 1:
        res = ""
        #print("temp: ", end="")
        #print(temp)
        index = stack.__len__()-1-i
        str = stack[index]
        while stack[index-1].isnumeric():
            str = stack[index-1] + str
            stack[index-1] = '@'
            index = index -1
        times = int(str)
        #times = int(stack[stack.__len__()-1-i])
        for j in range(times):
            res += temp
        #print("res: ", end="")
        #print(res)
    elif stack[stack.__len__()-1-i].isnumeric() and stack.__len__()-1-i == 1:
        str1 = ""
        #print("hello")
        for j in range(int(stack[stack.__len__()-1-i])):
            str1 += ans
        ans = str1
        break
    elif stack[stack.__len__()-1-i] == '[':
        #print("here")
        ans = res + ans
        temp = ""
        #print("ans: ", end="")
        #print(ans)
    else:
        continue

print(ans)
