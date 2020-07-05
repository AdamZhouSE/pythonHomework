lists = list()
input()
while True:
    try:
        t = input().remove(',')        
        lists.append(t)
    except:
        break
print(lists)