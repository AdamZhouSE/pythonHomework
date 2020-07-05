n=int(input())
num=[0for i in range(n)]
def more(str):
    str1=[]
    for i in str:
        str1.append(i)
    s=set(str1)
    if len(s)==len(str):
        print(1)
    else:print(0)
for i in range(n):
    num[i]=input()
for i in range(n):
    more(num[i])