def test7():
    n=int(input())
    exam=[]
    rank=1
    for i in range(n):
        x=input().split(" ")
        sumN=0
        for item in x:
            sumN=sumN+int(item)
        exam.append(sumN)
    for i in range(1,n):
        if exam[i]>exam[0]:
            rank=rank+1
    return rank
print(test7())
