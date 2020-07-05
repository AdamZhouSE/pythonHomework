def operation_1(t,g,c):
    for q in range(t,g+1):
        numlist[q] =  numlist[q]*c

def operation_2(t,g,c):
    for q in range(t,g+1):
        numlist[q] = numlist[q]+c

def operation_3(t,g):
    adder = 0
    for q in range(t,g+1):
        adder+=numlist[q]
    s = adder%p
    return s

n,p = map(int , input().split())
strs = input().split()
numlist = [ int(i) for i in strs]
answer = list()
a = int(input())
for i in range(a):
    strss = input().split()
    temp = [int(i) for i in strss]
    if temp[0]==1:
        operation_1(temp[1]-1,temp[2]-1,temp[3])
    elif temp[0]==2:
        operation_2(temp[1]-1,temp[2]-1,temp[3])
    elif temp[0]==3:
        k = operation_3(temp[1]-1,temp[2]-1)
        answer.append(k)
for i in range(len(answer)):
    print(answer[i])
