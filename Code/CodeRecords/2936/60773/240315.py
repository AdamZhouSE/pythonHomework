def convert(s):
    form={
        '-':'',
        '1':'1',
        '0':'0',
        '2':'2',
        '3':'3',
        '4':'4',
        '5':'5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        'A': '2',
        'B': '2',
        'C': '2',
        'D': '3',
        'E': '3',
        'F': '3',
        'G': '4',
        'H': '4',
        'I': '4',
        'J': '5',
        'K': '5',
        'L': '5',
        'M': '6',
        'N': '6',
        'O': '6',
        'P': '7',
        'R': '7',
        'S': '7',
        'T': '8',
        'U': '8',
        'V': '8',
        'X': '9',
        'Y': '9',
        'Z': '9',
    }
    result=""
    for i in s:
        result=result+form[i]
    return result
num=int(input())
#print(num)
list=[]
for i in range(num):
    list.append(input())
#print(list)
for i in range(num):
    list[i]=convert(list[i])
list.sort()
#print(list)
flag=0
for i in range(num):
    sum=1
    for j in range(i+1,num,1):
        if(list[j]==list[i]):
            list[j]='#'
            sum=sum+1
    #print(sum)
    if(sum>1)and(list[i]!='#'):
        print(list[i][0:3],end="-")
        print(list[i][3:],end=" ")
        print(sum)
        flag=flag+1
if flag==0:
    print("No duplicates.",end="")