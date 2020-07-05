def input_manage():
    temp=input()
    temp=temp[1:len(temp)-1]
    temp=temp.split(',')
    return temp
def find(num):
    result=0
    while 2**result<num:
        result=result+1
    return result
count=0
array=input_manage()
while array[count]!='null' and count<len(array):
    count=count+1
print(find(count))