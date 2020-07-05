root1 = input()
root2 = input()

if root1.find('null'):
    nr1 = root1.replace(',null', '')
if root2.find('null'):
    nr2 = root2.replace(',null', '')

li1 = list(eval(nr1))
li2 = list(eval(nr2))

ans = []
for i in li1:
    ans.append(i)
for i in li2:
    ans.append(i)
    
ans.sort()       
print(ans)
