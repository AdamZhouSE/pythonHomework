sources=[]
try:
    while(True):
        x=list(input())
        sources.append(x)
except(EOFError):
    pass
print(sources)