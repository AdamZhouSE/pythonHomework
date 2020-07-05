times=int(input())
for i in range(times):
    n=int(input())
    answerList=[]
    answer="0b1"
    i=0
    while True:
        x=int(answer,2)
        if x>n:
            break
        answerList.append(str(x))
        answer+=str(i)
        i=(i+1)%2
    print(" ".join(answerList))