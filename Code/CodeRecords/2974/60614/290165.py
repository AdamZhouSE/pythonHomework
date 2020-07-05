def find(str):
    exist=[]
    for j in range(1, len(str) + 1,2):
        for k in range(0, len(str) - j + 1):
            temp = str[k:k + j]
            if temp in exist:
                continue
            elif temp == temp[::-1]:
                exist.append(temp)
    return len(exist)
def all(str):
    exist=[]
    for i in range(1,len(str)+1):
        for k in range(0, len(str) - i + 1):
            temp = str[k:k + i]
            if temp in exist:
                continue
            else:
                exist.append(temp)
    return len(exist)
length=int(input())
init=input()
maximum=0
for i in range(1,length+1):
    first=init[0:i]
    second=init[i:]
    maximum=max(maximum,find(first)*(all(second)-find(second)))
print(maximum)
