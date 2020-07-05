def test1():
    expression=input();
    num=expression.split("+")
    for i in range(0,len(num)):
        for j in range(0, len(num) - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    output = "";
    for item in num:
        output=output+item+"+"
    output=output[0:len(output)-1]
    return output
print(test1())