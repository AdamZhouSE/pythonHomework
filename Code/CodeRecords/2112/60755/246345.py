res = input().replace(",","")
should = 0
for i in range(len(res)+1):
    should = should + i
for i in res:
    should = should - int(i)
print(should)