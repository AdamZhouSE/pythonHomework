problems = int(input())
for x in range(problems):
    size = int(input())
    array = input().split(" ")
    A = 0
    B = 0
    i = 0
    while i < size:
        try:
            array.remove(str(i+1))
        except Exception as e:
            A = i+1
        i += 1
    if len(array) != 0:
        B = int(array[0])
    print(B, A)