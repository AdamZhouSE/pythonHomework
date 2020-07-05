def isSame(str1,str2):
    if len(str1)!=len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

array1 = input().strip("[]").split(",")
array2 = input().strip("[]").split(",")
if len(array1)>len(array2):
    length = len(array2)
else:
    length = len(array1)
while length != 0:
    for i in range(len(array1)-length+1):
        for j in range(len(array2)-length+1):
            if isSame(array1[i:i+length],array2[j:j+length]):
                break
        else:
            continue
        break
    else:
        length = length - 1
        continue
    break
print(length)