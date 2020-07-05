n=eval(input())
hasCal=[]
temp=n
j=0
while True:
    tempn=list(str(temp))
    temp=0
    for i in tempn:
        temp+=(int(i)*int(i))
    if temp==1:
        print('True')
        break
    if temp not in hasCal:
        hasCal.append(temp)
    else:
        print('False')
        break