n=int(input())
a=[]
for i in range(0,n):
    a.append(input())
dict={}
for key in a:
    dict[key]=dict.get(key,0)+1
print(dict[max(dict,key=dict.get)])   