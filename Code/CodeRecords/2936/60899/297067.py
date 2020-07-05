num = int(input())
list0 = []
for i in range(num):
    temp = input()
    formstr = ""
    for j in range(len(temp)):
        if temp[j] == "-": formstr+=""
        elif temp[j] == "A" or temp[j] == "B" or temp[j]=="C":
            formstr += "2"
        elif temp[j] == "D" or temp[j] == "E" or temp[j] == "F":
            formstr += "3"
        elif temp[j] == "G" or temp[j] == "H" or temp[j] == "I":
            formstr += "4"
        elif temp[j] == "J" or temp[j] == "K" or temp[j] == "L":
            formstr += "5"
        elif temp[j] == "M" or temp[j] == "N" or temp[j] == "O":
            formstr += "6"
        elif temp[j] == "P" or temp[j] == "R" or temp[j] == "S":
            formstr += "7"
        elif temp[j] == "T" or temp[j] == "U" or temp[j] == "V":
            formstr += "8"
        elif temp[j] == "W" or temp[j] == "X" or temp[j] == "Y":
            formstr += "9"
        else:
            formstr += temp[j]
    list0.append(formstr)
list1 = []
result = False
for i in range(len(list0)):
    if list0.count(list0[i])>1:
        result = True
        result0 = True
        for j in range(len(list1)):
            if list1[j][0:7] == list0[i]:
                result0 = False
                break
        if result0:
            list1.append(list0[i]+" "+str(list0.count(list0[i])))
list1.sort()
for i in range(len(list1)):
    list1[i] = list1[i][0:3] + "-" +list1[i][3:]
    print(list1[i])
if result == False:
    print("No duplicates.",end="")