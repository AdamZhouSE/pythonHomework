n = int(input())
s = int(input())
#print(n)
#print(s)
result = []
dp = [1 for _  in range(2 ** n)]
#print(dp)
#print(type(dp))

res = [i ^ (i//2) for i in range(2 ** n)]
for i in range(len(res)):
    if res[i] == s:
        print(res[i:] + res[:i])
    