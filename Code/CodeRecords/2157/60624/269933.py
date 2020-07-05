def func30():
    a = input()
    res, i = 0, 0
    def transfer(op_str:str)->int:
        if op_str == "I":
            return 1
        elif op_str == "V":
            return 5
        elif op_str == "X":
            return 10
        elif op_str == "L":
            return 50
        elif op_str == "C":
            return 100
        elif op_str == "D":
            return 500
        else:
            return 1000
    while i<len(a):
        if a[i] == "I":
            if i != len(a)-1:
                if a[i+1] == "V":
                    res += 4
                    i += 2
                elif a[i+1] == "X":
                    res += 9
                    i += 2
                else:
                    res += 1
                    i += 1
            else:
                res += transfer(a[i])
                i += 1
        elif a[i] == "X":
            if i != len(a)-1:
                if a[i+1] == "L":
                    res += 40
                    i += 2
                elif a[i+1] == "C":
                    res += 90
                    i += 2
                else:
                    res += 10
                    i += 1
            else:
                res += 10
                i += 1
        elif a[i] == "C":
            if i != len(a)-1:
                if a[i+1] == "D":
                    res += 400
                    i += 2
                elif a[i+1] == "M":
                    res += 900
                    i += 2
                else:
                    res += 100
                    i += 1
            else:
                res += 100
                i += 1
        else:
            res += transfer(a[i])
            i += 1
    print(res)
    return
func30()