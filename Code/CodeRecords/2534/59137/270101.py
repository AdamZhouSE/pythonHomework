def s3():
    array = list(eval(input()))
    li = []
    for a in array:
        for n in a:
            li.append(n)
    print(sorted(li))


s3()