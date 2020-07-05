List = input()
List = List[1:len(List)-1]
List = List.split(",")
JList = []
OList = []
for i in range(len(List)):
    if int(List[i]) % 2 == 0:
        OList.append(List[i])
    else:
        JList.append(List[i])
OList.extend(JList)
final = []
for i in range(len(OList)):
    final.append(int(OList[i]))
print(final)