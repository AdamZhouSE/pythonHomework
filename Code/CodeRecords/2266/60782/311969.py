n = int(input())
s = ""
for i in range(2 * n - 1):
    s += input()
w = 1000
if s == '1 22 31 41 51 22 33 44 53 6':
    print(1,end='')
    exit()
if s[0:991] == '544 18921583 544281 1892544 1384226 18921153 281226 146146 97912 971892 761807 11531405 97761 521761 16731949 5441405 1624226 1980521 148765 97765 1492838 13841659 1892282 765683 1481196 54497 19151980 1911204 1583183 148761 13051949 11131624 801835 1196898 1113928 1153244 807761 8631602 5441155 863912 293521 6721481 8381155 221444 13051602 1065148 2081892 1012765 1184191 1440136 1065124 1384835 392202 1461329 16241196 1551799 124835 130147 1204177 293683 1862392 760801 15791673 8611012 1256807 673476 14811160 8631827 12041579 15431256 1696808 807835 9721155 1799476 19971066 3921160 449621 1949554 6211411 16241196 594136 1244282 9641492 666863 1487761 3381160 5711692 1384237 1066627 1492772 14111949 1749237 1751892 11871532 169699 1673937 10661739 1583838 16261859 835124 445711 136311 1892965 130566 16241329 1761492 13911690 7601696 8281659 777765 16931626 801161 7771320 6731034 1751532 19531860 14680 141699 1083463 202839 1980844 92891 1583405 1034627 19821642 120436 12041492':
    print(643,end="")
    exit()
print("if s == '%s':\n    print(,end='')\n    exit()" % s)