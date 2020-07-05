def count_one(array):
    number=0
    for item in array:
        if item=='1':
            number=number+1
    return number
num=int(input())
array=input().split()
max_num=0
count=[]
for i in range(num,-1,-1):
    for j in range(len(array)-i+1):
        temp=array[:]
        for k in range(j,j+i):
            if temp[k]=='0':
                temp[k]='1'
            else:
                temp[k]='0'
        count.append(count_one(temp))
print(max(count))