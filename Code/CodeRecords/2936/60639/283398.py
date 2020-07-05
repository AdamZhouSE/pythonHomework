def valid(string):
    list=[['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','R','S'],['T','U','V'],['W','X','Y']]
    teleNumber=[]
    validNumber=""
    for i in range(len(string)):
        if string[i]!='-': teleNumber.append(str(string[i]))
    for i in range(len(teleNumber)):
        if teleNumber[i].isdigit():
            validNumber+=teleNumber[i]
        else:
            for j in range(len(list)):
                if teleNumber[i] in list[j]:
                    validNumber+=str(j+2)
    return validNumber
def operation(arr):
    judge=0
    result="No duplicates."
    for i in range(len(arr)):
        arr[i]=valid(arr[i])
    numSet=set(arr)
    for i in numSet:
        if arr.count(i)>1:
            result=i[0:3]+'-'+i[3:len(i)]+' '+str(arr.count(i))
    return result
def main():
    n=int(input())
    numList=[]
    for i in range(n):
        numList.append(input())
    if operation(numList)=="No duplicates.":
        print(operation(numList),end='')
    else :
        print(operation(numList))
main()
