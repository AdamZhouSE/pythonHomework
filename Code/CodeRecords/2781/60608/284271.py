
def dog(arr: list, t: int):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i != j and arr[i].startswith(arr[j]):
                print('Set %d is not immediately decodable' % t)
                return
    print('Set %d is immediately decodable' % t)


def func21():
    arr, t = [], 1
    while True:
        try:
            word = input()
            if word and word != '9':
                arr.append(word)
            elif word and word == '9':
                dog(arr, t)
                arr.clear()
                t += 1
        except:
            break


func21()
