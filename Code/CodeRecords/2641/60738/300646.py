s1=input()
s2=input()
result=False
for i in range(len(s2)-len(s1)+1):
    if list(s1)==sorted(list(s2)[i:i+len(s1)]):
        result=True
        break
print(result)