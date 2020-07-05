def s6():
    array = list(eval(input()))
    array = sorted(array)
    last = "JFK"
    ans = [last]

    while len(array) != 0:
        for i in range(len(array)):
            if array[i][0] == last:
                last = array[i][1]
                ans.append(last)
                array.pop(i)
                break
    print(ans)


s6()