string = input()
order = input().split(" ")
print(string)
if order[0] == "D":
    # 删除
    string = string.replace(order[1], "", 1)
elif order[0] == "I":
    # insert
    found = False
    for i in range(0, len(string)):
        if string[len(string)-1-i] == order[1]:
            string = string[0:len(string)-1-i] + order[2] + string[len(string)-1-i:len(string)-1]
            found = True
            break
    if not found:
        print("error")

elif order[0] == "R":
    # replace
    found = False
    for i in range(0, len(string)):
        if string[i] == order[1]:
            string = string[0:i] + order[2] + string[i+1:len(string)]
            found = True
    if not found:
        print("error")
print(string)
