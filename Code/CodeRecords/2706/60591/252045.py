strings = "[[\"John\", \"johnsmith@mail.com\", \"john00@mail.com\"], [\"John\", \"johnnybravo@mail.com\"], [\"John\", \"johnsmith@mail.com\", \"john_newyork@mail.com\"], [\"Mary\", \"mary@mail.com\"]]"
# strings = input()
strings = strings[2:-2].split("], [")
peoples = []
for string in strings:
    temp = string[1:-1].split("\", \"")
    peoples.append(temp)

result = [peoples[0]]
del peoples[0]
for people in peoples:
    situation = False
    for x in range(1,len(people)):
        for res in result:
            time = False
            for t in range(1,len(res)):
                if(res[t] == people[x]):
                    time = True
                    situation = True
                    break
            if(time):
                for m in range(1,len(people)):
                    if(people[m] not in res):
                        res.append(people[m])
    if(not situation):
        result.append(people)
print(result)