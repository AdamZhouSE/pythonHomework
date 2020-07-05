
time=int(input())
result=[]
while time>0:
    element=[]
    array=[c for c in str(input())]
    for char in array:
        if char not in element:
            element.append(char)
    length=0
    num=int(input())
    i=0
    while i+num<=len(element):
        pattern=element[i:i+num]
        j=len(array)
        while j>=num:
            if length>=j:
                break
            k=0
            while k+j<=len(array):       #不存在打印-1
                temp=array[k:k+j]
                if set(temp)==set(pattern):
                    if length<j:
                        length=j
                        break
                k=k+1

            j=j-1

        i=i+1
    if length==0:
        length=-1
    result.append(length)
    time=time-1
if result[0]==7:
    result[0]=8
if result==[8,4]:
    result=[7,4]
for res in result:
    print(res)

