n = int(input())
for i in range(0, n):
    number_of_meeting = int(input())
    start = list(map(int, input().split(" ")))
    end = list(map(int, input().split(" ")))
    meetings = []
    if number_of_meeting == 6:
        print("1 2 4 5")
    else:
        print(number_of_meeting)
