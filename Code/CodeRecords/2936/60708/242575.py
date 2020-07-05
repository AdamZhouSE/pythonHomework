#!/usr/bin/python3
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
        elif(i=="0"):
            newstr=newstr+'0'
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
    hasrepetition=0
    #字典排序
    A=[]
    step=len(a)
    for m in range(0, step):
        for n in range(0,len(a)):
            min=int(a[0])
            x=int(a[n])
            if x<=min:
                min=x
                minNo=n
        A.append(a[n])
        a.pop(n)

    for n in range(0,len(A)):
        if(b[A[n]]>1):
            str=A[n][0:3]+"-"+A[n][3:7]
            print(str,b[A[n]])
            hasrepetition=1
    if hasrepetition==0:
        print("No duplicates.",end="")