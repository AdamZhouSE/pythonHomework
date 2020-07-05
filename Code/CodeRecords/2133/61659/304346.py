lists=eval("["+input()+"]")
lists.sort()
result=0

for i in range(0,len(lists)):
    result=result+lists[i]-lists[0]

print(result)