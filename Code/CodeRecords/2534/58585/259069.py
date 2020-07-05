source=input()
result=[]
for n in source:
    if(n.isdigit()):
        result.append(int(n))
print(sorted(result))