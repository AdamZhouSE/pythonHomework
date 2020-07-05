n=int(input())
string=[]
for i in range(n):
    x=list(input())
    x.sort()
    string.append("".join(x))
sb=set(string)
print(sb.__len__()-1,end="")