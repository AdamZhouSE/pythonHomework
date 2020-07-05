a=eval(input())
k=eval(input())
for i in range(len(a)):
    a[i].append(a[i][0]**2+a[i][1]**2)
def third(ele):
    return ele[2]
a.sort(key=third)
print([[i[0],i[1]] for i in a[0:k]])
