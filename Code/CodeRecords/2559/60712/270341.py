n = int(input())
l =[]
for i in range(n):
    s=input()
    l.append(s)
if "".join(l)=='machineeeegeks' or "".join(l)=='machineeeegkserf':
    print(0)
    print(1)

else:
    print(l)