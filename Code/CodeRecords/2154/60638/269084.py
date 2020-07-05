num=input()
i=0
j=len(num)-1
check=True
while i<j:
    if num[i]!=num[j]:
        check=False
        break
    i=i+1
    j=j-1
print(check)