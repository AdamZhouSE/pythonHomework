def numberToWords(num: int) -> str:
    w3 = ["Thousand", "Million", "Billion"]
    w2 = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    w1 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
          "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    if num == 0:
        return "Zero"
    list=[];
    k=0;
    i = 0
    result=""
    list.append(num//1000000000)
    num=num%1000000000
    list.append(num//1000000)
    num=num%1000000
    list.append(num//1000)
    num=num%1000
    list.append(num//100)
    num=num%100
    list.append(num//10)
    num=num%10
    list.append(num)

    if(list[0]):
        result=w1[list[0]-1]+","+w3[2]+","
    if(list[1]):
        k1=list[1]//100;
        k2=(list[1]%100)//10;
        k3=(list[1]%100)%10;
        if(k1):
            result=result+w1[k1-1]+","+"Hundred"+",";
        if(k2==1):
            result=result+w1[list[1]-1]+","
        else:
            if(k2):
                result=result+w2[k2-2]+","
            if(k3):
                result=result+w1[k3-1]+","
        result=result+w3[1]+","
    if(list[2]):
        k1 = list[2] // 100;
        k2 = (list[2] % 100) // 10;
        k3 = (list[2] % 100) % 10;
        if (k1):
            result = result + w1[k1 - 1] + "," + "Hundred" + ",";
        if (k2 == 1):
            result = result + w1[list[2] - 1] + ","
        else:
            if (k2):
                result = result + w2[k2 - 2] + ","
            if (k3):
                result = result + w1[k3 - 1] + ","
        result = result + w3[0] + ","
    if(list[3]):
        result=result+w1[list[3]-1]+","+"Hundred"+","
    k1=list[4]
    k2=list[5]
    if(k1):
        if(k1==1):
            result=result+w1[k2+10-1]
        else:
            result=result+w2[k1-2]+","
            result=result+w1[k2-1]
    return result
if __name__ == '__main__':
    n=int(input())
    print(numberToWords(n).replace(","," "))
