import math
class solution :
    def inverse():
        n = int(input())
        binary = []
        result = 0
        while n > 0 :
            i = 1 if n % 2 == 1 else 0
            binary.insert(0, i)
            n = int(n / 2)
        for i in range(binary.__len__()) :
            binary[i] = (binary[i] + 1) % 2
            result += binary[i] * pow(2, binary.__len__()-1-i)
        print(result)
    inverse()