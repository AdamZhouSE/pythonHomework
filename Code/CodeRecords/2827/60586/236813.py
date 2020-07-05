def test8():
    n=int(input());
    row=input().split(" ")
    num=[]
    for i in range(n):
        num.append(int(row[i]))
    num.sort()
    result=""
    for i in num:
        result=result+str(i)+" "
    return result[0:len(result)-1]
print(test8())