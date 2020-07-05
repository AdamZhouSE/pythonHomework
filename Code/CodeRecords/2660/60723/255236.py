number=int(input())
file=[]
operation=[]
for i in range(number):
    temp=input().split()
    if temp[0]=='T':
       file.append(temp[1])
    elif temp[0]=='U':
        for i in range(int(temp[1])):
            file.pop()
    else:
        print(file[int(temp[1])-1])