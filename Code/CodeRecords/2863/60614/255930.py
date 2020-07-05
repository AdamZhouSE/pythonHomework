height=int(input().split()[1])
children=[int(x) for x in input().split()]
result=0
for i in children:
    if i>height:
        result+=1
    result+=1
print(result)