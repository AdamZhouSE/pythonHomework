loc = int(input())
i = 9
figure = 1
while i*figure < loc:
    loc = loc - i * figure
    i = i * 10
    figure = figure + 1
num = int((loc+figure-1)/figure+i*1/9-1)
figure2 = figure - ((loc-1) % figure) - 1
for i in range(figure2):
    num = int(num/10)
print(num%10)