n = int(input())
for i in range(n):
    str1=input()
    str2=input()
    find=False
    for x in str1:
        if x in str2:
            print(x)
            find = True
            break
    if find==False:
        print('$')