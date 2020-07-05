a = input()
array = input()
array = [int(x) for x in array.split(" ")]
max = 0
t = 0
flag = 0
up = False
down = False
for i in range(len(array)):
    if array[i] >  max:
        t = i
        max = array[i]
for i in range(t):
    if array[i] < array[i+1]:
        continue
    else:
        flag=1
        break
if flag == 1:
    print("NO")
else:
    c= 0
    for i in range(t,len(array)-1):
        if c == 0:
            if max == array[i+1]:
                continue
            elif array[i+1]<array[i]:
                c = 1
                continue
            else:
                flag = 1 
                break
        else:
            if array[i+1]< array[i]:
                continue
            else:
                flag=1
                break
    if flag == 1:
        print("NO")
    else:
        print("YES")