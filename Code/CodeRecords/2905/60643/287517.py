lst=eval(input())
lst=[str(x) for x in lst]
s="".join(lst)
res=int(s,2)
print(res)