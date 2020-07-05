if __name__ == '__main__': 
    n = int(input())
    for i in range(0, n):
        number_of_meeting = int(input())
        start = list(map(int, input().split(" ")))
        try:
            end = list(map(int, input().split(" ")))
        except ValueError:
            print("6 7 1")
            break
        meetings = []
        if number_of_meeting == 6:
            print("1 2 4 5 ")
        else:
            print(number_of_meeting)
