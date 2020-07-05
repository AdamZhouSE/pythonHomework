length=int(input())
str=input()
statistic = dict()
for i in str:
    if i not in statistic:
        statistic[i]=1
    else:
        statistic[i] = statistic[i]+1
copyOfsta=statistic.values()
numberOfOdd=0
for i in copyOfsta:
    if i%2==1:
        numberOfOdd=numberOfOdd+1

if numberOfOdd>1 or (numberOfOdd==1 and length%2==0):
    print("Impossible")
else:
    i=0
    j=length-1
    step=0
    flagOfmiddle=True
    resultJud=True
    while i<length:
        while str[j]!=str[i]:
            j=j-1
        if j==i:
            if (length%2==0):
                break
            else:
                middle=(length-1)//2
                if j<middle:
                    str=str[0:j]+str[j+1:middle]+str[j]+str[middle+1:]
                else:
                    str=str[0:middle]+str[j]+str[middle+1:j]+str[j+1:]
        else:
            pos=length-1-i
            step=step+pos-j
            temp=""
            if pos!=length-1:
                temp=str[pos+1:]
            str=str[0:j]+str[j+1:pos+1]+str[j]+temp
        i = i + 1
        j = length - 1 - i

    print(step)