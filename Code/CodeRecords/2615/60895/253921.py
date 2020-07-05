t=int(input())
while t>0:
    s=input()
    t=t-1
    ascii=[]
    for item in s:
        ascii.append(ord(item))
    max=1
    result=''
    for i in range(0,len(ascii)-2):
        length=0
        if ascii[i+2]-ascii[i+1]==ascii[i+1]-ascii[i]:
            length=3
            index=ascii[i+1]-ascii[i]
            temp=chr(ascii[i+2])+chr(ascii[i+1])+chr(ascii[i])
            for j in range(i+3,len(ascii)):
                if ascii[j]-ascii[j-1]==index:
                    length=length+1
                    temp=chr(ascii[j])+temp
                else:
                    break
        if length>=max:
            result=temp
            max=length
    print(result)