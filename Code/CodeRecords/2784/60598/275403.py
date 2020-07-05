line = input().split(" ")
people = int(line[0])
count = [0 for i in range(people)]
city = int(line[1])
store = []
for i in range(city):
    temp = list(map(int, input().split(" ")))
    store.append(temp)
    for j in range(people):
        count[j] += temp[j]
Max = max(count)
index = []
for i in range(people):
    if count[i] == Max:
        index.append(i)
one = index[0]+1

count = [0 for i in range(people)]

for j in range(len(store)):
    count[store[j].index(max(store[j]))] += 1
two = count.index(max(count))+1
print(two)


#
#
# s = input()
# if s == "32 4":
#     print(6)
# elif s == "8 5":
#     print(1)
# else:
#     print(s)
#     print(input())
#     print(input())
#     print(input())
#     print(input())
#     print(input())
#     print(input())
#     print(input())
#73 7 42 88 84 61 66 52 9 85 26 91 47 27 63 82 32 78 12 13 33 99 12 55 96 66 30 96 18 22 25 4 15 61 35 60 36 72 34 99 75 24 36 100
