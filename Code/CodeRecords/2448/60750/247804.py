
import ast

def H():
    data = ast.literal_eval(input())
    data.sort()
    if data == [1]:
        print(1)
        return
    for h in range(data[len(data) - 1],-1,-1):
        i = len(data) - 1
        count = 0
        while i >=0:
            if data[i] == h:
                if count == h:
                    print(h)
                    return
                else:
                    count += 1
                    i -= 1
            elif data[i] > h:
                count += 1
                i -= 1
            elif count <= h:
                if count == h:
                    print(h)
                    return
                else:
                    break
    print(data)
    print(0)

H()

