def findMode():
    array=list(eval(input()))
    modeStandard=len(array)//3
    array.sort()
    count=1
    mode = []
    for i in range(0, len(array)-1):
        if count>modeStandard:
            mode.append(array[i])
        if array[i]==array[i+1]:
            count+=1
            continue
        else:
            count=1
    print(mode)
    if mode==[]:
        print (array)

if __name__=='__main__':
    findMode()




