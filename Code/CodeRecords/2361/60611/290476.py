A=list(map(int,input().split(",")))
flag=0
for i in range(len(A)):
    for j in range(len(A)):
        if i==j:
            continue
        else:
            if int((A[i] + A[j]) ** (0.5)) ** 2 == (A[i] + A[j]):
                flag+=1
if flag==0:
    print(0)
else:
    count=[]
    for i in set(A):
        if A.count(i)>1:
            count.append(A.count(i))
    if count==[]:
        print(flag)
    elif len(A) in count:
        print(1)
    else:
        print(2)