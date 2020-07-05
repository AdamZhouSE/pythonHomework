source=str(input())
assist=""
for i in range(len(source)):
    if source[i].isdigit() or (source[i]==","):
        assist+=source[i]
result=map(int,assist.split(","))
print(sorted(result))