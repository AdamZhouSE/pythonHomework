s=input()
N=len(s)
i=0
result=[]
while(i<N):
    j = i
    k = i + 1
    while k < N and s[j] <= s[k] :
        if s[j] < s[k]:
            j = i
        else:
            j+=1
        k+=1
    while i <= j :
        result.append(str(i + k - j))
        i += k - j
print(" ".join(result))