def stringToArray(string):
    string=string[1:len(string)-1]
    array=string.split(",")
    return array
temp=stringToArray(input())
number=int(input())
count=-1
for i in range(0,len(temp)):
    if int(temp[i])==number :
        count=i
        break
print(count)