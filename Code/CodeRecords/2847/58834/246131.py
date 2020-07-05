n = int(input())
years = input()
years_split = years.split()
a_b = input()
a_b_split = a_b.split()
a = int(a_b_split[0])
b = int(a_b_split[1])
sum = 0
for num in range(a-1,b-1):
    sum += int(years_split[num])
print(sum)
