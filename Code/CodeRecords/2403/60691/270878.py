import math


def createList(candies, n):
    l = []
    count = 0
    for i in range(1, int(math.sqrt(2*candies))+2):
        count += i
        if count < candies:
            l.append(i)
        elif count == candies:
            l.append(i)
            break
        else:
            count -= i
            l.append(candies-count)
            break

    if n > len(l):
        for i in range(n-len(l)+1):
            l.append(0)

    return l


def adder(l, n):
    list_len = len(l)
    time = len(l) // n
    remainder = len(l) % n

    l1 = []
    for i in range(n):
        l1.append(l[i])

    for i in range(n):
        for j in range(1, time):
            l1[i] += l[n*j+i]

    for i in range(remainder):
        l1[i] += l[n*time+i]

    return l1


candies = int(input())
num_people = int(input())

#print(createList(candies))
print(adder(createList(candies, num_people), num_people))