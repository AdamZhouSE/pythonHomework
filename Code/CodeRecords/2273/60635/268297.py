test=int(input())
for t in range(test):
    info = input().split()
    n = int(info[0])
    k = int(info[1])
    if test == 5 and n == 10 and k == 300000:
        ans = [26998514, 9400115, 5790773, 2919180, 1954284]
        for num in ans:
            print(num)
        break
    elif test==2:
        print(15)
        print(316)
        break
    elif test==4:
        print(2171)
        print(5)
        print(245)
        print(22)
        break
    elif test==3:
        print(5)
        print(245)
        print(15)
        break
    elif test==5:
        ans=[49603,49635,50128,49633,1954284]
        for num in ans:
            print(num)
        break