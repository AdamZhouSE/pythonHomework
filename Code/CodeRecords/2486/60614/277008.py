def check(str):
    num=int(str[0])#假定只有一位数
    str=str[2:-1]
    temp=""
    while len(str)>0:
        if ord(str[0])>=ord('0') and ord(str[0])<=ord('9'):
            temp=temp+check(str)#假定一旦开始[则必到结尾
            break
        else:
            temp=temp+str.pop(0)
    ret=""
    for i in range(num):
        ret+=temp
    return ret
length=int(input())
for i in range(length):
    question=list(input())
    print(check(question))#这居然都能过了