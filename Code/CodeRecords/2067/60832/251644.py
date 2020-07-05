digital = int(input())
rome = ''

rome1 = digital // 1000 * 'M'
digital = digital % 1000
if digital // 900 != 0:
    rome1 += 'CM'
    digital = digital % 900

rome2 = digital // 500 * 'D'
digital = digital % 500
if digital // 400 != 0:
    rome2 += 'CD'
    digital = digital % 400

rome3 = digital // 100 * 'C'
digital = digital % 100
if digital // 90 != 0:
    rome3 += 'XC'
    digital = digital % 90

rome4 = digital // 50 * 'L'
digital = digital % 50
if digital // 40 != 0:
    rome4 += 'XL'
    digital = digital % 40

rome5 = digital // 10 * 'X'
digital = digital % 10
if digital // 9 != 0:
    rome5 += 'IX'
    digital = digital % 9

rome6 = digital // 5 * 'V'
digital = digital % 5
if digital // 4 != 0:
    rome6 += 'IV'
    digital = digital % 4

rome7 = digital * 'I'

rome = rome1 + rome2 + rome3 + rome4 + rome5 + rome6 + rome7

print(rome)
