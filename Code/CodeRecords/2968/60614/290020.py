str=input()
for i in range(int(input())):
    operation=input().split()
    if operation[0]=='1':
        str+=operation[1]
    elif operation[0]=='2':
        str=operation[1][::-1]+str
    else:
        count=0
        for j in range(1,len(str)+1):
            for k in range(0,len(str)-j+1):
                temp=str[k:k+j]
                if temp==temp[::-1]:
                    count+=1
        print(count)