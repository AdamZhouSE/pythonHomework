num = int(input())
for i in range(num):
    n=int(input())
    numStr=input()
    numList=[]
    add=0
    for c in numStr:
        if '0'<= c <='9':
            numList.append(int(c))
            add=add+int(c)
    if add!=0 and add%3==0:
        print(1)
    else:
        print(0)
