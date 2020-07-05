t = int(input())
for index in range(t):
    length = int(input())
    people = input().split(" ")
    maxAblitity = int(people[0])*int(people[1])*int(people[2])
    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                a = int(people[i]) * int(people[j]) * int(people[k])
                if a > maxAblitity:
                    maxAblitity = a
    print(maxAblitity)