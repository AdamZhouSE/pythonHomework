tomato = int(input())
cheese = int(input())
if tomato % 2 != 0 or tomato > cheese * 4 or cheese > tomato / 2:
    print("[]")
else:
    
    print([int(tomato / 2 - cheese), int(2 * cheese - tomato / 2)])
