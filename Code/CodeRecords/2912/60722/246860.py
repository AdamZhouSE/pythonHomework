word=input()
n=len(word)
result=[]
for i in range(n-1):
    longest=[word[i]]
    for j in range(i+1,n):
        if not word[j] in longest:
            longest.append(word[j])
        else:
            break
    result.append(len(longest))
print(max(result))