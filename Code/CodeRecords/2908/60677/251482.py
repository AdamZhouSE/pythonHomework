n=int(input())
string=[]
for i in range(n):
    x=list(input())
    x.sort()
    string.append("".join(x))
sb=set(string)
print(str(sb.__len__()-1))