if __name__ == '__main__':
    subString=input()
    string=input()
    subIndex=0
    index=0
    while index<len(string) and subIndex<len(subString):
        t=string[index]
        if t==subString[subIndex]:
            subIndex+=1
        index+=1
    if subIndex==len(subString):
        print(True)
    else:
        print(False)
            