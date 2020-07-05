def judge(l):
    flag = True
    for i in range(len(l)-1):
        if int(l[i+1])<=int(l[i]):
            flag = False
    return flag


string = input()
l = string[1:-1].split(",")

for i in range(len(l)):
    flag = False
    for k in range(i+1):
        if judge(l[k:k+len(l)-i]):
            print(len(l)-i)
            flag = True
            break
    if flag:
        break