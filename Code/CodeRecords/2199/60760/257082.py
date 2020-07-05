def work(str):                        #找到str的所有双子串
    length=len(str)
    result=[]
    needed=[]
    for j in range(1, length + 1):
        for n in range(length - j + 1):
            son = str[n:n + j]
            result.append(son)

    for i in result:
        num=0
        for j in range(length-len(i)+1):
            if str[j:j+len(i)]==i:
                num=num+1
        if num>=2:
            needed.append(i)
    return needed

def counted(str):
    if len(work(str))==0:
        return 0
    else:
        numbers=[]
        for i in work(str):
            numbers.append(counted(i))
        return max(numbers)+1


str0=input()
#print(work(str0))
result= counted(str0)
print(counted(str0)+1)
