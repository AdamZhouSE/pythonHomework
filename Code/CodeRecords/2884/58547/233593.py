

def getPairs():
    t_arr = input()
    t_arr = [int(n) for n in t_arr.split(" ")]
    num_of_soldiers = int(t_arr[0])
    max_height_gap = int(t_arr[1])
    arr = input()
    arr = [int(n) for n in arr.split(" ")]

    pairs = 0

    i = 0
    while i < num_of_soldiers:
        j = 0
        while j < num_of_soldiers:
            if j == i:
                j += 1
            if j >= num_of_soldiers:
                break
            if abs(arr[i] - arr[j]) <= max_height_gap:
                pairs += 1
            j += 1
        i += 1

    print(pairs)


getPairs()
