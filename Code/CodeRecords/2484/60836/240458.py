n=int(input())
string_list = []

for i in range(n*3):
    string_list.append(str(input()))

i=0
while i<len(string_list):
    NM = string_list[i].split(" ")
    N = NM[0]
    M = NM[1]
    A = string_list[i+1].split(" ")
    B = string_list[i+2].split(" ")

    m=0
    while m<len(A):
        j=m+1
        while j<len(A):
            if A[j]==A[m]:
                del A[j]
            else:
                j=j+1
        m=m+1

    for m in range(len(B)):
        isexist = False
        for n in range(len(A)):
            if B[m]==A[n]:
                isexist=True
                break
        if not isexist:
            A.append(B[m])

    print(len(A))
    i=i+3
