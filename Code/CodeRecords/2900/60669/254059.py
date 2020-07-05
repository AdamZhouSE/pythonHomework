string=input()
result=0
for item in string:
    if 'A'<=item<='Z' or 'a'<=item<='z' or '0'<=item<='9':
        result+=1
print(result,end="")
        