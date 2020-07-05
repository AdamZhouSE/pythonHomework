def input_manage():
    string=input()
    array=string.split(" ")
    return array
array=input_manage()
max_number=0
for item in array:
    if len(item)>max_number:
        max_number=len(item)
        result=item
print(result)