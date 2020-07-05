def stringToArray(string):
    string=string[1:len(string)-1]
    array=string.split(", ")
    return array
def find(number,temp):
    count = -1
    for i in range(0, len(temp)):
        if int(temp[i]) == number:
            count = i
            break
    return count
def exchange(oringin,change,temp):
    num=temp[oringin]
    temp[oringin]=temp[change]
    temp[change]=num
    return temp
temp=stringToArray(input())
count=0
for i in range(0,len(temp),2):
    flag=bool(int(temp[i])%2==0)#偶数和后面的凑，奇数和前面的凑
    if flag :
        change=find(int(temp[i])+1,temp)
        if change!=i+1:
            temp=exchange(i+1,change,temp)
            count=count+1
    else:
        change = find(int(temp[i]) -1, temp)
        if change!=i+1:
            temp=exchange(i+1,change,temp)
            count=count+1
print(count)