list1=input()
results=[]
for i in range(3):
    results=results+[i]*list1.count(str(i))
print(results)