source=list("CODEFESTIVAL2016")
a=source.copy()
target=list(input())
for i in range(16):
    if(target[i]==source[i]):
        a.pop(a.index(target[i]))
print(len(a))