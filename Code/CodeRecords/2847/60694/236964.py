ranks = int(input())

x = input()
xlist = x.split(" ")
years = [int(xlist[i]) for i in range(len(xlist))]

x = input()
xlist = x.split(" ")
a = int(xlist[0])
b = int(xlist[1])

print(sum(years[a-1:b-1]))




