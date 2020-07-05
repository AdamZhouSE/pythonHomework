import numpy as np
answerlist=[]
def recursion(degree,list,start,end,answer):
    if answer.__len__()==degree:
        answerlist.append(answer[:])
        return
    for i in range(start,end):
        answer.append(str(list[i]))
        recursion(degree,list,i+1,end,answer)
        answer.remove(str(list[i]))

n=int(input())
bigList=[]
for i in range(n):
    line=input()
    line+=(",1")
    bigList.append(line)
recursion(3,bigList,0,n,[])
squares=[]
for i in answerlist:
    matrix=[]
    for j in i:
        nums=j.split(",")
        nums=[int(x) for x in nums]
        matrix.append(nums)
    a = np.array(matrix)
    aa=np.linalg.det(a)/2
    squares.append(abs(aa))
squares.sort(reverse=True)
print(squares[0])