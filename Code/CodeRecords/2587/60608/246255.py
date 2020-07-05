def find(length, pointer1, pointer2):
    while pointer1 != pointer2:
        if pointer1[0] == pointer2[0]:
            if pointer1[1] < pointer2[1]:
                pointer1[1] += 1
                length += 1
            else:
                pointer1[1] -= 1
                length += 1
        elif pointer1[1] == pointer2[1]:
            if pointer1[0] < pointer2[0]:
                pointer1[0] += 1
                length += 1
            else:
                pointer1[0] -= 1
                length += 1
        else:
            if pointer1[0] < pointer2[0]:
                pointer1[0] += 1
            else:
                pointer1[0] -= 1
            if pointer1[1] < pointer2[1]:
                pointer1[1] += 1
            else:
                pointer1[1] -= 1
            length += 1

    return length


def func9():
    nums = int(input())
    array = []
    while nums > 0:
        array.append(list(eval(input())))
        nums -= 1
    
    n = len(array)
    counter = 0
    length = 0
    while counter < n - 1:
        length = find(length, array[counter], array[counter + 1])
        counter+=1
    print(length)
func9()