str=input()
list=list(map(int,str[1:len(str)-1].split(',')))
list.sort()
maxNum=0
for i in range(len(list)-1):
    num=int(list[i+1])-int(list[i])
    if num>maxNum:
        maxNum=num
print(maxNum)