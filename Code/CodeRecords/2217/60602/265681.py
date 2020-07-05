def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def distance(listA,listB):
    temp= pow(listA[0]-listB[0],2)+pow(listA[1]-listB[1],2);
    return temp;

def IsHer(listA,listB,listC):
    deltaAB1=listA[0]-listC[0];
    deltaAB2=listA[1]-listC[1];
    deltaBC1=listB[0]-listC[0];
    deltaBC2=listB[1]-listC[1];
    if(deltaAB1*deltaBC1+deltaAB2*deltaBC2==0):
        return True;
    else:
        return False;


def IsSquare(listA,listB,listC,listD):
    if(distance(listA,listC)==distance(listB,listC) and distance(listB,listC)==distance(listB,listD) and IsHer(listA,listB,listC)):
        print(True);
    else:
        print(False);

listA=makeIntList(str(input()).split(","));
listB=makeIntList(str(input()).split(","));
listC=makeIntList(str(input()).split(","));
listD=makeIntList(str(input()).split(","));
IsSquare(listA,listB,listC,listD);