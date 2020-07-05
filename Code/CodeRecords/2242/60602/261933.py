def recCalcu(listA,listB):
    if((listB[0]>listA[0] and listB[0]<listA[2] and listB[1]>listA[1] and listB[1]<listA[3]) or (listB[2]>listA[0] and listB[2]<listA[2] and listB[3]>listA[1] and listB[3]<listA[3]) or (listB[0]>listA[0] and listB[0]<listA[2] and listB[3]>listA[1] and listB[3]<listA[3]) or (listB[2]>listA[0] and listB[2]<listA[2] and listB[1]>listA[1] and listB[1]<listA[3])):
        print(True);
    else:
        print(False);

listA=eval(input());
listB=eval(input());
recCalcu(listA,listB);