def change(temp):
    newstr=''
    for i in temp:
        if(i=="1"):
            newstr=newstr+'1'
        elif(i=="2" or i=="A" or i=="B" or i=="C"):
            newstr=newstr+'2'
        elif (i == "3" or i == "D" or i == "E" or i == "F"):
            newstr = newstr + '3'
        elif (i == "4" or i == "G" or i == "H" or i == "I"):
            newstr = newstr + '4'
        elif (i == "5" or i == "J" or i == "K" or i == "L"):
            newstr = newstr + '5'
        elif (i == "6" or i == "M" or i == "N" or i == "O"):
            newstr = newstr + '6'
        elif (i == "7" or i == "P" or i == "R" or i == "S"):
            newstr = newstr + '7'
        elif (i == "8" or i == "T" or i == "U" or i == "V"):
            newstr = newstr + '8'
        elif (i == "9" or i == "W" or i == "X" or i == "Y"):
            newstr = newstr + '9'
    return newstr

if __name__ == '__main__':
    a=[];
    b={};
    i=int(input())
    for n in range(0,i):
        str=(input());
        temp = list(str)
        str=change(temp)
        if str not in a:
            b[str]=1
            a.append(str)
        else:
            b[str]+=1
    for n in range(0,len(a)):
        if(b[a[n]]>1):
            print(a[n],b[a[n]])
