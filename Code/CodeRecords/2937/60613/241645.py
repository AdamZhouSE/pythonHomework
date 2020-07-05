sta="CODEFESTIVAL2016"
curr=input().split()[0]

result=0

for i in range(16):
    if curr[i]!=sta[i]:
        result+=1
print(result)
