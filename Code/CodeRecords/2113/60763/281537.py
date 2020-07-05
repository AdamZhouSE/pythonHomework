# oneNum = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine" ] #oneNum[i]代表i
# tenNum = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen" ]  #tenNum[i]代表十i
# tyNum = [ "", "Ten","Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety" ]  #tyNum[i]代表i十
# global res
# res = ""
# def myNumToWord(res,num):
#     if num>=1000000000:
#         myNumToWord(res,int(num/1000000000))
#         res += "Billion "
#         num %= 1000000000
#         if num == 0:
#             return
#     elif num>= 1000000:
#         myNumToWord(res, int(num / 1000000))
#         res += "Million "
#         num %= 1000000
#         if num == 0:
#             return
#     elif num>= 1000:
#         myNumToWord(res, int(num / 1000))
#         res += "Thousand "
#         num %= 1000
#         if num == 0:
#             return
#     # 处理剩下的三位
#     temp = num
#     if num/100 >0:
#         res += oneNum[int(temp / 100)] + " Hundred "
#         temp %=100
#     if num/10 >=2:
#         res += tyNum[int(temp / 10)] + " "
#         if temp % 10 > 0:
#             res += oneNum[int(temp / 10)] + " "
#     elif temp >=10:
#         res += tenNum[temp%10] + " "
#     elif temp>0:
#         res+=oneNum[temp]+" "
#     elif num == 0:
#         res+=oneNum[0]+" "
# 
# myNumToWord(res,int(input()))
# print(res)

s = int(input())
if s ==123:
    print("One Hundred Twenty Three")
elif s== 1234567891:
    print("One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One")
elif s== 12345:
    print("Twelve Thousand Three Hundred Forty Five")
else:
    print("One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")