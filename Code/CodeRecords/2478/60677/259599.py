times=int(input())

def do():
    line=input().split()
    line=[int(x) for x in line]
    n=int(input())
    return (n-1)*(line[1]-line[0])+line[0]
for i in range(times):
    print(do())