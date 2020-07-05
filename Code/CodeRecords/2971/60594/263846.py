def sort(A: list,B:list):
    oc = []
    a = 1
    b = len(A)
    while a <= b:
        min = 0
        for index in range(len(A)):
            if A[index] < A[min]:
                min = index
        oc.append(B[min])
        del (A[min])
        del(B[min])
        a += 1
    return oc


s=input()
oc=[]
oc2=[]
for index in range(len(s)):
    oc.append(index+1)
    oc2.append(s[index:])
oc=sort(oc2,oc)
for index in range(len(oc)):
    print(oc[index],end=' ')