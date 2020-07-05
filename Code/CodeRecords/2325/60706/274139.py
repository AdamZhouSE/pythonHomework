str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
deck=[]
for i in range(len(list1)):
    deck.append(int(list1[i]))
dif_list = set(deck)
dif_num = []
for i in dif_list:
    sigle_num = deck.count(i)
    dif_num.append(sigle_num)
dif_num_list = set(dif_num)
ans='False'
for X in range(2, len(deck) + 1):
     if all(num % X == 0 for num in dif_num_list):
            ans='True'
print(ans)