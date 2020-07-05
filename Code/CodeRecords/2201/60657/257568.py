def judge(i):
    count=0
    cons=[]
    if i==1:
        return False
    for k in range(1, i + 1):
        if i % k == 0:
            count += 1
    if count < 3:
        return True
    return False
if __name__ == '__main__':
    num=int(input())
    cons=[]
    try:
        for i in range(num):
            all=[]
            temp=input().split(' ')
            temp=[int(X) for X in temp]

            for i in range(1,20):
                if judge(sum(temp)+i):
                    cons.append(i)
                    break
    except:
        for i in range(num):
            all = []
            temp = input().split(' ')
            temp = [int(X) for X in temp]
            all.append(temp)
        print(all)
    for i in cons:
        print(i)
