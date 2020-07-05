str=input()
source=list(map(int,str.split(",")))
length=source.__len__()
number=[0]*50
i=0
while i<length:
    number[source[i]]=0+number[source[i]]+1
    if number[source[i]]>length//2:
        print(source[i])
        break
    i=i+1