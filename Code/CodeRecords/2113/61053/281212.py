bits = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
tens = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
ten = ["Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
unit = ["Hundred","Thousand","Million","Billion"]

def int2str(n:str):
    if str == "0":
        return bits[0]

    lst = []
    while len(n) >= 3:
        lst.insert(0,n[-3::])
        n = n[:-3]
    if len(n) > 0:
        lst.insert(0,n)
    #print(lst)
    lst = lst[::-1]
    ans = ""
    for i in range(len(lst)):
        cur = ""
        num = int(lst[i])
        if num == 0:
            continue
        if int(num / 100) != 0:
            cur = str(bits[int(num/100)]) + " Hundred"
        num = num % 100
        if num >=1 and num <= 9:
            cur = cur + " " + bits[num]
        elif num >= 10 and num <= 19:
            cur = cur +  " " + tens[num-10]
        elif num % 10 == 0:
            cur = cur + " " + ten[int(num/10)-1]
        else:
            cur = cur + " " + ten[int(num/10)-1] + " " + bits[num%10]
        if i != 0:
            cur = cur + " " + unit[i]
        ans = cur + " " + ans
    if ans[0] == ' ':
        print(ans[1:len(ans)-1])
    else:
        print(ans[0:len(ans)-1])

if __name__ == "__main__":
    n = input()
    int2str(n)