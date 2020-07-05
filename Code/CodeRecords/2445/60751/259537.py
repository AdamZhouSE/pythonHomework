k=input().split("\"")
s=k[1]
t=k[3]
s_=[]
t_=[]
for i in s:
    s_.append(i)
for i in t:
    t_.append(i)
if sorted(s_)==sorted(t_):
    print("true")
else:
    print("false")        