def stringToArray(string):
    string=string[1:len(string)-1]
    array=string.split(",")
    return array
def arrayToString(array):
    string="["+', '.join(array)+"]"
    return string
temp=stringToArray(input())
temp=sorted(temp)
length=int(len(temp)/3)
result=[]
for i in range (0,len(temp)-length):
    if temp[i]==temp[i+length]:
        result.append(temp[i])
print(arrayToString(result))