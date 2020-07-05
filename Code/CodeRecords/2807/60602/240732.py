def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def keyForBox(boxList,keyList):
    boxList=makeIntList(boxList);
    keyList=makeIntList(keyList);
    boxOdd=0;
    boxEven=0;
    keyOdd=0;
    keyEven=0;
    for element in boxList:
        if(element%2==1):
            boxOdd+=1;
        else:
            boxEven+=1;
    for element in keyList:
        if(element%2==1):
            keyOdd+=1;
        else:
            keyEven+=1;
    print(min(boxOdd,keyEven)+min(boxEven,keyOdd));
Total=str(input());
Total=Total.split(" ");
listBox=str(input());
listBox=listBox.split(" ");
listKey=str(input());
listKey=listKey.split(" ");
keyForBox(listBox,listKey);