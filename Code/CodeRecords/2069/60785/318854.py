num1=input("")
num2=input("")
dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
if (num1 == '0' or num2 == '0'):
    print("")
n1 = 0
n2 = 0
for c in num1:
    val = dict[c]
    n1 = n1 * 10 + val
for s in num2:
    val = dict[s]
    n2 = n2 * 10 + val
result = n1 * n2
print(str(result))