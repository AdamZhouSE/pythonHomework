def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def bookCase(shelf,bookNum):
    shelf=makeIntList(shelf);
    bookNum=makeIntList(bookNum);
    i=0;
    while(i<len(bookNum)):
        tempNum=bookNum[i];
        j=0;
        while(j<len(shelf)):
            if(tempNum>shelf[j]):
                tempNum-=shelf[j];
            else:
                print(j+1);
                break;
            j+=1;
        i+=1;

Total=int(input());
shelf=str(input());
shelf=shelf.split(" ");
totalBook=int(input());
bookNum=str(input());
bookNum=bookNum.split(" ");
bookCase(shelf,bookNum);