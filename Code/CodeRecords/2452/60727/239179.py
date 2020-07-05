
def s(data,num,target,leng):
    if leng !=4:
        return False
    for i in range(0,num):
        for j in range(0,leng):
            if(target == data[i][j]):
                return(True)
    return False
num = int(input())
data =[]*num
le = 0
for i in range(0,num):
    a=input().split(",")
    data.append(a)
li = data[0]
leng = len(li)
target = int(input())
print(s(data,num,target,leng))
