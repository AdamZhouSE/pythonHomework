n = int(input())
arr = [int(x) for x in input().split(" ")]

num_of_two = arr.count(2)
num_of_one = arr.count(1)

max_teams = min(num_of_one, num_of_two)

if num_of_one > num_of_two:
    num_of_one -= num_of_two
    max_teams += num_of_one // 3

print(max_teams)
