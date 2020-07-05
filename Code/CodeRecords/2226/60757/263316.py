def judge(a):
    for i in range(len(str(a))):
        if (str(a))[i] =='0':
            return '0'
        if(a%int((str(a))[i]))!=0:
            return '0'
    return '1'
left=int(input())
right=int(input())
li=[]
for i in range(left,right+1):
    if judge(i)=='1':
        li.append(i)
print(li)