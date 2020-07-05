def judge(lst,k,t):
    for i in range(len(lst)):
        for j in range(1,k+1):
            if i+j >= len(lst):
                break
            if abs(lst[i] - lst[i+j]) <= t:
                return True
    return False

if __name__ == "__main__":
    str = input().split(' ')
    #print(str)
    lst = eval(str[2][0:-1])
    k = int((str[5].split(','))[0])
    t = int(str[8])
    res = judge(lst,k,t)
    if res:
        print("true")
    else:
        print("false")