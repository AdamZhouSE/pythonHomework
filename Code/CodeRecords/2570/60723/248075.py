def input_manage(number):
    array=[[0 for _ in range(2)] for _ in range(number)]
    for i in range(number):
        temp=input()
        array[i][0]=int(temp[0])
        array[i][1]=int(temp[2])
    array.sort(reverse=True)
    return array
number=int(input())
array=input_manage(number)
count=1
max_len=array[0][0]
max_board=array[0][1]
for i in range(1,len(array)):
    if array[i][0]<max_len and array[i][1]<max_board:
        max_len=array[i][0]
        max_board=array[i][1]
        count=count+1
print(count)