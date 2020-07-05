def input_manage():
    temp=input()
    temp=temp[1:len(temp)-1]
    array=temp.split(',')
    return array
def check(i,j,k):
    if i+j>k and i+k>j and j+k>i:
        return True
    return False
array=input_manage()
cycle=[]
for i in range(len(array)-2):
    for j in range(i+1,len(array)-1):
        for k in range(j+1,len(array)):
            if check(int(array[i]),int(array[j]),int(array[k])):
                cycle.append(int(array[i])+int(array[j])+int(array[k]))
if len(cycle)==0:
    print(0)
else:
    print(max(cycle))