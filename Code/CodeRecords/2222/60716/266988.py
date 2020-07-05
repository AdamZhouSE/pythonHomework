def caculate_x():
    temp = strs.split('=')
    index = 0
    for j in range(len(temp[0])):
        if temp[0][j]=='x':
            if j==0:
                index+=1
            else:
                if temp[0][j-1]=='+' or temp[0][j-1]=='-':
                    if temp[0][j-1]=='+':
                        index+=1
                    else:
                        index-=1
                else:
                    if j-1==0:
                        index+=int(temp[0][j-1])
                    else:
                        if temp[0][j-2]=='+': index+=int(temp[0][j-1])
                        if temp[0][j-2]=='-': index-=int(temp[0][j-1])
    for j in range(len(temp[1])):
        if temp[1][j]=='x':
            if j==0:
                index-=1
            else:
                if temp[1][j-1]=='+' or temp[1][j-1]=='-':
                    if temp[1][j-1]=='+':
                        index-=1
                    else:
                        index+=1
                else:
                    if j-1==0:
                        index-=int(temp[1][j-1])
                    else:
                        if temp[1][j-2]=='+': index-=int(temp[1][j-1])
                        if temp[1][j-2]=='-': index+=int(temp[1][j-1])
#    print(index)
    return index

def caculate_c():
    number = [0,1,2,3,4,5,6,7,8,9]
    numbers = [str(i) for i in number]
    temp = strs.split('=')
    index = 0
    for j in range(len(temp[0])):
        if temp[0][j] in numbers:
            if j!=len(temp[0])-1 and temp[0][j+1]=='x':
                continue
            if j==0:
                index+=int(temp[0][j])
            else:
                index+= int(temp[0][j-1:j+1])
    for j in range(len(temp[1])):
        if temp[1][j] in numbers:
            if j!=len(temp[1])-1 and temp[1][j+1]=='x':
                continue
            if j==0:
                index-=int(temp[1][j])
            else:
                index-= int(temp[1][j-1:j+1])
#    print(index*-1)
    return index*-1

strs = input()
t = caculate_x()
c = caculate_c()
if t==0 and c==0:
    print("Infinite solutions")
elif t==0 and c!=0:
    print("No solution")
else:
    print("x={}.0".format(c//t))