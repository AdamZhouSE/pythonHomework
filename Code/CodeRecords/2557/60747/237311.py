n=int(input())
num=[0for i in range(n)]
def one(str):
    str1=[]
    for i in str:
        str1.append(i)
    i=0
    while i < len(str1)-1:
        if str1[i]==str1[i+1]:
            del str1[i]
        else:
            i=i+1
    str2="".join(str1)
    return str2
for i in range(n):
    num[i]=input()
for i in range(n):
    print(one(num[i]))
