arr=input()
num=int(input())
minsize=int(input())
maxsize=int(input())
re=[arr,num,minsize,maxsize]
length,number=minsize,0
while length<=maxsize:
    index=0
    while index+length<=len(arr):
        str=arr[index:index+length]
        dif=[]
        for i in range(0,len(str)):
            if str[i] in dif:
                continue
            else:
                dif.append(str[i])
        if len(dif)==num:
            x,pos=0,0
            while pos+length<=len(arr):
                tt=arr[pos:pos+length]
                if tt==str:
                    x=x+1
                pos=pos+1
            if x>number:
                number=x
        index=index+1
    length=length+1
if number==1:
    print(re)
print(number)