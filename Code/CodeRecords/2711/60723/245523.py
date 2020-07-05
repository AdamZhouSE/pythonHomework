def similar_or_not(str1,str2):
    for i in range(len(str1)-1):
        for j in range(i+1,len(str1)):
            if swap(str1,i,j)==str2:
                return True
    return False
def swap(str,i,j):
    return str[:i]+str[j]+str[i+1:j]+str[i]+str[j+1:]
def input_manage():
    temp=input()
    temp=temp[2:len(temp)-2]
    array=temp.split('","')
    return array
array=input_manage()
count=1
for i in range(len(array)-1):
    for j in range(i+1,len(array)):
        if similar_or_not(array[i],array[j]):
            count=count+1
print(count)