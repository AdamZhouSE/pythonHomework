n=list(input())
summary=0
total=1
for i in range(len(n)):
    temp=int(n[i])
    summary=summary+temp
    total=total*temp
print(total-summary)