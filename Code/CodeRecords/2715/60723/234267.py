def stringToArray(string):
    string=string[2:len(string)-2]
    array=string.split("],[")
    return array
temp=stringToArray(input())
temp=sorted(temp)
count=0
for i in range(0,len(temp)-1):
    for j in range(i+1,len(temp)):
        if temp[i][0]==temp[j][0] :
            count=count+1
            break
        elif temp[i][2]==temp[j][2] :
            count = count + 1
            break
print(count)