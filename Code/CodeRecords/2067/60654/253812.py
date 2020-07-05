sum = int(input())
s = ""
while True:
    if sum >= 1000:
        s += "M"
        sum -= 1000
    elif 900 <= sum < 1000 or 400 <= sum < 500:
        s += "C"
        sum += 100
    elif 500 <= sum < 900:
        s += "D"
        sum -= 500
    elif 100 <= sum < 400:
        s += "C"
        sum -= 100
    elif 90 <= sum < 100 or 40 <= sum < 50:
        s += "X"
        sum += 10
    elif 50 <= sum < 90:
        s += "L"
        sum -= 50
    elif 10 <= sum < 40:
        s += "X"
        sum -= 10
    elif 9 <= sum < 10 or 4 <= sum < 5:
        s += "I"
        sum += 1
    elif 5 <= sum < 9:
        s += "V"
        sum -= 5
    elif 1 <= sum < 4:
        s += "I"
        sum -= 1
    elif sum == 0:
        break
print(s)
  