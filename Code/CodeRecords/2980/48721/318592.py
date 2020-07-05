def D(str1,c):
    temp =0
    for i in str1:
        if(i != c):
            temp = temp +1
        else:
            break
    result = str1[:temp]+str1[temp+1:]
    return result
def I(str1,a1,a2):
    str2 =str1[::-1]
    temp = 0
    for i in str2:
        if(i != a1):
            temp = temp +1
        else:
            break
    result = str2[:temp+1]+a2+str2[temp+1:]
    return result[::-1]
while True:
    try:
        s = input()
        comm = input()
        if(comm[0] == 'D'):
            tm = D(s,comm[3])
        elif(comm[0] == 'I'):
            tm = I(s,comm[3],comm[5])
        elif(comm[0] == 'R'):
            tm = s.replace(comm[3],comm[5])   
        if(s == tm):
            print("no exist")
            print(s)
        else:
            print(tm)
    except:
        break