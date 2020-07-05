def func(source:str,word:str):
    res=0
    word=sorted(word)
    length=len(source)
    l=len(word)
    for i in range(length-l+1):
        temp=sorted(source[i:i+l])
        if sorted(source[i:i+l])==word:
            res=res+1
    return res
tests=int(input())
results=[]
for i in range(tests):
    source=input()
    str=input()
    results.append(func(source,str))
for i in results:
    print(i)
