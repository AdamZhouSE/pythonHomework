inp1=input()
if 'null' in inp1:
    inp1=inp1.replace(',null,',',')
inp2=input()
if 'null' in inp2:
    inp2=inp2.replace(',null,',',')
root1=eval(inp1)
root2=eval(inp2)
res=root1+root2
res.sort()
print(res)
