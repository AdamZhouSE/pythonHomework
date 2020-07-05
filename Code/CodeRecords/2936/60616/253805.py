count=int(input())
nums=[]
for i in range (count):
    nums.append(input())
newNums=[]
for num in nums:
    if(len(num)==10):
        num=num[0:1]+num[2:7]+num[8:]
        newNums.append(num)
    else:
        if(num[0:1].isalpha()):
            for j in range(len(num)):
                tmp=num[j:j+1]
                if (tmp == 'A' or tmp == 'B' or tmp == 'C'): num=num.replace(tmp, '2')
                if (tmp == 'D' or tmp == 'E' or tmp == 'F'): num=num.replace(tmp, '3')
                if (tmp == 'G' or tmp == 'H' or tmp == 'I'): num=num.replace(tmp, '4')
                if (tmp == 'J' or tmp == 'K' or tmp == 'L'): num=num.replace(tmp, '5')
                if (tmp == 'M' or tmp == 'N' or tmp == 'O'): num=num.replace(tmp, '6')
                if (tmp == 'P' or tmp == 'R' or tmp == 'S'): num=num.replace(tmp, '7')
                if (tmp == 'T' or tmp == 'U' or tmp == 'V'): num=num.replace(tmp, '8')
                if (tmp == 'W' or tmp == 'X' or tmp == 'Y'): num=num.replace(tmp, '9')
        newNums.append(num)
dic={}
for newNum in newNums:
    dic[newNum]=newNums.count(newNum)
haveRepeat=False
for key,value in dic.items():
    if(value>1):
        haveRepeat=True
        break
if(haveRepeat):
    for key, value in dic.items():
        if(value>1):
            print(key,value)
else:
    print('No duplicates',end='.')
