def solve():
    pass

num=int(input())
list_ans=[]
for i in range(num):
    x=input().split()
    A=input().split()
    B=input().split()
    C=[0]*(len(A)+len(B)-1)
    for i in range(len(A)):
        for j in range(len(B)):
            C[i+j]+=int(A[i])*int(B[j])
    list_ans.append(C)
for ans_ in list_ans:
    print(" ".join(str(i) for i in ans_))

