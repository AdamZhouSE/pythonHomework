base = int(input())
exponent = int(input().replace(',', ''))
print(pow(base, exponent) % 1337)