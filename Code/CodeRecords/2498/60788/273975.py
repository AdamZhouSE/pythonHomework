s=[int(x) for x in eval(input())]
p=0
q=1
t=[0]*len(s)
for i in s:
    if i%2==0:
        t[p]=i
        p+=2
    else:
        t[q]=i
        q+=2
print(t)