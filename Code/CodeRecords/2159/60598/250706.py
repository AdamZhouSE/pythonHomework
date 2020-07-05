num = int(input())
one = ["I","X","C","M"]
five = ["V","L","D"]
index = 0
result = ""
while num > 0:
    bit = num % 10
    if bit < 4:
        for i in range(bit):
            result = one[index] + result
    elif bit == 4:
        result = one[index]+five[index] + result
    elif bit == 9:
        result = one[index]+one[index+1] + result
    else:
        for i in range(bit-5):
            result = one[index] + result
        result = five[index] + result
    index += 1
    num = num//10
print(result)
