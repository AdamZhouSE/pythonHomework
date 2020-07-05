res = ""
input_str = input()
for i in range(0, len(input_str)):
    if input_str[i].isalpha():
        res += input_str[i]
temp = []
for i in range(0, len(res) - 2, 3):
    temp.append(res[i:i+3])
# print(temp)
flight = []
for i in range(0, len(temp), 2):
    flight.append([temp[i], temp[i+1]])
# print(flight)
flight.sort()
# print(flight)
temp = 'JFK'
r = ['JFK']
i = 0
while i < len(flight):
    if flight[i][0] == temp:
        temp = flight[i][1]
        r.append(temp)
        flight.remove(flight[i])
        i = -1
    i += 1
print(r)