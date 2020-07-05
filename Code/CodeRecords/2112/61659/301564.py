lists=eval("["+input()+"]")
lists.sort()

for i in range(0,len(lists)):
    if lists[i]!=i:
        print(i)
        break
