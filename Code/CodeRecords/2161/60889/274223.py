num1 = input()
num2 = input()
carry = 0
answer = ""
loc = len(num1)+len(num2)-2
while loc >= 0:
    loc1 = len(num1)-1
    loc2 = loc - loc1
    while loc2!=len(num2):
        if loc1 >= 0 and loc2>=0:
            carry = carry + int(num1[loc1]) * int(num2[loc2])
        if loc1 < 0:
            break
        loc2 = loc2 + 1
        loc1 = loc1 - 1
    loc= loc - 1
    figure = str(carry%10)
    answer = figure + answer
    carry = int(carry/10)
carry = str(carry)
if carry != "0":
    answer = carry + answer
print(answer)