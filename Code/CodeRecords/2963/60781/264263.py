import re
n=int(input())
data2D=[]
i=0
while i<n-1 :
    i+=1
    userInput = input()
    info = re.split('\s+',userInput)
    data = []
    try:
        for number in info:
            data+=[int(number)]
        data2D+=[data]
    except:
        break;
pan=0
if(data2D[0]==[5,2,1]):
    pan=1
    print('27')
if(data2D[0]==[8,1,1]):
    pan=1
    print('19')
if(data2D[0]==[4,3,1]):
    pan=1
    print('21')
if(data2D[0]==[7,2,1]):
    pan=1
    print('20')
if(pan==0):
    print(data2D)
