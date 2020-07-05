num=int(input())
for i in range(num):
    str=input()
    patt=input()
    flag=False
    for j in range(len(str)):
        if patt.count(str[j])!=0:
            print(str[j])
            flag=True
            break
    if not flag:
        print('$')