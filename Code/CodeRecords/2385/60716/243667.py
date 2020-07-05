#没有算法，直接根据数学归纳法推出公式以此计算
testnum = int(input())
answerlist = list()
for i in range(testnum):
    num = int(input())
    #k(n+1)=k(n)+k(n+1)
    #k(1)=2,k(2)=3,k(3)=5
    alist = list()
    alist.append(2)
    alist.append(3)
    if num==1:
        answerlist.append(2)
    elif num==2:
        answerlist.append(3)
    else:
        for j in range(2,num):
            temp = alist[j-1]+alist[j-2]
            alist.append(temp)
        an = alist.pop()
        answerlist.append(an)
for i in range(testnum):
    print(answerlist[i])