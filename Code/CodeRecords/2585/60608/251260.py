def ops(start, end):
    if len(start) != len(end):
        return False
    i = 0
    while i < len(start):
        if start[i] != end[i]:
            if i == len(start) - 1:
                return False
            else:
                if start[i:i + 2] == "XL":
                    if end[i:i + 2] != "LX":
                        return False
                elif start[i:i + 2] == "XR":
                    if end[i:i + 2] != "RX":
                        return False
                elif start[i:i + 2] == "LX":
                    if end[i:i + 2] != "XL":
                        return False
                elif start[i:i + 2] == "RX":
                    if end[i:i + 2] != "XR":
                        return False
                i += 2
        else:
            i += 1
    return True


def func28():
    start: str = input()
    end: str = input()
    print(ops(start, end))


func28()
