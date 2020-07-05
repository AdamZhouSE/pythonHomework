numList = [int(x) for x in input().split(",")];
if(len(numList)==1):
    print("False")
else:
    numList.sort()
    dictt =dict()
    for i in numList:
        if(i not in dictt):
            dictt[i] = 1
        else:
            dictt[i]+=1

    flag = False
    import sys
    minLen = sys.maxsize;
    for key in dictt:
        if dictt[key]<minLen:
            minLen = dictt[key]
    if(minLen==1):
        print(False)
    else:

        for i in range(2,minLen+1):
            index = 0;
            for key in dictt:
                if dictt[key]%i==0:
                    index+=1

            if(index==len(dictt)):
                flag = True
                print(True)
                break
        if(not flag):
            print(False)
        