source=eval(input())
sources=[]
if(type(source)==int):
    sources.append(source)
else:
    for i in source:
        sources.append(i)
print(sources)