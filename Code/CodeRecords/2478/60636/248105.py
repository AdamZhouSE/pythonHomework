t=int(input())
for i in range(t):
    source=input().split(" ")
    sources=[]
    sources.append(int(source[0]))
    sources.append(int(source[1]))
    n=int(input())
    print(sources[0]+(n-1)*(sources[1]-sources[0]))