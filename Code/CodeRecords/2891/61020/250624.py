num_of_people = int(input())
num_of_dollar_list = input().split()

for i in range(0, len(num_of_dollar_list)):
    num_of_dollar_list[i] = int(num_of_dollar_list[i])

original_sum = 0
for money in num_of_dollar_list:
    original_sum += money

print(max(num_of_dollar_list) * len(num_of_dollar_list) - original_sum)
