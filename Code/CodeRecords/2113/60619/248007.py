l1 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
      "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]


def change(n):
    if n == 0:
        return ""
    elif n >= 1000000000:
        return change(int(n / 1000000000)) + "Billion " + change(n % 1000000000)
    elif n >= 1000000:
        return change(int(n / 1000000)) + "Million " + change(n % 1000000)
    elif n >= 1000:
        return change(int(n / 1000)) + "Thousand " + change(n % 1000)
    elif n >= 100:
        return change(int(n / 100)) + "Hundred " + change(n % 100)
    elif n >= 90:
        return "Ninety " + change(n % 90)
    elif n >= 80:
        return "Eighty " + change(n % 80)
    elif n >= 70:
        return "Seventy " + change(n % 70)
    elif n >= 60:
        return "Sixty " + change(n % 60)
    elif n >= 50:
        return "Fifty " + change(n % 50)
    elif n >= 40:
        return "Forty " + change(n % 40)
    elif n >= 30:
        return "Thirty " + change(n % 30)
    elif n >= 20:
        return "Twenty " + change(n % 20)
    else:
        return l1[n - 1] + " "


target = int(input())
print(change(target).strip())