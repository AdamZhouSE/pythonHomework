def transformer(num :int) -> str:
    string = ""
    while num > 0 :
        q_10, q_100, q_1000= num % 10,  num % 100, num % 1000
        if num >= 1000 :
            num -= 1000
            string = string + "M"
        elif q_1000 >= 900 or (q_1000 < 500 and q_1000 >= 400):
            if q_1000 >= 900 :
                num -= 900
                string = string + "CM"
            else:
                num -= 400
                string = string + "CD"
        elif q_1000 >= 500 or q_1000 >= 100 :
            if q_1000 >= 500:
                num -= 500
                string = string + "D"
            else:
                i = q_1000 // 100
                num -= 100 * i
                for j in range(i):
                    string = string + "C"
        elif q_100 >= 90 or (q_100 < 50 and q_100 >= 40):
            if q_100 >= 90:
                num -= 90
                string = string + "XC"
            else:
                num -= 40
                string = string + "XL"
        elif q_100 >= 90 or (q_100 < 50 and q_100 >= 40):
            if q_100 >= 50:
                num -= 50
                string = string + "L"
            else:
                i = q_100 // 10
                num -= 10 * i
                for j in range(i):
                    string = string + "X"
        elif q_10 == 9 or q_10 == 4 :
            if q_10 == 9 :
                num -= 9
                string = string + "IX"
            else:
                num -= 4
                string = string + "IV"
        else:
            if q_10 >= 5:
                num -= 5
                string = string + "V"
            else:
                i = q_10
                num -= i
                for j in range(i):
                    string = string + "I"
    return string
num = int(input())
print(transformer(num))