import sys


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0,int(test)):
    temp = ""
    str = Input[begin]
    begin += 1
    for item in str:
        if item.isalpha():
            item = item.lower()
            temp += item
    li = list(temp)
    li.reverse()
    rev = "".join(li)
    if temp == rev:
        print("YES")
    else:
        print("NO")


    '''
    for i in range(0, N):
        print(arr[i], end=" ")
    print("")
    '''