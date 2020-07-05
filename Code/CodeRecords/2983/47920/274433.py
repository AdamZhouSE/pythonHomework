
n = int(input())
str1 = input()
str2 = str1[::-1]
if(str1 == str2 ):
    print("0")
elif(len(str1) == 1):
    print("1")
else:
    result = []
    for i in range(len(str1)):
        temp = 0
        for j in range(len(str2)):
            if(i != j ):
                if(str1[i] == str1[j]):
                    temp = temp +1
        result.append(temp)
    tm = 0
    for i in range(len(result)):
        if(result[i]%2 != 0):
            tm =tm +1
    if(tm>=2):
        print("Impossible")
    #print("6")