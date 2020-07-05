def judgeASelfDivide(x):
    strNum=str(x)
    for i in strNum:
        if int(i)==0:
            return False
        if x%int(i)!=0:
            return False
    return True

start=int(input())
end=int(input())
result=[]

for k in range(start,end+1):
    if judgeASelfDivide(k):
        result.append(k)

print(result)