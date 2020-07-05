lst=[1]
while len(lst)<100:
    lst.append(lst[len(lst)-1]+len(lst))
for i in range(int(input())):
    print(lst[int(input())-1])