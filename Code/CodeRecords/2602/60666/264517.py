A=eval(input())
B=eval(input())
index={}
result=1
for i in range(len(B)):
    if B[i] not in index:
        index[B[i]]=[i]
    else:
        index[B[i]].append(i)
for i in range(len(A)):
    if A[i] in index:
        for j in index[A[i]]:
            while i+result<=len(A) and j+result<=len(B) and A[i:i+result]==B[j:j+result]:
                result+=1
result-=1
print(result)