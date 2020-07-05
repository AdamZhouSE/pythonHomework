target=input()
length=len(target)
res=list()
while True:
    try:
        temp = input()
        i=0
        while i<len(temp)-length:
            if target[0].lower()==temp[i].lower():
                if target.lower()==temp[i:i+length].lower():
                    temp=temp[0:i]+temp[i+length:]
            i=i+1
        i=0
        while i<len(temp):
            if temp[i]==' ':
                temp=temp[0:i]+temp[i+1:]
            i=i+1
        res.append(temp)
    except:
        break
i=0
while i<res.__len__():
    print(res[i])
    i=i+1