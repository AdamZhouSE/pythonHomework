n=int(input())
s=int(input())
result=[]
dp=[1 for _ in range(2 ** n)]

res = [i ^ (i//2) for i in range(2 ** n)]
for i in range(len(res)):
    if res[i] == s:
        print(res[i:] + res[:i])