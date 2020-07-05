n=int(input())
string=[]
for i in range(n):
    x=input()
    x=list(x)
    x.sort()
    if i!=n-1:
        x.pop(0)
    string.append("".join(x))
sb=set(string)
print(sb.__len__(),end="")