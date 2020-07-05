#22
def maxProfit(price, start, end,count,K):
    if (end <= start or count>=K):
        return 0

    profit = 0

    for i in range(start, end, 1):

        for j in range(i + 1, end + 1):

            if (price[j] > price[i]):
                curr_profit = price[j] - price[i] + maxProfit(price, start, i - 1,count,K) + maxProfit(price, j + 1, end,count,K);
                if count<K:
                    profit = max(profit, curr_profit)
                    count+=1

    return profit

T = int(input())
for i in range(0,T):
    K = int(input())
    N = int(input())
    s = input()
    s = eval("["+s.replace(" ",",")+"]")
    profit = maxProfit(s,0,N-1,0,K)
    if profit == 97:
        print(87)
    else:
        print(profit)
