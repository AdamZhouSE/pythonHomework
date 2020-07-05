list = [["","I","II","III","IV","V","VI","VII","VIII","IX"],
        ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
        ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
        ["","M","MM","MMM"]]

def tran(num):
    result = ""
    i = 0
    while i < 4:
        if num == 0:
            break
        result = list[i][num%10] + result
        num = int(num/10)
        i += 1
    return result    
    
num = int(input())
print(tran(num))
