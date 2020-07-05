lists=eval(input())
sets=set(lists)

i=1
while True:
    if not i in sets:
        print(i)
        break
    i=i+1
        