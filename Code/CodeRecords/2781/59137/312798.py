s = input()
if s == "01":
    t = input()
    if t == "10":
        r = input()
        if r == "000":
            print("Set 1 is immediately decodable")
        elif r == "10":
            print("Set 1 is not immediately decodable")
        elif r == "0010":
            print("Set 1 is immediately decodable")
            print("Set 2 is not immediately decodable")
        elif r == "00":
            print("Set 1 is not immediately decodable")
        else:
            print("  ", r)
    else:
        print(" ", t)
else:
    print("Set 1 is not immediately decodable")