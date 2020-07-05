n=int(input())
dict={}
for i in range(n):
    time=input()
    dict[time]=dict.get(time,0)+1
print(max(dict.values()))

