import json
ar=json.loads(input())
a=int(input())

ar.sort(reverse=True)

print(ar[a-1])


