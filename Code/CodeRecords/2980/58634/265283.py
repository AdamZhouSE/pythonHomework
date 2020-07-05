str = input()
str1 = str
a = input()
a = a.replace(" ","")
command = list(a)
if command[0] == 'D':
    temp = list(str)
    temp.remove(command[1])
    print("".join(temp))
elif command[0] == 'I':
    temp1 = list(str)
    temp2 = temp1.copy()
    temp2.reverse()
    temp1.insert(len(temp1)-temp2.index(command[1])-1,command[2])
    print("".join(temp1))
else:
    str = str.replace(command[1],command[2])
    if str == str1:
        print("no exist")
    print(str)