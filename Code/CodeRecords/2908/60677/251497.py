n=int(input())
string=[]
for i in range(n):
    x=input()
    x=list(x)
    x.sort()
    string.append("".join(x))
    print(x)
sb=set(string)
print(sb.__len__()-1,end="")