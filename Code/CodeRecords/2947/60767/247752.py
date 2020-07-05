def fileOperation(file,operationStr):
    decode = operationStr.split(" ")
    if(decode[0]=="1"):
        file = file + decode[1]
        print(file)
        return file
    elif(decode[0]=="2"):
        a = int(decode[1])
        b = int(decode[2])
        file = file[a:a+b]
        print(file)
        return file
    elif(decode[0]=="3"):
        a = int(decode[1])
        string = decode[2]
        temp1 = file[:a]
        temp2 = file[a:]
        file = temp1 + string +temp2
        print(file)
        return file
    elif(decode[0]=="4"):
        stirng = decode[1]
        print(findSub(file,stirng))
        return file

def findSub(s,target):
    l = len(target)
    for i in range(0,len(s)-l+1):
        if(s[i:i+l]==target):
            return i
    return -1

num = int(input())
file = input()
for i in range(0,num):
    operationStr = input()
    #print("operationStr is:",operationStr)
    file = fileOperation(file,operationStr)